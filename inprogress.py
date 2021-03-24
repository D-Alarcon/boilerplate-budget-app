
class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def get_balance(self):
        total_funds = 0
        for item in self.ledger:
            total_funds += item["amount"]
        return total_funds

    # def transfer(self, amount, category):

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items = f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
        total += item['amount']
        output = title + items + "Total: " + str(total)
        return output




food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
