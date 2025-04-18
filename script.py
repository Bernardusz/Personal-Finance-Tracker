from allfunctions import User, Transaction, Income, Expense, database, FinanceTracker
from allfunctions import read_welcone

if __name__ == "__main__":
    FinanceTrackerApp = FinanceTracker()
    read_welcone()
    print("Make sure when inputting data, NO SPACE !")
    while True:
        userinput = input("What do you want to do ? : ")
        
        if userinput == "Add User":
            new_user = input("Input your name, income per month, and money left : ").split(",")
            try:
                FinanceTrackerApp.add_user(new_user[0], int(new_user[1]), int(new_user[2]))
                print(f"Welcome {new_user[0]} !")
            except:
                print("Invalid number !")
        
        elif userinput == "Log in":
            login = input("Input your username : ")
            try:
                FinanceTrackerApp.log_in(login)
                print(f"Welcome {login} !")
            except:
                print("User doesn't exist !")
        
        elif userinput == "Change Monthly Income":
            new_income = input("Enter the new amount : ")
            if FinanceTrackerApp.loggedin == True:
                try:
                    FinanceTrackerApp.change_income(int(new_income))
                    print("Changed !")
                except:
                    print("Invalid input !")
            else:
                print("You hasn't logged in yet !")
        
        elif userinput == "Add Incomes":
            new_incomes = input("Enter the amount, category, date : ").split(",")
            if FinanceTrackerApp.loggedin == True:
                try:
                    FinanceTrackerApp.add_income(int(new_incomes[0]), new_incomes[1], new_incomes[2])
                    print("Added !")
                except:
                    print("Invalid input !")
            else:
                print("You hasn't logged in yet !")
        
        elif userinput == "Add Expenses":
            new_expenses = input("Enter the amount, category, date : ").split(",")
            if FinanceTrackerApp.loggedin == True:
                try:
                    FinanceTrackerApp.add_expenses(int(new_expenses[0]), new_expenses[1], new_expenses[2])
                    print("Added !")
                except:
                    print("Invalid input !")
            else:
                print("You hasn't logged in yet !")
        
        elif userinput == "View All Transactions":
            if FinanceTrackerApp.loggedin == True:
                FinanceTrackerApp.view_transaction()
            else:
                print("You hasn't logged in yet !")

        elif userinput == "View Balance/s Left":
            if FinanceTrackerApp.loggedin == True:
                FinanceTrackerApp.view_balance()
            else:
                print("You hasn't logged in yet !")
        
        elif userinput == "View By Category":
            category = input("Enter a category: ")
            if FinanceTrackerApp.loggedin == True:
                if category.lower() == "expense":
                    FinanceTrackerApp.view_expense()
                elif category.lower() == "income":
                    FinanceTrackerApp.view_income()
                else:
                    print("Heading to else")
                    FinanceTrackerApp.viewby_category(category)
            else:
                print("You hasn't logged in yet !")

        elif userinput == "Save To Json":
            jsonfile = input("Enter file name [file.json] : ")
            if FinanceTrackerApp.loggedin == True:
                # try:
                FinanceTrackerApp.save_json(jsonfile)
                print("Added !")
                # except:
                #     print("Invalid input !")
            else:
                print("You hasn't logged in yet !")
        
        elif userinput == "Load From Json":
            try :
                jsonfile1 = input("Enter file name [file.json] : ")
                FinanceTrackerApp.load_json(jsonfile1)
            except:
                print("Invalid File Name !")
        
        elif userinput == "Exit":
            print("See you ! Don't forget, save your money !")
            break
        
        else:
            print("Invalid Command !")