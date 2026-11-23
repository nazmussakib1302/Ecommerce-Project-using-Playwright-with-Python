import json

from config.config import TEST_DATA_DIR


def load_test_data(file_name: str) -> dict:
    with open(TEST_DATA_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)
