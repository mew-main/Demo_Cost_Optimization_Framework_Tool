import pandas as pd

def suggest_ai_upgrades(df: pd.DataFrame) -> pd.DataFrame:
    """
    # Future: Add AI-powered suggestions here.
    For now, returns features with high AI opportunity (ai_opportunity >= 4) if present.
    """
    if "ai_opportunity" in df.columns:
        return df[df["ai_opportunity"] >= 4][["feature_name", "ai_opportunity"]].reset_index(drop=True)
    else:
        return pd.DataFrame([]) 