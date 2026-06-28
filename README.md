# Description

Build a simple expense tracker application to manage your finances. 
The application should allow users to add, delete, and view their expenses.
The application should also provide a summary of the expenses.

## Requirements
Application should run from the command line and should have the following features:

1. Users can add an expense with a description and amount.
2. Users can update an expense.
3. Users can delete an expense.
4. Users can view all expenses.
5. Users can view a summary of all expenses.
6. Users can view a summary of expenses for a specific month (of current year).

Here are some additional features that you can add to the application:

1. Add expense categories and allow users to filter expenses by category.
2. Allow users to set a budget for each month and show a warning when the user exceeds the budget.
3. Allow users to export expenses to a CSV file.

## Commands list
The list of commands and their expected output is shown below:

```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20
```

## Implementation

You can implement the application using any programming language of your choice. 
Here are some suggestions:

1. Use any programming language for any available module for parsing command arguments (e.g. python with the argparse, node.js with commander etc).
2. Use a simple text file to store the expenses data. You can use JSON, CSV, or any other format to store the data.
3. Add error handling to handle invalid inputs and edge cases (e.g. negative amounts, non-existent expense IDs, etc).
4. Use functions to modularize the code and make it easier to test and maintain.


## Adiciones interesantes respecto a proyectos anteriores.
1. subparsers de argparse: Anteriormente ya habia usado argparse con argumentos posicionales y grupos mutuamente excluyentes, pero no subparsers. 
   Definitivamente, es una forma mas elegante de manejar los argumentos, sus requerimientos y exclusiones.
2. Manejar pandas y Json en un solo proyecto: He manejado Json como almacen de datos, y pandas tambien en tareas de Data Analyst, pero nunca los usé simultaneamente.
En este proyecto, por cuestion de impresión (list) mas comoda, decidi usar pandas para la creació de un Data Frame, y  considerado que tambie usé Json, 
fue necesario pensar en como sería optimizar las operaciones CRUD del programa y permitir su manejo en pandas. Un reto particular.