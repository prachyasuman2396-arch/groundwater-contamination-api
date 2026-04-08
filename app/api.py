from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import pandas as pd
from pathlib import Path

app = FastAPI(
    title="Groundwater Contamination Risk API",
    description="Predict groundwater risk level and top contaminants for villages",
    version="1.0.0"
)

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
        "contaminant_3"
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
        "villages_loaded": len(df)
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

        response = {
            "status": "success",
            "data": {
                "village": row["VILLAGE"],
                "risk_level": row["risk_level"],
                "cluster": int(row["cluster"]),
                "top_contaminants": [
                    row["contaminant_1"],
                    row["contaminant_2"],
                    row["contaminant_3"]
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