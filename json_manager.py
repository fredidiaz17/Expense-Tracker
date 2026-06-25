import json, pandas as pd
from pathlib import Path

FILEPATH = "expenses.json"

def write_json(data):
    with open(FILEPATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def file_reader(data): # SI hay data, se va a agregar algo. De lo contrario, solo se va a leer.

    if not Path(FILEPATH).exists():
        if data: # No existe archivo, pero se va a agregar un gasto. Se crea el archivo.
            print("Creating expenses file...")
            write_json(data)
            print("Expenses file created successfully.")
        # No existe archivo y no se va a agregar un gasto. Nada que hacer
    else:# Existe el archivo
        with open(FILEPATH, "r", encoding="utf-8") as f:
            json_data = json.load(f)

    if not data: # Leer solo
        return json_data

    json_data.append(data)
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

    