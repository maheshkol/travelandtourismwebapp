# modules/recommendations.py

def get_recommendations(destination, interests, budget_type, data):

    recommendations = []

    dest_data = data[destination]

    places = dest_data["places"]
    activities = dest_data["activities"]

    # 🎯 Interest-based filtering
    for interest in interests:

        if interest.lower() == "adventure":
            recommendations.append("Try adventure activities like trekking, paragliding, or water sports")

        elif interest.lower() == "food":
            recommendations.append("Explore local cuisine and famous food spots")

        elif interest.lower() == "nature":
            recommendations.append("Visit scenic spots, mountains, beaches, and parks")

        elif interest.lower() == "history":
            recommendations.append("Visit historical monuments and cultural landmarks")

    # 💰 Budget-based recommendations
    if budget_type == "Low":
        recommendations.append("Choose budget hotels or hostels")
        recommendations.append("Use public transport or rent a bike")
        recommendations.append("Prefer free or low-cost attractions")

    elif budget_type == "Medium":
        recommendations.append("Book comfortable hotels")
        recommendations.append("Use cabs or rental vehicles")
        recommendations.append("Try popular tourist attractions")

    else:
        recommendations.append("Stay in premium resorts")
        recommendations.append("Use private transport")
        recommendations.append("Enjoy exclusive experiences and guided tours")

    # ✅ FIXED HERE
    place_names = [p["name"] for p in places[:3]]

    recommendations.append(f"Top places to visit: {', '.join(place_names)}")
    recommendations.append(f"Popular activities: {', '.join(activities[:3])}")

    return recommendations


def get_smart_recommendations(destination, days, interests, budget_type, data):
    """
    Advanced recommendation system (future-ready)
    """

    recs = []

    # Longer trip suggestions
    if days >= 5:
        recs.append("Consider exploring nearby destinations for a complete experience")

    # Interest-based enhancement
    if "Adventure" in interests:
        recs.append("Plan at least one full day for adventure activities")

    if "Food" in interests:
        recs.append("Include local food tours in your itinerary")

    if "Nature" in interests:
        recs.append("Visit sunrise/sunset viewpoints")

    # Budget optimization tips
    if budget_type == "Low":
        recs.append("Travel in off-season to save more money")

    return recs