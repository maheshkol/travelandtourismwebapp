# pages/4_Recommendations.py

import streamlit as st
from utils.helpers import load_data
from modules.recomendations import get_recommendations, get_smart_recommendations

# 📂 Load data
data = load_data("data/destinations.json")

st.title("🎯 Travel Recommendations")

st.write("Get smart travel suggestions based on your interests and preferences.")

st.write("---")

# 🧾 User Inputs
destination = st.selectbox("📍 Select Destination", list(data.keys()))

days = st.slider("📅 Number of Days", 1, 10)

budget = st.selectbox("💰 Select Budget", ["Low", "Medium", "Luxury"])

interests = st.multiselect(
    "🎯 Select Interests",
    ["Adventure", "Food", "Nature", "History"]
)

st.write("---")

# 🚀 Generate Recommendations
if st.button("Get Recommendations"):

    # 🎯 Basic Recommendations
    recs = get_recommendations(destination, interests, budget, data)

    st.header("🎯 Personalized Recommendations")

    for r in recs:
        st.write(f"👉 {r}")

    st.write("---")

    # 🧠 Smart Recommendations
    smart_recs = get_smart_recommendations(destination, days, interests, budget, data)

    st.header("🧠 Smart Tips")

    for r in smart_recs:
        st.write(f"💡 {r}")