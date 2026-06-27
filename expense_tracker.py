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

    # List
    parser_list = subparsers.add_parser("list", help="List all expenses")

    # Summary
    parser_summary = subparsers.add_parser("summary", help="Show expenses summary")
    parser_summary.add_argument(
        "--month","-m",
        type=int,
        help="Month of the expense"
        )

    # Update
    parser_update = subparsers.add_parser("update", help="Update expense")
    parser_update.add_argument("--id", type=int, required=True, help="Obligatory ID for update")
    parser_update.add_argument("--description", "-d", help="New description of the expense")
    parser_update.add_argument("--amount", "-a", help="Amount of the expense")

    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete expense")
    parser_delete.add_argument("--id", type=int, required=True, help="Obligatory ID for delete")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.command == "add":
        ef.add({"Description":args.description,"Amount":args.amount})

    if args.command == "list":
        ef.list()

    if args.command == "summary":
        if args.month:
            ef.summary(args.month)
        else:
            ef.summary()

    if args.command == "update":

        if args.description is None and args.amount is None:
            parser.error("Amount or Description is required")

        data = {"ID": args.id}
        if args.description:
            data["Description"] = args.description
        if args.amount:
            data["Amount"] = args.amount

        ef.update(data)

    if args.command == "delete":
        ef.delete(args.id)

