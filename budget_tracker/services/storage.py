import json
import os
from models import expense as exp_mod
#save data / load data
#handle JSONs and files
#no menus, no printing

def save_expenses(expense: exp_mod.Expense, target_path="data", target_file="expenses.json"):
    expenses = load_expenses()
    expenses.append(expense.get_config())
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as file:
        json.dump(expenses, file, indent = 4) 

def load_expenses(target_path="data", target_file="expenses.json"):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    try:
        with open(os.path.join(target_path, target_file), "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        return []
