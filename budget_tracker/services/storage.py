import json
import os
from models import expense as exp_mod
#save data / load data
#handle JSONs and files
#no menus, no printing

def save_expenses(expense: exp_mod.Expense, target_path="data", target_file="expenses"):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as file:
        json.dump(list(expense.get_config()), file) #only writing dictionary values?

def load_expenses(target_path="data", target_file="expenses"):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), "r") as file:
        expenses = json.load(file)
    return expenses

