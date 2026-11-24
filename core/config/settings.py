from pathlib import Path

# Project directories
ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REFERENCE_DIR = DATA_DIR / "reference"

# Default project
PROJECT_NAME = "Silverlinjen"
MODEL_NAME = "Viadukten"

MODEL_DIR = RAW_DIR / "viadukten"
IFC_FILE = MODEL_DIR / "viadukten.ifc"

# Validation settings
VOLUME_TOLERANCE_M3 = 0.001

# Engineering categories
STRUCTURAL_CATEGORIES = (
    "Columns",
    "Foundations",
    "Beams",
    "Bridge Deck",
    "Walls",
)

# Revit CSV category mapping
CSV_CATEGORY_MAPPING = {
    "QTO - Floors": "Bridge Deck",
    "QTO - Structural Foundations": "Foundations",
    "QTO - Structural Framing": "Beams",
    "QTO - Walls": "Walls",
    "structural_columns": "Columns",
}