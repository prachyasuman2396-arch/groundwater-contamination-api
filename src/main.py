import pandas as pd

from src.feature_engineering import engineer_features
from src.scaler import scale_features
from src.clustering import run_clustering, label_risk_levels
from src.ranking import add_top3
from src.predict import predict_village


# ----------------------------------------
# Load dataset
# ----------------------------------------
df = pd.read_excel("data/CONTAMINANT.xlsx")

# IMPORTANT FIX
df.rename(columns={
    'Ca++': 'Ca',
    'Mg++': 'Mg',
    'Cl-': 'Cl',
    'F-': 'F'
}, inplace=True)


# ----------------------------------------
# Feature engineering
# ----------------------------------------
df_features = engineer_features(df)


# ----------------------------------------
# Scale
# ----------------------------------------
X_scaled, scaler = scale_features(df_features)


# ----------------------------------------
# Clustering
# ----------------------------------------
labels, score = run_clustering(X_scaled)


# ----------------------------------------
# Label clusters
# ----------------------------------------
df_clustered = label_risk_levels(df_features, labels)


# ----------------------------------------
# Merge
# ----------------------------------------
df_final = df.copy()

df_final['cluster'] = df_clustered['cluster']
df_final['risk_level'] = df_clustered['risk_level']


# ----------------------------------------
# Top 3 contaminants
# ----------------------------------------
df_final = add_top3(df_final)


print("\nSilhouette Score:", score)

print("\nCluster Counts:")
print(df_final['risk_level'].value_counts())


# ----------------------------------------
# Predict
# ----------------------------------------
df_final.to_csv("models/final_dataset.csv", index=False)

print("Saved final dataset -> models/final_dataset.csv")
while True:

    village = input("\nEnter village name (or exit): ")

    if village.lower() == "exit":
        break

    predict_village(df_final, village)

