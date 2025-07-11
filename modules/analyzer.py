import pandas as pd

def analyze_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate value_score and recommend action for each feature.
    Fills missing columns with default values for demo purposes.
    """
    df = df.copy()
    # Fill missing columns with default/mock values
    for col, default in [
        ("user_satisfaction_score", 0),
        ("avg_support_cost", 0),
        ("underutilization_penalty", 0)
    ]:
        if col not in df.columns:
            df[col] = default

    # Calculate support_cost for each feature
    df["support_cost"] = df["support_tickets"] * df["avg_support_cost"]

    # Calculate value_score using the provided formula
    df["value_score"] = (
        (df["usage_per_month"] * df["user_satisfaction_score"])
        / (df["infra_cost"] + df["support_cost"] + df["underutilization_penalty"])
    )

    # Recommend action based on value_score
    df["action"] = df["value_score"].apply(lambda x: "Retire" if x < 1 else "Keep/Improve")
    return df 