import pandas as pd


def predict_village(df, village_name):

    row = df[df['VILLAGE'] == village_name]

    if len(row) == 0:
        print("Village not found")
        print(df['VILLAGE'].head(20).tolist())
        return

    row = row.iloc[0]

    print("\nVillage:", village_name)
    print("Risk Level:", row['risk_level'])
    print("Cluster:", row['cluster'])

    print("\nTop 3 Contaminants:")
    print("1.", row['contaminant_1'])
    print("2.", row['contaminant_2'])
    print("3.", row['contaminant_3'])

    print("=" * 40)