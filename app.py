# ==========================================================
# STREAMLIT APP - KLASIFIKASI TEKS
# LSTM (PyTorch) | BERT | DistilBERT
# ==========================================================

import os, json, pickle
import streamlit as st
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from transformers import (
    BertTokenizer, BertForSequenceClassification,
    DistilBertTokenizer, DistilBertForSequenceClassification
)

from sklearn.preprocessing import LabelEncoder

# ==========================================================
# STREAMLIT CONFIG
# ==========================================================
st.set_page_config(
    page_title="Dashboard Klasifikasi Teks",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# HEADER
# ==========================================================
st.markdown(
    """
    <h1 style='text-align:center;'>📊 Dashboard Klasifikasi Teks</h1>
    <p style='text-align:center; color:gray;'>
    Perbandingan Model LSTM, BERT, dan DistilBERT
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# PAD SEQUENCES
# ==========================================================
def pad_sequences(seqs, maxlen=100):
    return np.array([
        s[:maxlen] + [0] * (maxlen - len(s)) if len(s) < maxlen else s[:maxlen]
        for s in seqs
    ])

# ==========================================================
# LOAD DATASET
# ==========================================================
@st.cache_data
def load_data():
    train = pd.read_csv("dataset/train.csv")
    test = pd.read_csv("dataset/test.csv")
    return train, test

train_df, test_df = load_data()

label_encoder = LabelEncoder()
train_df["label_enc"] = label_encoder.fit_transform(train_df["Label"])
num_labels = len(label_encoder.classes_)

# ==========================================================
# SIDEBAR
# ==========================================================
st.sidebar.header("⚙️ Konfigurasi Model")

bert_ok = os.path.exists("models/bert_output/checkpoint-1000")
distil_ok = os.path.exists("models/distilbert_output/checkpoint-1000")

model_list = ["LSTM"]
if bert_ok:
    model_list.append("BERT")
if distil_ok:
    model_list.append("DistilBERT")

model_choice = st.sidebar.selectbox(
    "Pilih Model Klasifikasi",
    model_list
)

st.sidebar.info(
    f"""
    **Model Aktif:** {model_choice}  
    **Jumlah Label:** {num_labels}
    """
)

# ==========================================================
# SAMPLE DATASET
# ==========================================================
with st.container():
    st.subheader("📄 Contoh Dataset (Random)")

    samples = []
    for lbl in train_df["Label"].unique():
        samples.append(train_df[train_df["Label"] == lbl].sample(5))

    sample_df = pd.concat(samples).sample(20)[["Text", "Label"]]

    st.dataframe(
        sample_df,
        hide_index=True,
        use_container_width=True
    )

# ==========================================================
# LSTM MODEL
# ==========================================================
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.embedding(x)
        _, (h, _) = self.lstm(x)
        return self.fc(h[-1])

@st.cache_resource
def load_lstm():
    with open("models/lstm_model/config.json") as f:
        cfg = json.load(f)

    with open("models/lstm_model/vocab.pkl", "rb") as f:
        vocab = pickle.load(f)

    model = LSTMClassifier(
        vocab_size=max(vocab.values()) + 1,
        embed_dim=cfg["embed_dim"],
        hidden_dim=cfg["hidden_dim"],
        output_dim=num_labels
    )
    model.load_state_dict(
        torch.load("models/lstm_model/lstm_model.pth", map_location="cpu")
    )
    model.eval()
    return model, vocab

lstm_model, lstm_vocab = load_lstm()

def predict_lstm(texts):
    seqs = [[lstm_vocab.get(w, 0) for w in t.lower().split()] for t in texts]
    x = torch.LongTensor(pad_sequences(seqs))
    with torch.no_grad():
        probs = F.softmax(lstm_model(x), dim=1)
    return probs.argmax(1).numpy(), probs.max(1).values.numpy()

# ==========================================================
# BERT & DISTILBERT
# ==========================================================
def load_transformer(path, is_distil=False):
    if is_distil:
        tok = DistilBertTokenizer.from_pretrained(path)
        mdl = DistilBertForSequenceClassification.from_pretrained(
            path, num_labels=num_labels
        )
    else:
        tok = BertTokenizer.from_pretrained(path)
        mdl = BertForSequenceClassification.from_pretrained(
            path, num_labels=num_labels
        )
    mdl.eval()
    return tok, mdl

if bert_ok:
    bert_tok, bert_model = load_transformer("models/bert_output/checkpoint-1000")

if distil_ok:
    distil_tok, distil_model = load_transformer(
        "models/distilbert_output/checkpoint-1000",
        is_distil=True
    )

def predict_transformer(texts, tokenizer, model):
    inp = tokenizer(
        texts,
        padding=True,
        truncation=True,
        return_tensors="pt"
    )
    with torch.no_grad():
        probs = F.softmax(model(**inp).logits, dim=1)
    return probs.argmax(1).numpy(), probs.max(1).values.numpy()

# ==========================================================
# PREDIKSI
# ==========================================================
st.markdown("---")
st.subheader("✍️ Prediksi Teks")

col1, col2 = st.columns([3, 2])

with col1:
    text = st.text_area(
        "Masukkan teks yang ingin diklasifikasikan",
        height=120,
        placeholder="Contoh: Pemerintah mengumumkan kebijakan ekonomi baru..."
    )

with col2:
    st.markdown("### 📌 Informasi Model")
    st.write(f"**Model:** {model_choice}")
    st.write(f"**Jumlah Kelas:** {num_labels}")

if st.button("🔍 Prediksi", use_container_width=True):
    if text.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        if model_choice == "LSTM":
            pred, conf = predict_lstm([text])
        elif model_choice == "BERT":
            pred, conf = predict_transformer([text], bert_tok, bert_model)
        else:
            pred, conf = predict_transformer([text], distil_tok, distil_model)

        label = label_encoder.inverse_transform(pred)[0]

        st.success(f"📌 **Hasil Prediksi: {label}**")

        c1, c2 = st.columns(2)
        with c1:
            st.metric(
                label="Confidence",
                value=f"{conf[0]*100:.2f}%"
            )
        with c2:
            st.progress(int(conf[0] * 100))
