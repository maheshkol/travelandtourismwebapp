# pages/3_Budget.py

import streamlit as st
from utils.helpers import load_data
from modules.budget import calculate_budget, get_budget_breakdown

# 📂 Load data
data = load_data("data/destinations.json")

st.title("💰 Budget Planner")

st.write("Estimate your travel expenses based on destination and preferences.")

st.write("---")

# 🧾 User Inputs
destination = st.selectbox("📍 Select Destination", list(data.keys()))
days = st.slider("📅 Number of Days", 1, 10)
budget = st.selectbox("💼 Select Budget Type", ["Low", "Medium", "Luxury"])

st.write("---")

# 🚀 Calculate Budget
if st.button("Calculate Budget"):

    total_cost = calculate_budget(destination, days, budget, data)
    breakdown = get_budget_breakdown(destination, days, budget, data)

    # 💰 Total Cost
    st.header("💰 Total Estimated Cost")
    st.success(f"₹ {total_cost}")

    st.write("---")

    # 📊 Breakdown
    st.header("📊 Budget Breakdown")

    for key, value in breakdown.items():
        st.write(f"{key}: ₹{value}")

    st.write("---")

    # 💡 Budget Tips
    st.header("💡 Budget Tips")

    if budget == "Low":
        st.info("✔ Travel in off-season\n✔ Use public transport\n✔ Stay in budget hotels/hostels")

    elif budget == "Medium":
        st.info("✔ Book hotels in advance\n✔ Use cabs for convenience\n✔ Try popular attractions")

    else:
        st.info("✔ Choose premium stays\n✔ Book guided tours\n✔ Enjoy luxury experiences")