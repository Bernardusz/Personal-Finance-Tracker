from abc import ABC, abstractmethod
import json
class User:#As a flex, i add user~
    def __init__(self, username, incomemonth, money):
        self.username = username
        self.__income = incomemonth
        self.__money = money #money left
        self.__transaction = {"income" : [],
                              "expense" : []}
    @property
    def return_info_income(self):
        return self.__income

    @property
    def return_info_money(self):
        return self.__money
    
    @property
    def return_transaction(self):
        return self.__transaction
    
    @property
    def return_transaction_expense(self):
        return self.__transaction["expense"]
    
    @property
    def return_transaction_income(self):
        return self.__transaction["income"]
    
    def change_income(self, amount):
        self.__income += amount
        
    def expenses(self, amount, objtransaction):
        self.__money -= amount
        self.__transaction["expense"].append(objtransaction)

    def income(self, amount, objtransaction):
        self.__money += amount
        self.__transaction["income"].append(objtransaction)

class Transaction(ABC):
    def __init__(self, moneyflow, category, date):
        self.moneyflow = moneyflow
        self.category = category
        self.date = date
    
    def edit_moneyflow(self):
        pass

class Income(Transaction):
    def __init__(self, moneyflow, category, date, user_obj):
        super().__init__(moneyflow, category, date)
        self.user = user_obj 

    def edit_moneyflow(self, instance):
        self.user.income(self.moneyflow, instance)
    
class Expense(Transaction):
    def __init__(self, moneyflow, category, date, user_obj):
        super().__init__(moneyflow, category, date)
        self.user = user_obj 

    def edit_moneyflow(self, instance):
        self.user.expenses(self.moneyflow, instance)
        
        
    
class database:
    Users = {}

class FinanceTracker:
    def __init__(self):
        self.users = database.Users
        self.current_user = {}
        self.username = ""
        self.loggedin = False

    def add_user(self, username, income, money):
        self.users[username] = User(username, income, money)
        print("Added !")
    
    def log_in(self, username):
        self.username = username
        self.current_user = self.users[username]
        self.loggedin = True
    
    def change_income(self, amount):
        self.current_user[self.username].change_income(amount)
    
    def add_income(self, amount, category, date):
        user_obj = self.current_user[self.username]
        instance = Income(amount, category, date, user_obj)
        instance.edit_moneyflow(instance)
    
    def add_expenses(self, amount, category, date):
        username = self.current_user[self.username].username
        instance = Expense(amount, category, date, username)
        instance.edit_moneyflow(instance)
    
    def view_balance(self):
        print(f"Your balance is : {self.current_user[self.username].return_info_money}")

    def view_transaction(self):
        print("Here is the complete data : ")
        print(self.current_user[self.username].return_transaction)

    def view_expense(self):
        expenses = self.current_user[self.username].return_transaction_expense
        for i in range(len(expenses)):
            print(f"Date : {expenses[i].date} \nCategory : {expenses[i].category} \nAmount : {expenses[i].moneyflow}")
    
    def view_income(self):
        income = self.current_user[self.username].return_transaction_income
        for i in range(len(income)):
            print(f"Date : {income[i].date} \nCategory : {income[i].category} \nAmount : {income[i].moneyflow}")

    def viewby_category(self, category):
        expenses = self.current_user[self.username].return_transaction_expense
        income = self.current_user[self.username].return_transaction_income
        for i in range(len(expenses)):
            if category == expenses[i].category:
                print(f"Date : {expenses[i].date} \nCategory : {expenses[i].category} \nAmount : {expenses[i].moneyflow}")
        for i in range(len(income)):
            if category == income[i].category:
                print(f"Date : {income[i].date} \nCategory : {income[i].category} \nAmount : {income[i].moneyflow}")

    def save_json(self, file):
        username =  self.current_user[self.username].username
        incomes = self.current_user[self.username]. return_transaction_income
        expenses = self.current_user[self.username]. return_transaction_expense
        money = self.current_user[self.username].return_info_money
        incomemonth = self.current_user[self.username].return_info_income
        data = {}
        data[username] = {"money" : money,
                          "income per month" : incomemonth,
                          "incomes": [{"amount": i.moneyflow, "category": i.category, "date": i.date} for i in incomes],
                          "expenses": [{"amount": e.moneyflow, "category": e.category, "date": e.date} for e in expenses]}

        
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_json(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            for key in data:
                self.add_user(key, data[key]["income per month"], data[key]["money"])
                self.log_in(key)
                for i in data[key]["incomes"]:
                    self.add_income(i["amount"], i["category"], i["date"])

                for i in data[key]["expenses"]:
                    self.add_expenses(i["amount"], i["category"], i["date"])

                
def read_welcone():
    with open("welcome.txt", "r") as f:
        lines = f.readlines()    
        for line in lines:
            print(line)   

    
    
        
    

