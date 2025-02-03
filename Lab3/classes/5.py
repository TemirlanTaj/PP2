class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, depAmount):
        self.balance += depAmount
        print(f"Deposit: {depAmount} won\nAvailable: {self.balance} won\n")
    def withdraw(self,wtd):
        if wtd <= self.balance :
            self.balance -= wtd
            print(f"Withdrawal: {wtd} won\nAvailable: {self.balance} won\n")
        else:
            print("Operation declined \nNot enough money for withdrawal\n")


SonKiHun = Account("Player 456", 10000)

print(f"Your balance, {SonKiHun.balance} won\n")

SonKiHun.deposit(1500)

SonKiHun.deposit(500)

SonKiHun.withdraw(2000)

SonKiHun.withdraw(20000)

SonKiHun.deposit(4560000000)