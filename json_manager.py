import json, pandas as pd
from pathlib import Path

FILEPATH = "expenses.json"

def read_json():
    json_data = None
    if Path(FILEPATH).exists():
        with open(FILEPATH, "r", encoding="utf-8") as f:
            json_data = json.load(f)
    
    return json_data

def write_json(data): # Something was modified (add, delete, update).
    if data:
        if not Path(FILEPATH).exists(): # File doesn't exist, so It will be created
            print("No expenses file found. Creating expenses file...")

        # Something was modified in the Json data (add, delete, update), time to rewrite it.
        # The Data was already sent with the planned Json Schema.
        with open(FILEPATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    else:
        print("No data was sent.")

def to_csv(json_data):
    df = pd.DataFrame.from_dict(json_data, orient="index")
    df.to_csv("expenses.csv", index=False, encoding="utf-8")

    