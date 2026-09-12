from AccountEnhanced import Account
from InvalidAmountException import InvalidAmountException
from InsufficientBalanceException import InsufficientBalanceException
from MinimumBalanceViolationException import MinimumBalanceViolationException
from InactiveAccountException import InactiveAccountException
from InvalidPinException import InvalidPinException


def display_account(account):
    pin_status = "Yes" if account.hasPin() else "No"

    print(
        f"Account #{account.getAccountNumber()} | "
        f"{account.getName()} ({account.getAge()} yrs) | "
        f"{account.getAccountType()} | "
        f"₹{account.getBalance()} | "
        f"{account.getStatus()} | "
        f"PIN: {pin_status}"
    )


print("=" * 60)
print("ACCOUNT TEST WITH EXCEPTIONS")
print("=" * 60)

accounts = []


# Test 1
print("\n>>> Test 1: Valid Account Creation")

try:
    account1 = Account(1001, "John Doe", 25, 1000.0, "Savings")
    accounts.append(account1)

    print("SUCCESS:", end=" ")
    display_account(account1)

except ValueError as e:
    print("EXCEPTION:", e)


# Test 2
print("\n>>> Test 2: Invalid Age (under 18)")

try:
    account2 = Account(1002, "Young Kid", 16, 500.0, "Savings")
    accounts.append(account2)

except ValueError as e:
    print("EXCEPTION:", e)


# Test 3
print("\n>>> Test 3: Invalid Account Type")

try:
    account3 = Account(1003, "Test User", 25, 500.0, "Invalid")
    accounts.append(account3)

except ValueError as e:
    print("EXCEPTION:", e)


# Test 4
print("\n>>> Test 4: Minimum Balance on Creation")

print("\nCreating Savings account with ₹300")

try:
    account4 = Account(1004, "Bob Wilson", 35, 300.0, "Savings")
    accounts.append(account4)

except ValueError as e:
    print("EXCEPTION:", e)


# Test 5
print("\n>>> Test 5: Valid Deposit and Withdrawal")

account5 = Account(1005, "Alice Brown", 30, 1000.0, "Current")
accounts.append(account5)

print("Account:", end=" ")
display_account(account5)

try:
    account5.setPin(1234)
    print("Setting PIN 1234: SUCCESS")

    account5.deposit(500.0)
    print("Depositing ₹500.0: SUCCESS")
    print(f"Balance after deposit: ₹{account5.getBalance()}")

    account5.withdraw(200.0, 1234)
    print("Withdrawing ₹200.0: SUCCESS")
    print(f"Balance after withdrawal: ₹{account5.getBalance()}")

except (InvalidAmountException,
        InsufficientBalanceException,
        MinimumBalanceViolationException,
        InactiveAccountException,
        InvalidPinException) as e:
    print("EXCEPTION:", e)

display_account(account5)


# Test 6
print("\n>>> Test 6: Invalid Deposit (Negative Amount)")

print("Attempting to deposit ₹-100.0")

try:
    account5.deposit(-100.0)

except InvalidAmountException as e:
    print("EXCEPTION:", e)


# Test 7
print("\n>>> Test 7: Insufficient Balance")

account6 = Account(1006, "Charlie Green", 35, 500.0, "Savings")
account6.setPin(1234)
accounts.append(account6)

print("Account:", end=" ")
display_account(account6)

print("Attempting to withdraw ₹1000.0")

try:
    account6.withdraw(1000.0, 1234)

except InsufficientBalanceException as e:
    print("EXCEPTION:", e)


# Test 8
print("\n>>> Test 8: Minimum Balance Violation")

account7 = Account(1007, "Diana Prince", 28, 1000.0, "Savings")
account7.setPin(1234)
accounts.append(account7)

print("Account:", end=" ")
display_account(account7)

print("Attempting to withdraw ₹600.0")

try:
    account7.withdraw(600.0, 1234)

except MinimumBalanceViolationException as e:
    print("EXCEPTION:", e)


# Test 9
print("\n>>> Test 9: Inactive Account Operations")

account8 = Account(1008, "Eve Wilson", 32, 2000.0, "Current")
accounts.append(account8)

print("Account:", end=" ")
display_account(account8)

try:
    account8.closeAccount()
    print("Closing account: SUCCESS")

except RuntimeError as e:
    print("EXCEPTION:", e)

print("Attempting to deposit ₹100.0 on closed account")

try:
    account8.deposit(100.0)

except InactiveAccountException as e:
    print("EXCEPTION:", e)

try:
    account8.reopenAccount()
    print("Reopening account: SUCCESS")

    account8.deposit(100.0)
    print("Depositing ₹100.0 after reopen: SUCCESS")
    print(f"Balance after deposit: ₹{account8.getBalance()}")

except InactiveAccountException as e:
    print("EXCEPTION:", e)


# Test 10
print("\n>>> Test 10: PIN Verification")

account9 = Account(1009, "Frank Miller", 40, 1500.0, "Savings")
accounts.append(account9)

print("Account:", end=" ")
display_account(account9)

try:
    account9.setPin(1234)
    print("Setting PIN 1234: SUCCESS")

    account9.withdraw(200.0, 1234)
    print("Withdrawing ₹200.0 with correct PIN: SUCCESS")
    print(f"\nBalance: ₹{account9.getBalance()}")

except (InvalidPinException,
        InvalidAmountException,
        InsufficientBalanceException,
        MinimumBalanceViolationException) as e:
    print("EXCEPTION:", e)


print("Attempting to withdraw ₹100.0 with incorrect PIN (9999)")

try:
    account9.withdraw(100.0, 9999)

except InvalidPinException as e:
    print("EXCEPTION:", e)


print("Attempting to withdraw ₹100.0 without PIN set")

account_without_pin = Account(
    1010, "No Pin User", 25, 1000.0, "Savings"
)

try:
    account_without_pin.withdraw(100.0, 1234)

except InvalidPinException as e:
    print("EXCEPTION:", e)


# Test 11
print("\n>>> Test 11: All Accounts Summary")

for account in accounts:
    display_account(account)


print("=" * 60)
print("TEST COMPLETED!")
print("=" * 60)