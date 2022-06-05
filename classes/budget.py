from classes.category import Category

class Budget:
    def __init__(self):
        self.income = 0
        self.transactions = []
    
    # Users should be able to update their monthly income.
    def set_monthly_income(self, income):
        self.income = income
    
    # It should know how much the user's monthly costs are.
    def get_monthly_cost(self, month):
        month_total = 0
        for tran in self.transactions:
            if tran.month == month:
                month_total += tran.amount
        return month_total

# It should be able to create and calculate new expenses.
    def get_month_cost_by_category(self, month):
        category_cost = {}
        for cat in Category:
            category_cost[cat.value] = 0

        for tran in self.transactions:
            if tran.month == month:
                category_cost[tran.category] += tran.amount
            return category_cost

    def add_transactions(self, tran):
        monthly_expenses = self.get_monthly_cost(tran.month)
        if monthly_expenses + tran.amount > self.income:
            print("NOT ENOUGH MONEY TO DO THIS!")
            raise("error")
        self.transactions.append(tran)

# It should be able to tell users what percent of their monthly income is being spent in each category.
    def percentage(self, month):
        total = self.get_monthly_cost(month)
        category_cost = self.get_month_cost_by_category()
        category_percent = {}
        for cat in category_cost:
            category_percent[cat] = 100 * (category_cost[cat] / total)
        return category_percent


    