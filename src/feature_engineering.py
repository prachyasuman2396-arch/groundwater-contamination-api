
import pandas as pd


def engineer_features(df: pd.DataFrame):

    df= df.copy()
    df.rename(columns = {'Ca++':'Ca','Mg++':'Mg','Cl-':'Cl','SO4':'SO4','NO3':'NO3','F-':'F'},inplace = True)


    
    df['total_mineral_load'] = (
        df['Ca'] + df['Mg'] + df['Cl'] +
        df['SO4'] + df['NO3'] + df['F'] + df['TDS']
    )

    
    df['violation_count'] = df[
        ['ACTUAL_Ca','ACTUAL_Mg','ACTUAL_NO3',
         'ACTUAL_F','ACTUAL_Cl','ACTUAL_SO4','ACTUAL_TDS']
    ].sum(axis=1)

    
    df['max_contaminant'] = df[
        ['Ca','Mg','NO3','F','Cl','SO4','TDS']
    ].max(axis=1)

    
    df['mean_contaminant'] = df[
        ['Ca','Mg','NO3','F','Cl','SO4','TDS']
    ].mean(axis=1)

    
    limits = {
        'NO3': 45,
        'F': 1.5,
        'Cl': 250,
        'SO4': 200,
        'TDS': 500,
        'Mg': 30,
        'Ca': 75
    }

    
    for col, limit in limits.items():
        df[f'{col}_exceed'] = df[col] / limit

    exceed_cols = [f'{c}_exceed' for c in limits.keys()]

    
    df['contamination_count'] = (df[exceed_cols] > 1).sum(axis=1)

    
    df['max_risk'] = df[exceed_cols].max(axis=1)

    
    df['risk_score'] = (
        df['NO3'] * 0.25 +
        df['F']   * 0.25 +
        df['TDS'] * 0.15 +
        df['Cl']  * 0.10 +
        df['SO4'] * 0.10 +
        df['Mg']  * 0.075 +
        df['Ca']  * 0.075
    )
    CLUSTER_FEATURES = [
    'risk_score',
    'violation_count',
    'max_contaminant',
    'total_mineral_load',
    'RASTERVALU',
    'pH',
    'contamination_count',
    'max_risk'
    ]
    return df[CLUSTER_FEATURES]

if __name__ == '__main__':

    df = pd.read_excel(
        '/Users/prachyasumandas/Documents/ground_water_contamination/data/CONTAMINANT.xlsx'
    )
        # df.rename(columns = {'Ca++':'Ca','Mg++':'Mg','Cl-':'Cl','SO4':'SO4','NO3':'NO3','F-':'F'},inplace = True)
    df = engineer_features(df)
    # print(df.head())
    print(df.columns)


