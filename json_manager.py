import json, pandas as pd
from pathlib import Path

FILEPATH = "expenses.json"

def write_json(data):
    with open(FILEPATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def file_reader(data): # If there's data, something was modified (add, delete, update).
    # Otherwise, it is just reading.

    if not Path(FILEPATH).exists(): # File doesn't exist...
        if data: # But an expense is going to be added. The file will be created.
            print("There were no expenses. Creating expenses file...")
            write_json(data)
            print("Expenses file created successfully.")

    else: # File exist, so it's necessary read it first.
        with open(FILEPATH, "r", encoding="utf-8") as f:
            json_data = json.load(f)

    if not data: # Only reading, nothing was modified (add, update, delete)
        return json_data

    # Otherwise, something WAS modified, time to rewrite it. The Data was already sent with the planned Json Schema.
    json_data = data
    write_json(json_data)
    return None

# Pending
def to_csv():
    json_data = file_reader(None)

    if json_data["data"]:
        df = pd.DataFrame(json_data["data"])
        df.to_csv("expenses.csv", index=False, encoding="utf-8")
    else:
        print("There is no expenses or expenses file doesn't exist...")

    