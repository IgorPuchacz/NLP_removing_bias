from pathlib import Path

DATA_DIR      = Path("../data")
RAW_DIR       = DATA_DIR/"raw"
PROCESSED_DIR = DATA_DIR/"processed"
MODEL_DIR     = Path("../models")
RESULTS_DIR   = Path("../results")
MODELS = [
    "distilbert-base-uncased",
    "albert-base-v2",
    "roberta-base"
]
