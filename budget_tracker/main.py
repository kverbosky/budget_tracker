import os
import json
os.system("cls")

def main():
    expenses = []
    expense = {"cost":15, "category":"food"}

    expenses.append(expense)

    for expense in expenses:
        print(expense)

    with open("expenses.json", "w") as file:
        json.dump(expense, file)

    with open("expenses.json", "r") as file:
        expenses = json.load(file)


main()