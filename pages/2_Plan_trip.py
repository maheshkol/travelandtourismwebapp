# pages/2_Plan_Trip.py

import streamlit as st
from utils.helpers import load_data
from modules.itinerary import generate_detailed_itinerary
from modules.budget import calculate_budget, get_budget_breakdown
from modules.recomendations import get_recommendations

# 📂 Load data
data = load_data("data/destinations.json")

st.title("✈️ Plan Your Trip")

st.write("Customize your travel plan based on your preferences.")

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

# 🚀 Generate Plan Button
if st.button("Generate Travel Plan"):

    # 📅 Itinerary
    itinerary = generate_detailed_itinerary(destination, days, data)

    st.header("📅 Your Itinerary")

    for day in itinerary:
        st.subheader(f"Day {day['day']}")
        st.write(f"🌅 Morning: {day['morning']}")
        st.write(f"🌞 Afternoon: {day['afternoon']}")
        st.write(f"🌙 Evening: {day['evening']}")
        st.write("---")

    # 💰 Budget
    total_cost = calculate_budget(destination, days, budget, data)
    breakdown = get_budget_breakdown(destination, days, budget, data)

    st.header("💰 Budget Details")
    st.success(f"Total Estimated Cost: ₹ {total_cost}")

    st.subheader("📊 Breakdown")
    for key, value in breakdown.items():
        st.write(f"{key}: ₹{value}")

    st.write("---")

    # 🎯 Recommendations
    recs = get_recommendations(destination, interests, budget, data)

    st.header("🎯 Recommendations")

    for r in recs:
        st.write(f"👉 {r}")