import pandas as pd
import numpy as np


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


# contaminant → disease mapping (with severity)
CONTAMINANT_DISEASE = {

    "NO3": [
        ("Methemoglobinemia", 1.5),
        ("Blue baby syndrome", 1.6),
        ("Thyroid problems", 1.2)
    ],

    "F": [
        ("Dental fluorosis", 1.2),
        ("Skeletal fluorosis", 1.6),
        ("Joint pain", 1.1)
    ],

    "Cl": [
        ("Hypertension", 1.1),
        ("Gastrointestinal irritation", 0.9)
    ],

    "SO4": [
        ("Diarrhea", 1.0),
        ("Dehydration", 1.1)
    ],

    "TH": [
        ("Kidney stones", 1.3),
        ("Gall stones", 1.0)
    ],

    "Ca": [
        ("Kidney stones", 1.0)
    ],

    "Mg": [
        ("Diarrhea", 0.9),
        ("Muscle weakness", 0.8)
    ],

    "Na": [
        ("Hypertension", 1.4),
        ("Heart disease", 1.3)
    ],

    "Fe": [
        ("Stomach upset", 0.6),
        ("Iron overload", 0.8)
    ]
}


def rank_diseases(row):

    disease_scores = {}

    for contaminant in SAFE_LIMITS.keys():

        value = row.get(contaminant, np.nan)

        if pd.isna(value):
            continue

        limit = SAFE_LIMITS[contaminant]
        weight = RISK_WEIGHTS[contaminant]

        contaminant_score = (value / limit) * weight

        diseases = CONTAMINANT_DISEASE.get(contaminant, [])

        for disease, severity in diseases:

            score = contaminant_score * severity

            if disease not in disease_scores:
                disease_scores[disease] = 0

            disease_scores[disease] += score

    ranked = sorted(
        disease_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top3 = [d[0] for d in ranked[:3]]

    while len(top3) < 3:
        top3.append("None")

    return top3


def add_top3_diseases(df):

    df = df.copy()

    top3 = df.apply(rank_diseases, axis=1)

    df['disease_1'] = top3.apply(lambda x: x[0])
    df['disease_2'] = top3.apply(lambda x: x[1])
    df['disease_3'] = top3.apply(lambda x: x[2])

    return df