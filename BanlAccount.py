class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance


        class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Error: Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully to", other_account.account_holder)
        else:
            print("Error: Insufficient balance for transfer.")


# Creating two BankAccount objects
account1 = BankAccount("Prachi")
account2 = BankAccount("Riya")

# Deposits
account1.deposit(5000)
account2.deposit(3000)

# Display balances
account1.display_balance()
account2.display_balance()

# Withdrawals
account1.withdraw(1000)
account2.withdraw(500)

# Transfer money
account1.transfer(1500, account2)

# Display final balances
print("\nFinal Account Details:")
account1.display_balance()
account2.display_balance()