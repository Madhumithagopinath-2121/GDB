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
print("ENHANCED ACCOUNT TEST (EXCEPTIONS)")
print("=" * 60)

accounts = []


# --------------------------------------------------
# Test 1: Valid Account Creation
# --------------------------------------------------
print("\n>>> Test 1: Valid Account Creation")

try:
    account1 = Account(1001, "John Doe", 25, 1000.0, "Savings")
    accounts.append(account1)

    print("Account created successfully")
    display_account(account1)

except ValueError as e:
    print("Account creation failed:", e)


# --------------------------------------------------
# Test 2: Invalid Age
# --------------------------------------------------
print("\n>>> Test 2: Invalid Age (under 18)")

print("Creating account with age 16")

try:
    account2 = Account(1002, "Young Kid", 16, 500.0, "Savings")
    accounts.append(account2)

except ValueError as e:
    print("Exception:", e)


# --------------------------------------------------
# Test 3: Invalid Account Type
# --------------------------------------------------
print("\n>>> Test 3: Invalid Account Type")

print('Creating account with type "Invalid"')

try:
    account3 = Account(1003, "Test User", 25, 500.0, "Invalid")
    accounts.append(account3)

except ValueError as e:
    print("Exception:", e)


# --------------------------------------------------
# Test 4: Minimum Balance Enforcement
# --------------------------------------------------
print("\n>>> Test 4: Minimum Balance Enforcement on Creation")

print("Creating Savings account with ₹300 (below minimum)")

try:
    account4 = Account(1004, "Bob Wilson", 25, 300.0, "Savings")
    accounts.append(account4)

except ValueError as e:
    print("Exception:", e)


# --------------------------------------------------
# Test 5: Withdrawal with Minimum Balance
# --------------------------------------------------
print("\n>>> Test 5: Withdrawal with Minimum Balance")

account5 = Account(1005, "Alice Brown", 30, 2000.0, "Current")
account5.setPin(1234)
accounts.append(account5)

print("Initial:", end=" ")
display_account(account5)

# Successful withdrawal
amount = 500.0

try:
    account5.withdraw(amount, 1234)

    print(f"Withdrawing ₹{amount}: SUCCESS")
    print(f"New balance: ₹{account5.getBalance()}")

except Exception as e:
    print("Withdrawal failed:", e)

print("After withdrawal:", end=" ")
display_account(account5)


# Minimum balance violation
amount = 600.0

try:
    account5.withdraw(amount, 1234)

    print(f"Withdrawing ₹{amount}: SUCCESS")

except MinimumBalanceViolationException as e:
    print(
        f"Withdrawing ₹{amount}: FAILED "
        f"(Minimum balance violation)"
    )
    print("Exception:", e)

print(f"Current balance: ₹{account5.getBalance()}")


# --------------------------------------------------
# Test 6: Account Status Management
# --------------------------------------------------
print("\n>>> Test 6: Account Status Management")

account6 = Account(1006, "Charlie Green", 35, 2000.0, "Savings")
accounts.append(account6)

print("Initial:", end=" ")
display_account(account6)

# Close account
try:
    account6.closeAccount()
    print("Closing account: SUCCESS")

except RuntimeError as e:
    print("Closing account failed:", e)

print("After close:", end=" ")
display_account(account6)


# Deposit into closed account
amount = 500.0

try:
    account6.deposit(amount)
    print(f"Depositing ₹{amount} to closed account: SUCCESS")

except InactiveAccountException as e:
    print(
        f"Depositing ₹{amount} to closed account: "
        f"FAILED (Account inactive)"
    )
    print("Exception:", e)


# Reopen account
try:
    account6.reopenAccount()
    print("Reopening account: SUCCESS")

except RuntimeError as e:
    print("Reopening account failed:", e)

print("After reopen:", end=" ")
display_account(account6)


# --------------------------------------------------
# Test 7: PIN Protection
# --------------------------------------------------
print("\n>>> Test 7: PIN Protection")

account7 = Account(1007, "Diana Prince", 28, 1500.0, "Savings")
accounts.append(account7)


# Set PIN
try:
    account7.setPin(1234)
    print("Setting PIN 1234: SUCCESS")

except ValueError as e:
    print("Setting PIN failed:", e)


# Correct PIN
amount = 200.0

try:
    account7.withdraw(amount, 1234)

    print(
        "Withdrawing ₹200.0 with correct PIN (1234): SUCCESS"
    )
    print(f"New balance: ₹{account7.getBalance()}")

except Exception as e:
    print("Withdrawal failed:", e)


# Incorrect PIN
amount = 100.0

try:
    account7.withdraw(amount, 9999)

    print(
        "Withdrawing ₹100.0 with incorrect PIN (9999): SUCCESS"
    )

except InvalidPinException as e:
    print(
        "Withdrawing ₹100.0 with incorrect PIN (9999): "
        "FAILED (Incorrect PIN)"
    )
    print("Exception:", e)


# PIN not set
account_without_pin = Account(
    1008, "No Pin User", 25, 1000.0, "Savings"
)

amount = 100.0

try:
    account_without_pin.withdraw(amount, 1234)

    print(
        "Withdrawing ₹100.0 with PIN not set: SUCCESS"
    )

except InvalidPinException as e:
    print(
        "Withdrawing ₹100.0 with PIN not set: "
        "FAILED (PIN not set)"
    )
    print("Exception:", e)


# --------------------------------------------------
# Test 8: All Accounts Summary
# --------------------------------------------------
print("\n>>> Test 8: All Accounts Summary")

for account in accounts:
    display_account(account)


print("=" * 60)
print("ENHANCED TEST COMPLETED!")
print("=" * 60)