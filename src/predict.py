# import pandas as pd


# def predict_village(df, village_name):

#     row = df[df['VILLAGE'] == village_name]

#     if len(row) == 0:
#         print("Village not found")
#         print(df['VILLAGE'].head(20).tolist())
#         return

#     row = row.iloc[0]

#     print("\nVillage:", village_name)
#     print("Risk Level:", row['risk_level'])
#     print("Cluster:", row['cluster'])

#     print("\nTop 3 Contaminants:")
#     print("1.", row['contaminant_1'])
#     print("2.", row['contaminant_2'])
#     print("3.", row['contaminant_3'])


#     print("\nPossible Diseases:")
#     print("1.", row['disease_1'])
#     print("2.", row['disease_2'])
#     print("3.", row['disease_3'])
#     print("=" * 40)


import pandas as pd


CONTAMINANT_REASON = {
    "NO3": "Agricultural fertilizer runoff / sewage contamination",
    "F": "Fluoride rich geological formation",
    "Cl": "Salinity intrusion / wastewater mixing",
    "SO4": "Industrial discharge / mineral dissolution",
    "TH": "Hardness due to calcium & magnesium rocks",
    "Ca": "Limestone weathering",
    "Mg": "Dolomite dissolution",
    "Na": "Irrigation return flow / salinity",
    "Fe": "Iron rich soil leaching"
}


def predict_village(df, village_name):

    row = df[df['VILLAGE'] == village_name]

    if len(row) == 0:
        print("Village not found")
        print("Available villages:")
        print(df['VILLAGE'].head(20).tolist())
        return

    row = row.iloc[0]

    print("\n==============================")
    print("Village:", village_name)
    print("Risk Level:", row['risk_level'])
    print("Cluster:", row['cluster'])

    print("\nTop 3 Contaminants:")

    c1 = row['contaminant_1']
    c2 = row['contaminant_2']
    c3 = row['contaminant_3']

    print("1.", c1, "-", CONTAMINANT_REASON.get(c1, "Unknown reason"))
    print("2.", c2, "-", CONTAMINANT_REASON.get(c2, "Unknown reason"))
    print("3.", c3, "-", CONTAMINANT_REASON.get(c3, "Unknown reason"))

    print("\nPossible Diseases:")
    print("1.", row['disease_1'])
    print("2.", row['disease_2'])
    print("3.", row['disease_3'])

    print("==============================")