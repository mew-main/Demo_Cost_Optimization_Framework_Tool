import streamlit as st
import pandas as pd
from modules.analyzer import analyze_features
from modules.ai_layer import suggest_ai_upgrades

st.title("Legacy SaaS Cost Optimization Tool")

# Try to load the data, show a helpful error if not found
try:
    data = pd.read_csv("data/legacy_features.csv")
except FileNotFoundError:
    st.error("Mock data not found. Please add 'data/legacy_features.csv'.")
    st.stop()

# Check for required columns and show a helpful error if missing
required_columns = [
    "feature_name", "theme", "usage_per_month", "user_satisfaction_score",
    "infra_cost", "support_tickets", "avg_support_cost", "underutilization_penalty"
]
missing_cols = [col for col in required_columns if col not in data.columns]
if missing_cols:
    st.error(f"Missing columns in CSV: {', '.join(missing_cols)}. Please update your data file.")
    st.stop()

# Show the loaded data
st.dataframe(data)

# When the user clicks the button, run the analysis
if st.button("Run Analysis"):
    # Analyze features using the value_score formula
    result = analyze_features(data)
    st.dataframe(result)

    # Show features with high AI opportunity (future expansion)
    ai_suggestions = suggest_ai_upgrades(result)
    st.subheader("AI Opportunity Layer")
    st.write(ai_suggestions)

    # Optional: Show a heatmap of infra_cost vs value_score
    try:
        from modules.heatmap import plot_heatmap
        st.subheader("Cost vs Value Heatmap")
        plot_heatmap(result, st)
    except ImportError:
        st.info("Install seaborn and matplotlib to see the heatmap.") 