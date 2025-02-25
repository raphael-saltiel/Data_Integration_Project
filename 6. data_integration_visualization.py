# to run this program you should run in the terminal 'streamlit run .\data_integration.py'

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
def load_data():
    df = pd.read_csv("matrix.csv")
    df = df.iloc[1:].reset_index(drop=True)
    df["Total_Sales"] = pd.to_numeric(df["Total_Sales"], errors='coerce')
    df["Total_Profit"] = pd.to_numeric(df["Total_Profit"], errors='coerce')
    return df

df = load_data()

# Streamlit UI
st.title("K-Means Clustering on Sales and Profit Data")

# Scatter plot of Total Sales vs Total Profit
st.subheader("Scatter Plot of Total Sales vs Total Profit")
fig, ax = plt.subplots()
ax.scatter(df["Total_Sales"], df["Total_Profit"], alpha=0.7)
ax.set_xlabel("Total Sales")
ax.set_ylabel("Total Profit")
ax.set_title("Total Sales vs Total Profit")
ax.grid(True)
st.pyplot(fig)

# Select number of clusters
st.subheader("K-Means Clustering")
k = st.slider("Select number of clusters (K)", min_value=2, max_value=10, value=3)

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(df[["Total_Sales", "Total_Profit"]])

# Scatter plot with clusters
fig, ax = plt.subplots()
scatter = ax.scatter(df["Total_Sales"], df["Total_Profit"], c=df["Cluster"], cmap="viridis", alpha=0.7)
ax.set_xlabel("Total Sales")
ax.set_ylabel("Total Profit")
ax.set_title("K-Means Clustering of Total Sales vs Total Profit")
ax.grid(True)
plt.colorbar(scatter, label="Cluster")
st.pyplot(fig)

# Display clustered data
st.subheader("Clustered Data")
st.dataframe(df)
