from database import conn, cursor
from datetime import datetime


def add_expense():
    categories = [
        "Food",
        "Transport",
        "Education",
        "Entertainment",
        "Shopping",
        "Other"
    ]

    while True:
        try:
            amount = float(input("Enter Expense amount: "))

            if amount <= 0:
                print("Amount must be greater than 0")
            else:
                break

        except ValueError:
            print("Please enter a valid number")

    print("\nCategories:")

    for i in range(len(categories)):
        print(i + 1, ".", categories[i])

    while True:
        category_choice = input("Choose a category (1-6): ")

        if category_choice.isdigit():
            category_choice = int(category_choice)

            if 1 <= category_choice <= len(categories):
                category = categories[category_choice - 1]
                break

        print("Invalid Category. Please choose a number from 1 to 6.")

    description = input("Enter description: ")

    date = datetime.now().strftime("%d-%m-%Y")

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))

    conn.commit()

    print("\nExpense added successfully!")


def get_expenses():
    cursor.execute("""
        SELECT id, amount, category, description, date
        FROM expenses
        ORDER BY id
    """)

    return cursor.fetchall()


def update_expense(expense_id, amount, category, description, date):
    cursor.execute("""
        UPDATE expenses
        SET amount = ?,
            category = ?,
            description = ?,
            date = ?
        WHERE id = ?
    """, (amount, category, description, date, expense_id))

    conn.commit()


def delete_expense(expense_id):
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()


def get_total_spent():
    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    return total