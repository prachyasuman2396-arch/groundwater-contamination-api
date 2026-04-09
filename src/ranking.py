import pandas as pd
import numpy as np


CONTAMINANTS = [
    'NO3',
    'F',
    'Cl',
    'SO4',
    'TH',
    'Ca',
    'Mg',
    'Na',
    'Fe'
]


SAFE_LIMITS = {
    'NO3': 45,
    'F': 1.5,
    'Cl': 250,
    'SO4': 200,
    'TH': 200,
    'Ca': 75,
    'Mg': 30,
    'Na': 200,
    'Fe': 0.3
}


RISK_WEIGHTS = {
    'NO3': 1.3,
    'F': 1.4,
    'Cl': 0.6,
    'SO4': 0.7,
    'TH': 0.8,
    'Ca': 0.5,
    'Mg': 0.6,
    'Na': 1.0,
    'Fe': 0.4
}


def rank_contaminants(row):

    scores = {}

    for col in CONTAMINANTS:

        value = row.get(col, np.nan)
        limit = SAFE_LIMITS[col]
        weight = RISK_WEIGHTS[col]

        if pd.isna(value):
            continue

        score = (value / limit) * weight
        scores[col] = score

    if len(scores) == 0:
        return ["None", "None", "None"]

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top3 = [r[0] for r in ranked[:3]]

    while len(top3) < 3:
        top3.append("None")

    return top3


def add_top3(df):

    df = df.copy()

    top3 = df.apply(rank_contaminants, axis=1)

    df['contaminant_1'] = top3.apply(lambda x: x[0])
    df['contaminant_2'] = top3.apply(lambda x: x[1])
    df['contaminant_3'] = top3.apply(lambda x: x[2])

    return df