[Previous Project (Project #2 - GitHub User Activity)](https://github.com/fredidiaz17/github-user-activity)

> 🌐 [Leer en Español](README.es.md)

# Project #3 - Expense Tracker

Expense Tracker is a project from [Roadmap.sh](https://roadmap.sh/projects/expense-tracker).

## What is it about?

This project allows you to manage personal expenses from the command line. You can **add, update, delete, and query** expenses, view summaries by month or category, set **monthly budgets** with automatic alerts when exceeded, and export your data to **CSV**.

All data is stored in an `expenses.json` file generated automatically on first use.

---

## Prerequisites

- Python **3.10** or higher
- Install dependencies:

```powershell
pip install pandas
```

---

## Installation and usage

1. Clone the repository.
```powershell
git clone https://github.com/fredidiaz17/Expense-Tracker
```

2. Navigate to the project folder.
```powershell
cd expense-tracker
```

3. Install dependencies.
```powershell
pip install pandas
```

4. Run the program.
```powershell
python expense_tracker.py <command> [arguments]
```

---

## Commands

### `add` — Add an expense

Adds a new expense. **Description** and **amount** are required.

```powershell
python expense_tracker.py add --description "Lunch" --amount 20
```

#### Arguments

| Argument | Short | Required | Description | Example |
|----------|-------|----------|-------------|---------|
| `--description` | `-d` | ✅ | Expense description (max. 100 characters) | `--description "Lunch"` |
| `--amount` | `-a` | ✅ | Expense amount (positive integer, max. 999999) | `--amount 20` |
| `--category` | `-c` | ❌ | Expense category (max. 30 characters) | `--category Food` |

---

### `list` — List expenses

Displays all recorded expenses in table format.

```powershell
python expense_tracker.py list
```

#### Optional arguments

| Argument | Short | Description | Example |
|----------|-------|-------------|---------|
| `--category` | `-c` | Filters expenses by category | `python expense_tracker.py list --category Food` |

---

### `summary` — Expense summary

Shows the total of all expenses. Can be filtered by month of the current year and/or by category.

```powershell
python expense_tracker.py summary
```

#### Optional arguments

| Argument | Short | Description | Example |
|----------|-------|-------------|---------|
| `--month` | `-m` | Month of the current year (1-12) | `python expense_tracker.py summary --month 7` |
| `--category` | `-c` | Category to summarize | `python expense_tracker.py summary --category Food` |

Both arguments can be combined.

---

### `update` — Update an expense

Updates one or more fields of an existing expense by its ID. At least one field to update is required.

```powershell
python expense_tracker.py update <id> --amount 30
```

#### Arguments

| Argument | Short | Required | Description |
|----------|-------|----------|-------------|
| `id` | — | ✅ | ID of the expense to update (positional) |
| `--description` | `-d` | ❌ | New description (max. 100 characters) |
| `--amount` | `-a` | ❌ | New amount (positive integer, max. 999999) |
| `--category` | `-c` | ❌ | New category (max. 30 characters) |

---

### `delete` — Delete an expense

Deletes an existing expense by its ID.

```powershell
python expense_tracker.py delete <id>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `id` | ✅ | ID of the expense to delete (positional) |

---

### `csv` — Export to CSV

Exports all expenses to an `expenses.csv` file in the current directory.

```powershell
python expense_tracker.py csv
```

---

### `budget` — Budget management

Manages the monthly budget. Has two subcommands: `set` and `list`.

#### `budget set` — Set a budget

Sets the budget for a given month. If a budget already exists for that month, it is overwritten. If the amount is `0`, the existing budget is removed.

```powershell
python expense_tracker.py budget set --month 7 --amount 500
```

| Argument | Short | Required | Description |
|----------|-------|----------|-------------|
| `--month` | `-m` | ✅ | Month (1-12) |
| `--amount` | `-a` | ✅ | Budget amount (0 to delete) |
| `--year` | `-y` | ❌ | Year (between 2000 and 10 years from current). Defaults to current year if omitted. |

#### `budget list` — List budgets

Displays all existing budgets.

```powershell
python expense_tracker.py budget list
```

> ⚠️ **Budget alert**: When adding or updating an expense, the program automatically checks whether the month's total exceeds the set budget, displaying a warning if so.

---

## Project structure

```text
expense-tracker/
├── expense_tracker.py       # Program entry point
├── expense_functions.py     # Core logic for each command
├── json_manager.py          # Read, write, and CSV export operations
├── expenses.json            # Auto-generated on first use
├── expenses.csv             # Generated when running the csv command
└── README.md
```

---

## Limitations

- Expense amounts are integers; decimals are not supported.
- The month filter in `summary` always corresponds to the current year.
- Budgets with no year specified are assigned to the current year, regardless of the month provided.

---

## Development challenges

1. **Nested subparsers in argparse**: The `budget` command required nesting subparsers inside an already existing subparser — a more complex structure than the mutually exclusive arguments used in previous projects, but one that better reflects the experience of real CLI tools.
2. **Simultaneous use of Pandas and JSON**: The expense list is displayed using a Pandas `DataFrame` built from the JSON file, which required thinking about how to keep the JSON schema compatible with both CRUD operations and DataFrame construction.
3. **Closures in argparse**: Closures were used for argument validation functions — the first time this pattern was implemented — proving especially useful for parameterizing reusable validators.
4. **Budget system design**: Defining the upsert behavior, year handling, validation boundaries, and alert logic required several design decisions not specified by the project brief.

---

## License

This is a **personal project with no defined license**.

---

[Next Project (N/A)]()