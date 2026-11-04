from pathlib import Path
import pandas as pd
from fastapi import FastAPI, HTTPException

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "zoo_visitors.csv"

DATASET_URL = "https://data.go.th/dataset/zoo-visitors2569"
RESOURCE_ID = "0ecc96cf-d914-42a1-b184-dbbd013c3c9c"

app = FastAPI(
    title="Zoo Visitors API",
    description="RESTful API for Thailand Zoo visitor statistics, fiscal year 2569",
    version="1.0.0",
)

def load_real_data():
    """Read the actual CSV downloaded from the assigned Data.go.th resource."""
    if not DATA_FILE.exists():
        raise HTTPException(
            status_code=503,
            detail=(
                "ยังไม่พบไฟล์ข้อมูลจริง กรุณาดาวน์โหลด CSV จาก Data.go.th "
                "แล้วบันทึกเป็น data/zoo_visitors.csv"
            ),
        )

    try:
        try:
            df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
        except UnicodeDecodeError:
            df = pd.read_csv(DATA_FILE, encoding="cp874")

        # Replace pandas NaN values with JSON-compatible null values.
        df = df.astype(object).where(pd.notna(df), None)
        records = df.to_dict(orient="records")
        if not records:
            raise HTTPException(status_code=503, detail="ไฟล์ CSV ไม่มีรายการข้อมูล")
        return records
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"อ่านไฟล์ CSV ไม่สำเร็จ: {str(exc)}",
        )

@app.get("/")
def home():
    return {
        "message": "Zoo Visitors API is running",
        "api": "/api/zoo-visitors",
        "docs": "/docs",
    }

@app.get("/api/zoo-visitors")
def get_zoo_visitors():
    records = load_real_data()
    return {
        "dataset": "ข้อมูลรายงานสถิติจำนวนผู้เข้าชมสวนสัตว์",
        "organization": "องค์การสวนสัตว์แห่งประเทศไทย ในพระบรมราชูปถัมภ์",
        "fiscal_year": 2569,
        "source": DATASET_URL,
        "resource_id": RESOURCE_ID,
        "data_file": "data/zoo_visitors.csv",
        "record_count": len(records),
        "data": records,
    }
