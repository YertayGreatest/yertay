class BankAccount:
    def __init__(self, owner, initial = 0):
        self.owner = owner
        self.balance = initial
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ", amount, ", new balance: ",self.balance)
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        print("withdrew: ",amount,", new balance: ",self.balance)

account = BankAccount(owner="John", initial=1000)
account.deposit(230)
account.withdrawal(400)

            