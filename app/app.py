
import sys
import os

# add project root vào path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from src.predict import predict_price

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title("🚗 Car Price Predictor")

age = st.slider("Age", 0, 15, 3)
km_per_year = st.slider("KM/year", 0, 50000, 10000)
hp_kW = st.slider("Power", 50, 300, 100)
weight = st.slider("Weight", 800, 2500, 1300)

if st.button("Predict"):

    car = {
        "age": age,
        "km_per_year": km_per_year,
        "hp_kW": hp_kW,
        "Weight_kg": weight
    }

    price = predict_price(car)

    st.markdown("## 💰 Estimated Price")
    st.success(f"{int(price):,} VND")

    # pricing strategy
    st.markdown("## 📊 Pricing Strategy")
    col1, col2, col3 = st.columns(3)

    col1.metric("Quick Sale", f"{int(price*0.95):,}")
    col2.metric("Market Price", f"{int(price):,}")
    col3.metric("Premium", f"{int(price*1.05):,}")

    # confidence
    st.markdown("## 📉 Confidence Range")
    st.info(f"{int(price*0.85):,} → {int(price*1.15):,} VND")


    st.markdown("## 🧠 Why this price?")

    if km_per_year > 20000:
        st.write("• High mileage → giảm giá")

    if age > 5:
        st.write("• Xe cũ → giảm giá")

    if hp_kW > 120:
        st.write("• Công suất cao → tăng giá")

    if weight > 1500:
        st.write("• Xe nặng → thường thuộc phân khúc cao hơn")