from models import expense as exp_mod
from services import storage as storage_mod
from ui import menu
from utils.helpers import clear
clear()

#traffic control and logic

#start the app:
    #show the menu
    #connect everything --> make everything flow well
#do not:
    #perform JSON handling
    #perform analytics


def main():
    expense_config = {
        "value":15,
        "category":"food",
        "date":"5/11"
        }
    
    expense_config_2 = {
        "value":20,
        "category":"leisure",
        "date":"5/16",
        "note":"TESTING"
    }

    expense_a = exp_mod.Expense(expense_config)
    expense_b = exp_mod.Expense(expense_config_2)

    storage_mod.save_expenses(expense_a)
    storage_mod.save_expenses(expense_b)


    #menu.run_menu()


main()