# modules/budget.py

def calculate_budget(destination, days, budget_type, data):
    """
    Calculate total trip cost based on:
    - destination
    - number of days
    - budget type (Low, Medium, Luxury)
    """

    # 🏨 Hotel cost per day
    hotel_per_day = data[destination]["hotel_cost"][budget_type]

    # 🚗 Travel cost (fixed per day estimate)
    travel_cost_per_day = 2000

    # 🍽 Food cost per day
    food_cost_per_day = 500

    # 🎯 Activity cost (can vary by budget)
    if budget_type == "Low":
        activity_cost_per_day = 300
    elif budget_type == "Medium":
        activity_cost_per_day = 800
    else:  # Luxury
        activity_cost_per_day = 1500

    # 💰 Total calculation
    total_cost = (
        (hotel_per_day * days) +
        (travel_cost_per_day * days) +
        (food_cost_per_day * days) +
        (activity_cost_per_day * days)
    )

    return total_cost


def get_budget_breakdown(destination, days, budget_type, data):
    """
    Returns detailed cost breakdown
    """

    hotel_per_day = data[destination]["hotel_cost"][budget_type]

    breakdown = {
        "Hotel": hotel_per_day * days,
        "Travel": 2000 * days,
        "Food": 500 * days,
    }

    if budget_type == "Low":
        breakdown["Activities"] = 300 * days
    elif budget_type == "Medium":
        breakdown["Activities"] = 800 * days
    else:
        breakdown["Activities"] = 1500 * days

    breakdown["Total"] = sum(breakdown.values())

    return breakdown