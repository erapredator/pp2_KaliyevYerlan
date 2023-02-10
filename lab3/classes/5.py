class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to the account of {self.owner}")
        print(f"Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Regected")
            print(f"It is impossible to withdraw {amount}. You have in your balance {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account of {self.owner}")
            print(f"Current balance: {self.balance}")

account = BankAccount("Kaliyev Yerlan")

while True:
    print("Enter 'd' to deposit, 'w' to withdraw, or 'q' to quit:")
    choice = input().lower()
    if choice == 'd':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == 'w':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 'q':
        break
    else:
        print("Invalid input. Try again.")
