import json_manager as jsm, pandas as pd
from datetime import date

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def list():
    json_data = jsm.file_reader(None)
    data = None
    if json_data:
        data = pd.DataFrame(json_data["data"])

    if data:
        print(data)
    else:
        print("There is no expenses or the file doesn't exist. Try adding the first one.")


def add(expense):
    json_data = jsm.file_reader(None)

    # Ultimo ID agregado (Last ID)
    if json_data: # Hay data
        id = json_data["l_ID"] + 1

    else: # No hay
        id = 1
        json_data["data"] = {"ID":[],"Date":[],"Description":[],"Amount":[]}

    json_data["l_ID"] = id
    json_data["data"]["ID"].append(id)
    json_data["data"]["Date"].append(str(date.today()))
    json_data["data"]["Description"].append(expense["Description"])
    json_data["data"]["Amount"].append(expense["Amount"])

    jsm.file_reader(json_data)
    print(f"Expense added successfully (ID: {id})")

def update(expense):
    json_data = jsm.file_reader(None)
    id = expense("ID")
    if json_data and json_data["data"]:  # Hay archivo, y hay datos
        if id in json_data["data"]["ID"]:
            loc = json_data["data"]["ID"].index(id)

            json_data["data"]["Date"][loc] = str(date.today())
            json_data["data"]["Description"][loc] = expense["Description"]
            json_data["data"]["Amount"][loc] = expense["Amount"]

            jsm.file_reader(json_data)
            print(f"Expense with ID {id} has been successfully updated.")
        else:
            print(f"There is no expense identified by i: {id}")
    else:
        print("There is no expenses or expenses file doesn't exist. Try adding the first one.")

def summary(month_num = None):
    json_data = jsm.file_reader(None)

    if json_data:

        df = pd.dataframe(json_data["data"])

        if month_num:

            df["Date"] = pd.to_datetime(df["Date"])

            if df["Date"].dt.month == month_num:
                print(f"Total expenses for {months[month_num]}: {df.groupby(month_num)["Amount"].sum()}")
        else:
            print(f"Total expenses: {df["Amoun"].sum()}")

    else:
        print("There is no expenses or maybe expenses file doesn't exist. Try creating the first one.")

def delete(id):
    json_data = jsm.file_reader(None)

    if json_data and json_data["data"]: # Hay archivo, y hay datos
        if id in json_data["data"]["ID"]:
            loc = json_data["data"]["ID"].index(id)

            del json_data["data"]["ID"][loc]
            del json_data["data"]["Date"][loc]
            del json_data["data"]["Description"][loc]
            del json_data["data"]["Amount"][loc]

            print(f"Expense deleted successfully")
            jsm.file_reader(json_data)
        else:
            print(f"There is no expense identified by id: {id}")
    else:
        print("There is no expenses or expenses file doesn't exist. Try adding the first one.")