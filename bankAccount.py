class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount

    def __str__(self):
        return "{} Amount: {}".format(self.account_type, self.amount)


qazi = BankAccount("Checkings", 100)
print(narendra.account_type)
print(narendra.amount)

qazi.deposit(30)
print(narendra.amount)

qazi.withdraw(45)
print(narendra)
print(narendra.amount)
