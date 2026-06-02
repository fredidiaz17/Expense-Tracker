import json_manager as jsm, pandas as pd
from datetime import date

def list():
    json_data = jsm.file_reader(None)
    data = None
    if json_data:
        data = pd.DataFrame(json_data["data"])

    if data:
        print(data)
    else:
        print("There is no expenses (expenses file doesn't exist). Try creating your first expense.")


def add(expense):
    json_data = jsm.file_reader(None)

    # Ultimo ID agregado (Last ID)
    if json_data: # Hay data
        id = json_data["l_ID"] + 1

    else: # No hay
        id = 1
        json_data["data"] = {"ID":[],"Date":[],"Description":[],"Amount":[]}

    json_data["l_ID"] = id
    json_data["Data"]["ID"].append(id)
    json_data["Data"]["Date"].append(date.today())
    json_data["Data"]["Description"].append(expense["Description"])
    json_data["Data"]["Amount"].append(expense["Amount"])

    jsm.file_reader(json_data)

def update(expense):
    pass

def summary():
    json_data = jsm.file_reader(None)

    if json_data:
        data = json_data["data"]
    else:
        print(print("There is no expenses or maybe expenses file doesn't exist. Try creating your first expense."))


def delete():
    pass