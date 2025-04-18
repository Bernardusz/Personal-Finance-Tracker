# 💰 Personal Finance Tracker (Python CLI App)
A simple command-line based personal finance tracker built with Python!
Track your income, expenses, and savings with easy commands. You can also save your data to JSON files and load them later.

## 🛠 Features
👤 Add and log in as a user

💸 Track incomes and expenses (with date and category)

🧾 View transaction history, balance, and filter by category

💾 Save and load data to/from .json files

📁 Clean and organized OOP structure with abstract base classes

## 📂 Project Structure
```bash
.
├── allfunctions.py     # All classes and core logic
├── script.py           # CLI interface to run the app
└── welcome.txt         # Welcome message displayed on launch
```
## 🚀 How to Run
Clone the repo:

```bash
git clone https://github.com/Bernardusz/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker
```
Run the app:
```bash
python script.py
```

## ✨ Sample Commands
```pgsql
Add User
Log in
Change Monthly Income
Add Incomes
Add Expenses
View All Transactions
View Balance/s Left
View By Category
Save To Json
Load From Json
Exit
```

## 📦 JSON Save Format
When saving to JSON, your data will be stored like this:

```json
{
  "username": {
    "money": 3000,
    "income per month": 5000,
    "incomes": [
      {"amount": 5000, "category": "Salary", "date": "2025-04-01"}
    ],
    "expenses": [
      {"amount": 2000, "category": "Food", "date": "2025-04-02"}
    ]
  }
}
```

## 🧠 Concepts Used
Python OOP (Classes, Inheritance, Encapsulation)

Abstract Base Classes (abc)

File I/O (.txt, .json)

Data persistence and CLI interaction

-------------------------------------------------------

📜 Credits

Made with ❤️ by Bernardus

“Don't forget, save your money!”

