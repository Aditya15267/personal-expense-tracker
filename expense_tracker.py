import csv
import os

EXPENSE_FILE = 'expenses.csv'

def initialise_file():
    """Create the expense file if it does not exist"""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

def add_expense():
    """Add a new expense entry"""
    date = input('Enter the date (YYYY-MM-DD): ')
    category = input('Enter the category (Food, Transport, Entertainment, etc.): ')
    amount = input('Enter the amount: ')
    description = input('Enter short description: ')

    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print('Expense added successfully!\n')

def view_expense():
    """Display all recorded expenses"""
    if not os.path.exists(EXPENSE_FILE):
        print('No expenses found. Start adding some!\n')
        return
    
    with open(EXPENSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) <= 1:
        print('No expenses recorded yet.\n')
        return
    
    print('\n Your Expenses: \n')
    print('Date | Category | Amount | Description')
    print('-----------------------------------')
    for rows in expenses[1:]:
        print(f"{rows[0]} | {rows[1]} | {rows[2]} | {rows[3]}")
    print('\n')

def main():
    """Main menu for the expense tracker"""
    initialise_file()

    while True:
        print('Personal Expense Tracker')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            print('Exiting... Thank you for using the expense tracker!')
            print('Have a great day!')
            break
        else:
            print('Invalid choice. Try again.\n')

if __name__ == '__main__':
    main()