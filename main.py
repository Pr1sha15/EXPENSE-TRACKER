from datetime import datetime

from database import conn, cursor

from expense_manager import(
    add_expense,
    get_expenses,
    update_expense,
    delete_expense,
    get_total_spent
)

print("=============================")
print("   STUDENT EXPENSE TRACKER  ")
print("=============================")

expenses = []

categories = [
    "Food",
    "Transport",
    "Education",
    "Entertainment",
    "Shopping",
    "Other"
]
    
settings = {
    "budget": 0
}

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Category analysis")
    print("5. Delete Expense")
    print("6. Edit Expense")
    print("7. Set Budget")
    print("8. Check Budget")
    print("9. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
        
    elif choice == "2":
        cursor.execute("""
        SELECT id, amount, category, description, date
        FROM expenses
        ORDER by id
        """)
        
        rows = cursor.fetchall()
        
        if len(rows) == 0:
            print("\nNo Expenses recorded yet.")
        else:
            print("\n======= YOUR EXPENSES =======")
            
            for row in rows:
                print("------------------")
                print("ID: ", row[0])
                print("Amount: ", row[1])
                print("Category: ", row[2])
                print("Description: ", row[3])
                print("Date: ", row[4])
                
            print("-------------------")
              
    elif choice == "3":
        if len(expenses) == 0:
            print("\nNo Expenses recorded yet")
            
        else:
            total = 0
            
            for expense in expenses:
                total = total + expense["amount"]
                
        print("\nTotal Spent: ", total)
        
    elif choice == "4":
        if len(expenses) == 0:
            print("\nNo Expenses recorded yet.")
        else:
            category_totals = {}
            
            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]
                
                if category in category_totals:
                    category_totals[category] = category_totals[category] + amount
                else:
                    category_totals[category] = amount
                    
            print("\n==========SPENDING BY CATEGORY===========")
            
            for category in category_totals:
                print(category, ": ", category_totals[category])
       
    elif choice == "5":
        expense_id = input("Enter the ID of the expense to delete: ")
        
        if expense_id.isdigit():
            expense_id = int(expense_id)
            
            cursor.execute(
                "SELECT * FROM expenses WHERE id = ?",
                 (expense_id,)
                 
            )
            
            expense = cursor.fetchone()
            
            if expense is not None:
                cursor.execute(
                    "DELETE FROM expenses WHERE id = ?",
                    (expense_id,)
                )
                
                conn.commit()
                
                print("\nExpense deleted successfully!")
                
            else:
                print("\nExpense ID not found.") 
                
        else:
            print("\nPlease enter a valid ID.")
        
    elif choice == "6":
        if len(expenses) == 0:
            print("\nNo expenses to edit.")
            
        else:
            expense_id = int(input("Enter the ID of the expense to edit: "))
            
            found = False
            
            for expense in expenses:
                if expense["id"] == expense_id:
                    
                    print("\nEnter the new details:")
                    
                    expense["amount"] = float(input("Enter new amount: ₹"))
                    
                    print("\nCategories: ")
                            
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
                            
                    expense["description"] = input("Enter new description: ")
                    expense["date"] = input("Enter new date (DD-MM-YYYY): ")

                    found = True

                    print("\nExpense updated successfully!")
                    break
                
                if not found:
                    print("Expense ID not found.")       
    
    elif choice == "7":
        while True:
            try:
                budget = float(input("Enter your monthly budget: "))
                
                if budget <= 0:
                    print("Budget must be greater than 0")
                else:
                    break
                
            except ValueError:
                print("Please enter a valid number")
                
        settings["budget"] = budget 
        
        print("Monthly budget set to", budget)
                
    elif choice == "8":
        budget = settings["budget"]

        if budget == 0:
            print("\nPlease set your budget first.")

        else:
            total = get_total_spent()
            remaining = budget - total

            print("\n======== BUDGET ========")
            print("Monthly Budget:", budget)
            print("Total Spent:", total)
            print("Remaining:", remaining)

            if total >= budget:
                print("⚠️ You have exceeded your budget!")

            elif total >= budget * 0.8:
                print("⚠️ Warning: You have used 80% or more of your budget!")

            else:
                print("✅ You are within your budget")
        
    elif choice == "9":
        print("Thank you for using Student Expense Tracker!")
        break
    
    else:
        print("Invalid choice. PLease try again")
    
