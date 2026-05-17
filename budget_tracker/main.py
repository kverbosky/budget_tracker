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

    expense_a = exp_mod.Expense(expense_config)
    print(expense_a.get_config())

    storage_mod.save_expenses(expense_a)
    print(storage_mod.load_expenses())


    menu.run_menu()


main()