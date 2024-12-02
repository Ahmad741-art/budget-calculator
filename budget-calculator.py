import json  # Importing the JSON library for handling file operations with JSON format.

# Function to add an expense to the list
def add_expense(expenses, description, amount):
    """
    Adds an expense to the list of expenses.

    Parameters:
        expenses (list): List of existing expenses.
        description (str): Description of the expense.
        amount (float): Amount of the expense.

    Returns:
        None
    """
    expenses.append({"description": description, "amount": amount})  # Add expense as a dictionary to the list.
    print(f"Added expense: {description}, Amount: {amount}")  # Confirm the addition.

# Function to calculate the total of all expenses
def get_total_expenses(expenses):
    """
    Calculates the total amount of all expenses.

    Parameters:
        expenses (list): List of expense dictionaries.

    Returns:
        float: Sum of all expense amounts.
    """
    return sum(expense['amount'] for expense in expenses)  # Sum up all the amounts in the expenses list.

# Function to calculate the remaining balance
def get_balance(budget, expenses):
    """
    Calculates the remaining budget after expenses.

    Parameters:
        budget (float): Initial budget.
        expenses (list): List of expense dictionaries.

    Returns:
        float: Remaining budget.
    """
    return budget - get_total_expenses(expenses)  # Subtract total expenses from the initial budget.

# Function to display the budget and expenses in detail
def show_budget_details(budget, expenses):
    """
    Displays the budget, all expenses, total spent, and remaining balance.

    Parameters:
        budget (float): Initial budget.
        expenses (list): List of expense dictionaries.

    Returns:
        None
    """
    print(f"Total Budget: {budget}")
    print("Expenses:")
    # Iterate through each expense and display its details.
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")  # Display total spent.
    print(f"Remaining Budget: {get_balance(budget, expenses)}")  # Display remaining balance.

# Function to load budget data from a JSON file
def load_budget_data(filepath):
    """
    Loads budget data (initial budget and expenses) from a JSON file.

    Parameters:
        filepath (str): Path to the JSON file.

    Returns:
        tuple: Initial budget and expenses list.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)  # Load JSON data from file.
            return data['initial_budget'], data['expenses']  # Return the budget and expenses.
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return default values if file doesn't exist or is invalid.

# Function to save budget data to a JSON file
def save_budget_data(filepath, initial_budget, expenses):
    """
    Saves budget data (initial budget and expenses) to a JSON file.

    Parameters:
        filepath (str): Path to the JSON file.
        initial_budget (float): Initial budget value.
        expenses (list): List of expense dictionaries.

    Returns:
        None
    """
    data = {
        'initial_budget': initial_budget,  # Store the initial budget.
        'expenses': expenses  # Store the expenses list.
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)  # Save data in JSON format with indentation.

# Main function to handle the user interface and program flow
def main():
    """
    Main function for the Budget App. Allows users to manage their budget and expenses.

    Returns:
        None
    """
    print("Welcome to the Budget App")  # Greet the user.

    # Get the user's initial budget.
    initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget  # Set the budget variable to the entered amount.
    expenses = []  # Initialize an empty list to store expenses.

    while True:  # Loop for continuous user interaction until they choose to exit.
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")  # Prompt the user for a choice.

        if choice == "1":
            # Add a new expense.
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)  # Call add_expense to record the expense.
        elif choice == "2":
            # Show the current budget and expense details.
            show_budget_details(budget, expenses)
        elif choice == "3":
            # Exit the application.
            print("Exiting Budget App. Goodbye!")
            break  # Break the loop to end the program.
        else:
            # Handle invalid input.
            print("Invalid choice, please choose again.")

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function when the script is executed.
