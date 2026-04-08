# src/clustering.py

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import numpy as np


def run_clustering(X):

    # force 3 clusters
    model = AgglomerativeClustering(
        n_clusters=3,
        linkage='ward'
    )

    labels = model.fit_predict(X)

    score = silhouette_score(X, labels)

    print("Silhouette Score:", round(score, 4))

    return labels, score


def label_risk_levels(df, labels):

    df = df.copy()

    df['cluster'] = labels

    cluster_risk = df.groupby('cluster')['risk_score'].mean()

    sorted_clusters = cluster_risk.sort_values().index

    mapping = {
        sorted_clusters[0]: "Low Risk",
        sorted_clusters[1]: "Medium Risk",
        sorted_clusters[2]: "High Risk"
    }

    df['risk_level'] = df['cluster'].map(mapping)

    return df