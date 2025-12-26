from pathlib import Path

#===paths===
ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT/"data"
RAW = DATA/"raw"
PROCESSED = DATA/"processed"
DATA_FILE = RAW/"Housing.csv"

#===data split===
TRAINING_SIZE = 0.6
VALIDATION_SIZE = 0.2
TEST_SIZE = 0.2
RANDOM_STATE = 42

#===data information===
TARGET_COL = "price"
