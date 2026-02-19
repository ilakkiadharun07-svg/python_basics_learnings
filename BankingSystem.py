import json
import os


class BankAccount:
    def __init__(self, account_number, name, balance=0, transactions=None):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful.")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print("-", t)

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def create_account(self):
        acc_no = input("Enter Account Number: ")

        if acc_no in self.accounts:
            print("Account already exists.")
            return

        name = input("Enter Account Holder Name: ")
        account = BankAccount(acc_no, name)
        self.accounts[acc_no] = account
        self.save_data()
        print("Account created successfully.")

    def get_account(self):
        acc_no = input("Enter Account Number: ")
        account = self.accounts.get(acc_no)

        if not account:
            print("Account not found.")
            return None
        return account

    def deposit(self):
        account = self.get_account()
        if account:
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                self.save_data()
            except ValueError:
                print("Invalid input.")

    def withdraw(self):
        account = self.get_account()
        if account:
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
                self.save_data()
            except ValueError:
                print("Invalid input.")

    def check_balance(self):
        account = self.get_account()
        if account:
            account.show_balance()

    def show_transactions(self):
        account = self.get_account()
        if account:
            account.show_transactions()

    def save_data(self):
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        with open("bank_data.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        if os.path.exists("bank_data.json"):
            with open("bank_data.json", "r") as file:
                data = json.load(file)
                for acc_no, acc_data in data.items():
                    self.accounts[acc_no] = BankAccount(
                        acc_data["account_number"],
                        acc_data["name"],
                        acc_data["balance"],
                        acc_data["transactions"]
                    )

    def menu(self):
        while True:
            print("\n====== Bank Management System ======")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.show_transactions()
            elif choice == "6":
                print("Exiting system...")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    bank = BankSystem()
    bank.menu()
