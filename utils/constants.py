# utils/constants.py

# 💰 Budget Types
BUDGET_TYPES = ["Low", "Medium", "Luxury"]

# 🎯 User Interests
INTERESTS = ["Adventure", "Food", "Nature", "History"]

# 💸 Cost Constants (per day)
TRAVEL_COST_PER_DAY = 2000
FOOD_COST_PER_DAY = 500

# 🎯 Activity Cost by Budget
ACTIVITY_COST = {
    "Low": 300,
    "Medium": 800,
    "Luxury": 1500
}

# 📅 Default App Settings
MAX_DAYS = 10
MIN_DAYS = 1

# 🌍 Default Destination (fallback)
DEFAULT_DESTINATION = "Goa"

# 📁 File Paths
DATA_PATH = "data/destinations.json"

# 🎨 UI Text (optional centralization)
APP_TITLE = "🌍 AI Travel Planner"
APP_SUBTITLE = "Plan smarter with customized itineraries & budgets"