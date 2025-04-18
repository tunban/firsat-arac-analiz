
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fırsat Araç Bulucu", layout="wide")

st.title("🚗 Sahibinden Fırsat Araç Bulucu")

st.markdown("Bu uygulama, Sahibinden.com'daki ilanları manuel olarak inceleyip, mümkün olan araçların tespit edilmesine yardımcı olur. Şu anda demo modudur. Otomatik veri çekme özelliği, gelecekte entegre olur.")

marka = st.text_input("Marka", "Renault")
model = st.text_input("Örnek", "Megane 4")
min_yil = st.number_input("En düşük model yılı", min_value=2000, max_value=2025, value=2016)
max_yil = st.number_input("En yüksek model yılı", min_value=2000, max_value=2025, value=2024)
max_fiyat = st.number_input("Maksimum Fiyat (TL)", value=1100000)
max_km = st.number_input("Maksimum Kilometre", value=200000)

st.info("Bu demo sürümde otomatik ilan verisi çekilmemektedir. Manuel kıyaslama yapılabilir.")

veri = {
    "Başlık": ["2018 Megane 4 Icon", "2017 Megane 4 Touch", "2016 Megane Joy"],
    "Fiyat": [840000, 920000, 735000],
    "Km": [180000, 160000, 273000],
    "Yıl": [2018, 2017, 2016],
    "Durum": ["Fırsat 🚀", "Normal", "Yüksek KM ❌"],
    "Link": [
        "https://www.sahibinden.com/ilan/840",
        "https://www.sahibinden.com/ilan/920",
        "https://www.sahibinden.com/ilan/735"
    ]
}

df = pd.DataFrame(veri)

st.subheader("Analiz Sonuçları (Demo Verisi)")
st.dataframe(df)
