# Expense Tracker Project

expensesList = []  # list of expenses in form of dictionary
print("Welcome to Expenses Tracker 🙏 : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spend")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice (1-4) : "))

    # 1. Add Expense
    if choice == 1:
        date = input("On which date did you make the expense? (DD-MM-YYYY): ")
        category = input(
            "What type of expense did you make? (Food, Travel, Shopping, Books): "
        )
        description = input("Give more details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }
        expensesList.append(expense)
        print("\nExpense is added successfully ✅")

    # 2. View All Eexpenses
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expenses Added. Please add an expense first.")
        else:
            print("===== Here are all your expenses =====")
            count = 1
            for eachExpense in expensesList:
                print(
                    f"Expense Number {count} -> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["amount"]}"
                )
                count = count + 1

    # 3. View Total Spending
    elif choice == 3:
        total = 0
        for eachSpend in expensesList:
            total = total + eachSpend["amount"]
        print("\nTotal Spend = ", total)

    # 4. Exit
    elif choice == 4:
        print("Thank you for using our system 💻")
        break
    else:
        print("Invalid choice. Please try again.")
