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

def list(category = None):
    json_data = jsm.read_json("data")

    if json_data:
        df = pd.DataFrame.from_dict(json_data, orient="index")
        df.index.name = "ID"
        df["Amount"] = "$" + df["Amount"].astype(str)
        if category:
            category = category.replace("_", " ").capitalize()
            df = df[df["Category"] == category]
        if not df.empty:
            print(df.reset_index().to_string(index=False))
        else:
            print(f"No expenses found for {category}")
    else:
        print("No expenses found.")


def add(expense):
    json_data = jsm.read_json()
    # Last added ID (l_ID)
    if json_data: # Data exist
        id = json_data["l_ID"] + 1

    else: # No data
        id = 1
        json_data = {"l_ID": id, "data": {}}

    category = "No Category"

    if "Category" in expense:
        category = expense["Category"].replace("_", " ").capitalize()

    json_data["l_ID"] = id

    id = str(id)

    data = {
        "Date": str(date.today()),
        "Description": expense["Description"].replace("_", " "),
        "Amount": expense["Amount"],
        "Category": category
    }

    json_data["data"][id] = data
    jsm.write_json(json_data)
    print(f"Expense added successfully (ID: {id})")


def update(expense):
    json_data = jsm.read_json()

    if json_data and json_data["data"]:  # Both file and expenses (data) exist

        id = str(expense["ID"])

        if id in json_data["data"]:
            data = json_data["data"][id]
            data["Date"] = str(date.today())
            if "Description" in expense:
                data["Description"] = expense["Description"].replace("_", " ")
            if "Amount" in expense:
                json_data["data"][id]["Amount"] = expense["Amount"]
            if "Category" in expense:
                json_data["data"][id]["Category"] = expense["Category"].replace("_", " ").capitalize()

            jsm.write_json(json_data)
            print(f"Expense with ID {id} has been successfully updated.")
        else:
            print(f"There is no expense identified by id: {id}")
    else:
        no_data(json_data)


def summary(data):
    json_data = jsm.read_json("data")

    if json_data:
        month_num = category = None

        if "Month" in data:
            month_num = data["Month"]
        if "Category" in data:
            category = data["Category"].replace("_", " ").capitalize()

        filtered = []
        for data in json_data["data"].values():
            if month_num:
                current_year = str(date.today().year)
                if not (int(data["Date"][5:7]) == month_num and data["Date"][:4] == current_year):
                    continue
            if category:
                if data["Category"] != category: # the category from the data has the same style as the searching category
                    continue
            filtered.append(data)

        total = sum(item["Amount"] for item in filtered)
        if total > 0:
            print("Total expenses", end="")
            if month_num:
                print(f" for {months[month_num]}", end="")
            if category:
                print(f" with category '{category}'", end="")
            print(f": ${total}")
        else:
            print(f"There are no expenses", end=" ")
            if month_num:
                print(f" for {months[month_num]} of the current year", end="")
            if category:
                print(f" with category '{category}'")
    else:
        print("No expenses to summarize.")


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

def csv_export():
    # This probably can be changed
    json_data = jsm.read_json()
    if json_data and json_data["data"]:
        jsm.to_csv(json_data["data"])
    else:
        print("No expenses to import to CSV (There is no expenses or expenses file doesn't exist)")

def set_budget(data):
    json_data = jsm.read_json()

    if "budget" not in json_data:
        json_data["budget"] = {}

    year = data["Year"] if "Year" in data else str(date.today().year)
    budget_date = f"{data["Month"]}-{year}"

    if data["Amount"] == 0:
        del json_data["budget"][budget_date]
    else:
        json_data["budget"][budget_date] = data["Amount"]

def show_budget():
    json_data = jsm.read_json("budget")
    if json_data:
        print("List of all existing budgets:")
        for date, amount in json_data.items():
            print(f"-- {date}: {amount}")
    else:
        print("No month has a budget yet")