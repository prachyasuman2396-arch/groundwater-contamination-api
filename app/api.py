# from fastapi import FastAPI, HTTPException, Query
# from fastapi.responses import JSONResponse
# import pandas as pd
# from pathlib import Path

# app = FastAPI(
#     title="Groundwater Contamination Risk API",
#     description="Predict groundwater risk level, contaminants and diseases",
#     version="2.0.0"
# )

# # -----------------------------
# # Load dataset safely
# # -----------------------------
# BASE_DIR = Path(__file__).resolve().parent.parent
# DATA_PATH = BASE_DIR / "models" / "final_dataset.csv"

# try:
#     df = pd.read_csv(DATA_PATH)

#     REQUIRED_COLUMNS = [
#         "VILLAGE",
#         "risk_level",
#         "cluster",
#         "contaminant_1",
#         "contaminant_2",
#         "contaminant_3",
#         "disease_1",
#         "disease_2",
#         "disease_3"
#     ]

#     missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

#     if missing:
#         raise ValueError(f"Missing columns: {missing}")

# except FileNotFoundError:
#     raise RuntimeError("final_dataset.csv not found in models/")
# except Exception as e:
#     raise RuntimeError(f"Dataset loading failed: {str(e)}")


# # -----------------------------
# # Health endpoint
# # -----------------------------
# @app.get("/")
# def health():
#     return {
#         "status": "running",
#         "service": "groundwater-risk-api",
#         "villages_loaded": len(df),
#         "version": "2.0 (with disease prediction)"
#     }


# # -----------------------------
# # Example villages
# # -----------------------------
# @app.get("/examples")
# def examples():
#     return {
#         "example_villages": df["VILLAGE"].head(10).tolist()
#     }


# # -----------------------------
# # Predict endpoint
# # -----------------------------
# @app.get("/predict")
# def predict(
#     village: str = Query(..., description="Village name")
# ):
#     try:

#         if not village or village.strip() == "":
#             raise HTTPException(
#                 status_code=400,
#                 detail="Village name cannot be empty"
#             )

#         row = df[df["VILLAGE"].str.lower() == village.lower()]

#         if len(row) == 0:
#             return JSONResponse(
#                 status_code=404,
#                 content={
#                     "error": "Village not found",
#                     "village": village,
#                     "examples": df["VILLAGE"].head(5).tolist()
#                 }
#             )

#         row = row.iloc[0]

#         response = {
#             "status": "success",
#             "data": {
#                 "village": row["VILLAGE"],
#                 "risk_level": row["risk_level"],
#                 "cluster": int(row["cluster"]),

#                 "top_contaminants": [
#                     row["contaminant_1"],
#                     row["contaminant_2"],
#                     row["contaminant_3"]
#                 ],

#                 "possible_diseases": [
#                     row["disease_1"],
#                     row["disease_2"],
#                     row["disease_3"]
#                 ]
#             }
#         }

#         return response

#     except HTTPException:
#         raise

#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={
#                 "status": "error",
#                 "message": "Prediction failed",
#                 "details": str(e)
#             }
#         )


from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import pandas as pd
from pathlib import Path

app = FastAPI(
    title="Groundwater Contamination Risk API",
    description="Predict groundwater risk level, contaminants and diseases",
    version="3.0.0"
)

# -----------------------------
# Contaminant reason mapping
# -----------------------------
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

# -----------------------------
# Load dataset safely
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "models" / "final_dataset.csv"

try:
    df = pd.read_csv(DATA_PATH)

    REQUIRED_COLUMNS = [
        "VILLAGE",
        "risk_level",
        "cluster",
        "contaminant_1",
        "contaminant_2",
        "contaminant_3",
        "disease_1",
        "disease_2",
        "disease_3"
    ]

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

except FileNotFoundError:
    raise RuntimeError("final_dataset.csv not found in models/")
except Exception as e:
    raise RuntimeError(f"Dataset loading failed: {str(e)}")


# -----------------------------
# Health endpoint
# -----------------------------
@app.get("/")
def health():
    return {
        "status": "running",
        "service": "groundwater-risk-api",
        "villages_loaded": len(df),
        "version": "3.0 (with contamination reasons)"
    }


# -----------------------------
# Example villages
# -----------------------------
@app.get("/examples")
def examples():
    return {
        "example_villages": df["VILLAGE"].head(10).tolist()
    }


# -----------------------------
# Predict endpoint
# -----------------------------
@app.get("/predict")
def predict(
    village: str = Query(..., description="Village name")
):
    try:

        if not village or village.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="Village name cannot be empty"
            )

        row = df[df["VILLAGE"].str.lower() == village.lower()]

        if len(row) == 0:
            return JSONResponse(
                status_code=404,
                content={
                    "error": "Village not found",
                    "village": village,
                    "examples": df["VILLAGE"].head(5).tolist()
                }
            )

        row = row.iloc[0]

        c1 = row["contaminant_1"]
        c2 = row["contaminant_2"]
        c3 = row["contaminant_3"]

        response = {
            "status": "success",
            "data": {
                "village": row["VILLAGE"],
                "risk_level": row["risk_level"],
                "cluster": int(row["cluster"]),

                "top_contaminants": [
                    {
                        "name": c1,
                        "reason": CONTAMINANT_REASON.get(c1, "Unknown")
                    },
                    {
                        "name": c2,
                        "reason": CONTAMINANT_REASON.get(c2, "Unknown")
                    },
                    {
                        "name": c3,
                        "reason": CONTAMINANT_REASON.get(c3, "Unknown")
                    }
                ],

                "possible_diseases": [
                    row["disease_1"],
                    row["disease_2"],
                    row["disease_3"]
                ]
            }
        }

        return response

    except HTTPException:
        raise

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Prediction failed",
                "details": str(e)
            }
        )