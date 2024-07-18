class BankAccount:
  def __init__(self, account_number, account_name, balance=0):
    self.account_number = 10001
    self.account_name = account_name
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"You Deposited Rs.{amount} . Your new balance is: Rs.{self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient balance")
    else:
      self.balance -= amount
      print(f"You Withdrew Rs.{amount}. Your new balance is: Rs.{self.balance}")

  def check_balance(self):
    print(f"Your current balance is: Rs.{self.balance}")

class Bank:
  def __init__(self):
    self.accounts = {}

  def create_account(self):
    account_number = 10001+1
    account_name = input("Enter account name: ")
    initial_balance = float(input("Enter initial balance: "))
    self.accounts[account_number] = BankAccount(account_number, account_name, initial_balance)
    print(f"Account {account_number} created for {account_name} with initial balance {initial_balance}")

  def deposit(self):
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    if account_number in self.accounts:
      self.accounts[account_number].deposit(amount)
    else:
      print("Account not found")

  def withdraw(self):
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    if account_number in self.accounts:
      self.accounts[account_number].withdraw(amount)
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
  while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
      bank.create_account()
    elif choice == "2":
      bank.deposit()
    elif choice == "3":
      bank.withdraw()
    elif choice == "4":
      bank.check_balance()
    elif choice == "5":
      print("    Exiting. . .  . .!!")
      break
    else:
      print("Invalid option. Please try again.")

if __name__ == "__main__":
  main()
