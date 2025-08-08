import streamlit as st
import pandas as pd

data = {
    "Record No.": [...],
    "Ana Yüklenici": [...],
    "Uygunsuzluğu Tespit Eden": [...],
    "Uygunsuzluk Tespit Tarihi": [...]
}

df = pd.DataFrame(data)
df["Uygunsuzluk Tespit Tarihi"] = pd.to_datetime(df["Uygunsuzluk Tespit Tarihi"], errors='coerce')


st.title("Uygunsuzluk Raporu Dashboard")

st.subheader("Ana Yükleniciye Göre Uygunsuzluk Sayısı")
counts = df["Ana Yüklenici"].value_counts()
st.bar_chart(counts)

st.subheader("Uygunsuzluğu Tespit Eden Kişiye Göre Dağılım")
detector_counts = df["Uygunsuzluğu Tespit Eden"].value_counts()
st.bar_chart(detector_counts)

st.subheader("Zaman İçinde Uygunsuzluklar")
st.line_chart(df.groupby("Uygunsuzluk Tespit Tarihi").size())
