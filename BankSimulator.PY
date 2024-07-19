import random

class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Dear. {self.account_name} You Have successfully Deposited Rs.{amount}. Your new balance is: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Dear. {self.account_name} You Have successfully Withdrew Rs.{amount}. Your new balance is: Rs.{self.balance}")

    def check_balance(self):
        print(f"Dear. {self.account_name} Your current balance is: Rs.{self.balance}")
    

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def load_accounts(self):
        try:
            with open('accounts.txt', 'r') as file:
                for line in file:
                    account_number, account_name, balance = line.strip().split(',')
                    self.accounts[account_number] = BankAccount(account_number, account_name, float(balance))
        except FileNotFoundError:
            pass

    def save_accounts(self):
        with open('accounts.txt', 'w') as file:
            for account_number, account in self.accounts.items():
                file.write(f"{account_number},{account.account_name},{account.balance}\n")

    def create_account(self):
        account_number = random.randint(10000, 99999)
        account_name = input("Enter account name: ")
        initial_balance = float(input("Enter initial balance: "))
        self.accounts[account_number] = BankAccount(account_number, account_name, initial_balance)
        self.save_accounts()
        print(f"           Thank you...! \n Your account has been successfully created. Your account detail as below. \n Account No. {account_number} \n Account Title: {account_name}\n Initial deposit Rs.{initial_balance}")

    def deposit(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            self.save_accounts()
        else:
            print("Account not found")

    def withdraw(self):
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
            self.save_accounts()
        else:
            print("Account not found")

    def check_balance(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            self.accounts[account_number].check_balance()
        else:
            print("Account not found")
    

def main():
    bank = Bank()
    opt = "y"
    while (opt == "y"):

        print("\n           <<<--------------->>>|| WELLCOME TO MY BANK ||<<<--------------->>>")
        print("\n\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance")
        
        choice = input("\nChoose an option: ")
        if choice == "1":
            bank.create_account()
            
            return main()
        elif choice == "2":
            bank.deposit()
            
        elif choice == "3":
            bank.withdraw()

        elif choice == "4":
            bank.check_balance()
            
        else:
            print("Invalid option. Please try again.")
        print("Do you want to continue? (y/n)")
        opt = input()


if __name__ == "__main__":
      main()
