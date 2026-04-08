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


def rank_contaminants(row):
    
    scores = {}
    
    for col in CONTAMINANTS:
        # use .get to avoid KeyError if column missing
        value = row.get(col, np.nan)
        limit = SAFE_LIMITS[col]

        # skip missing or NaN values
        if pd.isna(value):
            continue

        # compute ratio of value to safe limit and rank by this ratio
        # (include values even if below the limit so we can always show top contaminants)
        scores[col] = value / limit
    
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