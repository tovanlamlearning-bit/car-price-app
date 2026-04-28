
import sys
import os
import streamlit as st
from src.predict import predict_price
# add project root vào path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))




st.set_page_config(layout="wide")

st.title("🚗 Car Price Predictor (Pro)")

# =====================
# BASIC INFO
# =====================
st.header("📊 Basic Information")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 0, 15, 3)
    km_per_year = st.slider("KM/year", 0, 50000, 10000)

with col2:
    hp_kW = st.slider("Power (hp)", 50, 300, 100)
    weight = st.slider("Weight (kg)", 800, 2500, 1300)

# =====================
# FEATURE COUNTS
# =====================
st.header("🧮 Feature Summary")

col1, col2 = st.columns(2)

with col1:
    comfort_count = st.slider("Comfort features", 0, 20, 5)
    safety_count = st.slider("Safety features", 0, 15, 5)

with col2:
    entertainment_count = st.slider("Entertainment features", 0, 10, 3)
    extras_count = st.slider("Extras", 0, 10, 2)

# =====================
# DETAILED FEATURES (ADVANCED)
# =====================
st.header("⚙️ Advanced Options (Optional)")

with st.expander("Show detailed features"):

    st.subheader("Comfort")
    aircon = st.checkbox("Air Conditioning")
    cruise = st.checkbox("Cruise Control")
    parking = st.checkbox("Parking Sensors")

    st.subheader("Entertainment")
    bluetooth = st.checkbox("Bluetooth")
    radio = st.checkbox("Radio")
    usb = st.checkbox("USB")

    st.subheader("Safety")
    abs = st.checkbox("ABS")
    airbags = st.checkbox("Airbags")

    st.subheader("Extras")
    sport_seats = st.checkbox("Sport Seats")
    roof = st.checkbox("Roof Rack")

# =====================
# BUILD INPUT
# =====================
if st.button("🚀 Predict Price"):

    car = {
        # numeric
        "age": age,
        "km_per_year": km_per_year,
        "hp_kW": hp_kW,
        "Weight_kg": weight,

        # counts
        "Comfort_Convenience_count": comfort_count,
        "Entertainment_Media_count": entertainment_count,
        "Extras_count": extras_count,
        "Safety_Security_count": safety_count,

        # OPTIONAL detailed (auto map to dummy)
        "Comfort_Convenience_Air conditioning": int(aircon),
        "Comfort_Convenience_Cruise control": int(cruise),
        "Comfort_Convenience_Parking assist system sensors rear": int(parking),

        "Entertainment_Media_Bluetooth": int(bluetooth),
        "Entertainment_Media_Radio": int(radio),
        "Entertainment_Media_USB": int(usb),

        "Safety_Security_ABS": int(abs),
        "Safety_Security_Driver-side airbag": int(airbags),

        "Extras_Sport seats": int(sport_seats),
        "Extras_Roof rack": int(roof),
    }

    price = predict_price(car)

    st.success(f"💰 Estimated Price: {price:,.0f} VND")