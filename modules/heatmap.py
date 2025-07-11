import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(df, st):
    """
    Plots a heatmap of infra_cost vs value_score for each feature.
    """
    # Prepare data for heatmap
    heatmap_data = df.set_index('feature_name')[['infra_cost', 'value_score']]
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.heatmap(heatmap_data, annot=True, ax=ax, cmap="YlGnBu")
    st.pyplot(fig) 