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
def no_data(data): # No data messages.
    if not data:
        print("Expenses file doesn't exist. Try adding the first expense.")
    else:
        print("There is no expenses. Try adding the first one.")

def list():
    json_data = jsm.read_json()

    if json_data and json_data["data"]:
        data = pd.DataFrame.from_dict(json_data["data"])
        print(data)
    else:
        no_data(json_data)


def add(expense):
    json_data = jsm.read_json()
    # Last added ID (l_ID)
    if json_data: # Data exist
        id = json_data["l_ID"] + 1

    else: # No data
        id = 1
    json_data["l_ID"] = id

    id = str(id)

    data = {
        "Date": str(date.today()),
        "Description": expense["Description"],
        "Amount": expense["Amount"],
    }

    json_data["data"]["id"] = data
    jsm.write_json(json_data)
    print(f"Expense added successfully (ID: {id})")

def update(expense):
    json_data = jsm.read_json()

    if json_data and json_data["data"]:  # Both file and expenses (data) exist

        id = str(expense["ID"])

        if id in json_data["data"]:
            data = json_data["data"][id]
            data["Date"] = str(date.today())
            if expense["Description"]:
                data["Description"] = expense["Description"]
            if expense["Amount"]:
                json_data["data"][id]["Amount"] = expense["Amount"]

            jsm.write_json(json_data)
            print(f"Expense with ID {id} has been successfully updated.")
        else:
            if not json_data:
                print("Expense file doesn't exist. Try adding the first one.")
            else:
                print(f"There is no expense identified by id: {id}")
    else:
        no_data(json_data)

def summary(month_num = None):
    json_data = jsm.read_json()

    if json_data and json_data["data"]:
        df = pd.DataFrame.from_dict(json_data["data"])
        if not month_num:
            print(f"Total expenses: {df["Amoun"].sum()}")
        else:
            df["Date"] = pd.to_datetime(df["Date"])

            if df["Date"].dt.month == month_num:
                print(f"Total expenses for {months[month_num]}: {df.groupby(month_num)["Amount"].sum()}")

    else:
        no_data(json_data)

def delete(id):
    json_data = jsm.read_json()

    if json_data and json_data["data"]: # Both file and data exists
        id = str(id)
        if id in json_data["data"]:
            del json_data["data"][id]

            print(f"Expense deleted successfully")
            jsm.write_json(json_data)
        else:
            if not json_data:
                print(f"Expenses file doesn't exist. Try adding the first one.")
            else:
                print(f"There is no expense identified by id: {id}")
    else:
        no_data(json_data)