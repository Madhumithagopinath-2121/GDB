from Account import Account


def display_account(account):
    print(
        f"Account #{account.getAccountNumber()} | "
        f"{account.getName()} ({account.getAge()} yrs) | "
        f"{account.getAccountType()} | "
        f"₹{account.getBalance()} | "
        f"{account.getStatus()}"
    )


print("=" * 50)
print("GLOBAL DIGITAL BANK - ACCOUNT TEST")
print("=" * 50)

# 1. Creating Account
print(">>> 1. Creating Account")

account1 = Account(1001, "John Doe", 25, 1000.0, "Savings")

print("Account created!")
display_account(account1)

# 2. Deposit Money
print(">>> 2. Deposit Money")

amount = 500.0
result = account1.deposit(amount)

if result:
    print(f"Depositing ₹{amount}: SUCCESS")
    print(f"New balance: ₹{account1.getBalance()}")
else:
    print(f"Depositing ₹{amount}: FAILED")

amount = -100.0
result = account1.deposit(amount)

if result:
    print(f"Depositing ₹{amount}: SUCCESS")
else:
    print(f"Depositing ₹{amount}: FAILED (Invalid amount)")

# 3. Withdraw Money
print(">>> 3. Withdraw Money")

amount = 200.0
result = account1.withdraw(amount)

if result:
    print(f"Withdrawing ₹{amount}: SUCCESS")
    print(f"New balance: ₹{account1.getBalance()}")
else:
    print(f"Withdrawing ₹{amount}: FAILED")

amount = 2000.0
result = account1.withdraw(amount)

if result:
    print(f"Withdrawing ₹{amount}: SUCCESS")
else:
    print(f"Withdrawing ₹{amount}: FAILED (Insufficient balance)")

print(f"Current balance: ₹{account1.getBalance()}")

# 4. Creating Another Account
print(">>> 4. Creating Another Account")

account2 = Account(1002, "Jane Smith", 30, 2000.0, "Current")

display_account(account2)

# 5. All Accounts
print(">>> 5. All Accounts")

display_account(account1)
display_account(account2)

print("=" * 50)
print("TEST COMPLETED!")
print("=" * 50)