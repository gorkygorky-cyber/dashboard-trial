import streamlit as st
import pandas as pd

data = {
    "Record No.": ["HSENCR-02047", "HSENCR-02046", "HSENCR-02045", "HSENCR-02044", "HSENCR-02043",
                  "HSENCR-02042", "HSENCR-02041", "HSENCR-02040", "HSENCR-02039", "HSENCR-02038",
                  "HSENCR-02037", "HSENCR-02036", "HSENCR-02035", "HSENCR-02034"],
    "Ana Yüklenici": ["VEN-0265", "VEN-0265", "VEN-0265", "VEN-0087", "VEN-0087", "VEN-0087", "VEN-0087",
                      "VEN-0087", "VEN-0087", "VEN-0265", "VEN-0082", "VEN-0082", "VEN-0082", "VEN-0082"],
    "Uygunsuzluğu Tespit Eden": ["BARÇIN BOSUT", "BARÇIN BOSUT", "BARÇIN BOSUT", "MUHAMMED BUĞRA ŞİMŞEK",
                                 "ANIL KESKİN", "MURAT BAYRAK", "ÖCAL KIRANER", "HALİL SERT", "NECMETTİN AKGÜL",
                                 "NECMETTİN AKGÜL", "ANIL KESKİN", "OĞUZHAN BAKİ", "OĞUZHAN BAKİ", "ONUR AKÇALI"],
    "Uygunsuzluk Tespit Tarihi": ["06/24/2025", "06/24/2025", "06/24/2025", "05/28/2025", "05/28/2025",
                                 "05/28/2025", "05/28/2025", "05/28/2025", "05/28/2025", "05/21/2025",
                                 "02/26/2025", "02/26/2025", "02/26/2025", "02/26/2025"]
}

df = pd.DataFrame(data)
df["Uygunsuzluk Tespit Tarihi"] = pd.to_datetime(df["Uygunsuzluk Tespit Tarihi"], errors='coerce')

st.title("Uygunsuzluk Raporu Dashboard")

st.subheader("Ana Yükleniciye Göre Uygunsuzluk Sayısı")
counts = df["Ana Yüklenici"].value_counts().reset_index()
counts.columns = ["Ana Yüklenici", "Adet"]
st.bar_chart(data=counts.set_index("Ana Yüklenici"))

st.subheader("Uygunsuzluğu Tespit Eden Kişiye Göre Dağılım")
detector_counts = df["Uygunsuzluğu Tespit Eden"].value_counts().reset_index()
detector_counts.columns = ["Uygunsuzluğu Tespit Eden", "Adet"]
st.bar_chart(data=detector_counts.set_index("Uygunsuzluğu Tespit Eden"))

st.subheader("Zaman İçinde Uygunsuzluklar")
time_counts = df.groupby("Uygunsuzluk Tespit Tarihi").size().reset_index(name='Adet')
time_counts = time_counts.set_index("Uygunsuzluk Tespit Tarihi")
st.line_chart(time_counts)
