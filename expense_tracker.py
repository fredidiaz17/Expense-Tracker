# Archivo de inicio.
import sys
import expense_functions as ef
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

     # ADD
    parser_add = subparsers.add_parser("add", help="Add a new expense")
    # Required argument with "add".
    parser_add.add_argument(
        "--description","-d",
        required= True,
        help="Description of the expense")
    parser_add.add_argument(
        "--amount", "-a",
        type=int,
        required= True,
        help= "amount of the expense"
    )
    parser_add.add_argument(
        "--category", "-c",
        help= "category of the expense"
    )

    # List
    parser_list = subparsers.add_parser("list", help="List all expenses")
    parser_list.add_argument(
        "--category", "-c",
        help= "category of the expenses to be shown"
    )

    # Summary
    parser_summary = subparsers.add_parser("summary", help="Show expenses summary")
    parser_summary.add_argument(
        "--month","-m",
        type=int,
        choices=(1,12),# Number of months
        help="Month of the current year to be summarized"
        )
    parser_summary.add_argument(
        "--category","-c",
        help= "category of the expenses to be summarized"
    )

    # Update
    parser_update = subparsers.add_parser("update", help="Update expense")
    parser_update.add_argument("--id", type=int, required=True, help="Obligatory ID for update")
    parser_update.add_argument("--description", "-d", help="New description of the expense")
    parser_update.add_argument("--amount", "-a", help="Amount of the expense")
    parser_update.add_argument("--category", "-c", help="Category of the expense")

    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete expense")
    parser_delete.add_argument("--id", type=int, required=True, help="Obligatory ID for delete")

    # To CSV
    parser_csv = subparsers.add_parser("csv", help="Export the expenses to a csv file")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.command == "add":
        data = {"Description":args.description,"Amount":args.amount}
        if args.category:
            data["Category"] = args.category
        ef.add(data)

    if args.command == "list":
        if not args.category:
            ef.list()
        else:
            ef.list(args.category)

    if args.command == "summary":
        parameters = {}
        if args.month:
            parameters["Month"] = args.month
        if args.category:
            parameters["Category"] = args.category
        ef.summary(parameters)

    if args.command == "update":

        if args.description is None and args.amount is None and args.category is None:
            parser.error("You must enter the Amount, Description or Category of the expense to be updated")

        data = {"ID": args.id}
        if args.description:
            data["Description"] = args.description
        if args.amount:
            data["Amount"] = args.amount
        if args.category:
            data["Category"] = args.category
        ef.update(data)

    if args.command == "delete":
        ef.delete(args.id)

    if args.command == "csv":
        ef.csv_export()