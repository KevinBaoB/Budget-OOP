from classes.transcation import Transaction
from classes.months import Months
from classes.budget import Budget
from classes.category import Category


class Interface:
    def __init__(self):
        self.budget = Budget()


    def start_up(self):
        while True:
            self.menu_start()
            option = int(input("\nSelect an option: \n"))
            if option == 1:
                month = int(input("Enter Month: \n")) - 1
                print("Your monthly expense for the month chosen is: ")
                expense = self.budget.get_monthly_cost(month)
                print(f"You spent {expense}$ in the month of {Months(month).name}.")
                

            elif option == 2:
                month = int(input("\nEnter month: ")) - 1

                category_cost = self.budget.get_month_cost_by_category(month)
                for cat in category_cost:
                    print(f"{Category(cat).name}: %{category_cost[cat]} of all expenses in the month of {Months(month).name}")

            elif option == 3:
                amount = int(input("\nAdd a transaction: "))
                category = int(input(f"""\nSelect one of the categories: \n1.Living\n2.Food\n3.Travel\n4.Savings\n5.Leisure\n"""))
                month = int(input("\nEnter month: ")) - 1
                tran = Transaction(amount, category, month)
                try:   
                    self.budget.add_transactions(tran)
                    print("Transaction SUCCESSFUL!")
                except:
                    print("ERROR TRANSACTION UNSUCCESSFUL!")

            elif option == 4:
                new_income = int(input("\nEnter new income amount: "))
                self.budget.set_monthly_income(new_income)

            elif option == 5:
                break

            print("\n______________\n")

    def menu_start(self):
        print(f"""1. See Total Monthly Expenses\n2. See Cost by Category\n3. Add Transaction\n4. Set Monthly Income\n5. Quit""")