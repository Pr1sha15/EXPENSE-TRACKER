# EXPENSE-TRACKER
# Student Expense Tracker

A Python-based console application designed to help students record, manage, and analyse their daily expenses. The project uses **SQLite** for persistent data storage and is organized into separate Python modules for better structure and maintainability.

## Features

* Add new expenses
* View all recorded expenses
* Calculate total spending
* Analyse spending by category
* Edit existing expenses
* Delete expenses
* Set a monthly budget
* Check remaining budget
* Receive warnings when spending reaches 80% of the budget or exceeds it
* Store expense records permanently using SQLite

## Expense Categories

The application currently supports the following categories:

* Food
* Transport
* Education
* Entertainment
* Shopping
* Other

## Technologies Used

* **Python**
* **SQLite**
* **sqlite3** — Python's built-in SQLite database module
* **datetime** — Used for recording expense dates
* **VS Code** — Development environment

## Project Structure

```text
StudentExpenseTracker/
│
├── main.py                 # Main menu and program flow
├── database.py             # Database connection and table setup
├── expense_manager.py      # Add, view, edit, delete and total expenses
├── budget_manager.py       # Budget-related functionality
├── analytics.py            # Expense/category analysis
├── expenses.db             # SQLite database
└── README.md               # Project documentation
```

## Database

The application uses an SQLite database named `expenses.db`.

The `expenses` table contains:

| Column        | Type    | Description                |
| ------------- | ------- | -------------------------- |
| `id`          | INTEGER | Unique ID for each expense |
| `amount`      | REAL    | Amount spent               |
| `category`    | TEXT    | Expense category           |
| `description` | TEXT    | Description of the expense |
| `date`        | TEXT    | Date of the expense        |

The database and table are automatically created when the application is run for the first time.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/StudentExpenseTracker.git
```

### 2. Open the project folder

```bash
cd StudentExpenseTracker
```

### 3. Run the application

```bash
python main.py
```

No external Python packages are required because the project uses modules from Python's standard library.

## How to Use

After running the program, a menu will be displayed:

```text
1. Add Expense
2. View Expenses
3. Total Spent
4. Category Analysis
5. Delete Expense
6. Edit Expense
7. Set Budget
8. Check Budget
9. Exit
```

Enter the number corresponding to the operation you want to perform.

### Budget Tracking

The budget feature allows the user to:

1. Set a monthly budget.
2. Calculate the total amount spent.
3. Calculate the remaining budget.
4. Receive a warning when 80% or more of the budget has been used.
5. Receive an alert when the budget has been exceeded.

## Input Validation

The application includes basic validation to prevent invalid inputs, including:

* Negative or zero expense amounts
* Invalid category selections
* Invalid budget amounts
* Invalid expense IDs
* Checking the budget before a budget has been set

## Project Architecture

The project follows a modular structure:

* `main.py` handles the main menu and user interaction.
* `database.py` handles the SQLite connection and database setup.
* `expense_manager.py` handles expense-related operations.
* `budget_manager.py` handles budget functionality.
* `analytics.py` handles spending analysis.

This separation makes the project easier to understand, maintain, and extend.

## Submitted by

**Prisha Singh**
26BCE11343

