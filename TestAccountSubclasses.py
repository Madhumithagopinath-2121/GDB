from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from AccountException import AccountException


def display_account(account):

    print(
        f"Account #{account.getAccountNumber()} | "
        f"{account.getName()} | "
        f"{account.getAccountType()} | "
        f"₹{account.getBalance()} | "
        f"{account.getStatus()}"
    )


print("=" * 70)
print("ACTIVITY 8 - ACCOUNT SUBCLASS TEST")
print("=" * 70)

accounts = []


# ============================================================
# TEST 1: CREATING ACCOUNTS
# ============================================================

print("\n>>> Test 1: Creating Accounts")

try:

    savings1 = SavingsAccount(
        1001,
        "John Doe",
        25,
        1000.0
    )

    current1 = CurrentAccount(
        1002,
        "Alice Brown",
        30,
        2000.0
    )

    accounts.append(savings1)
    accounts.append(current1)

    print("Savings Account created successfully")
    display_account(savings1)

    print("Current Account created successfully")
    display_account(current1)

except Exception as e:
    print("EXCEPTION:", e)


# ============================================================
# TEST 2: ACCOUNT TYPE AND MINIMUM BALANCE
# ============================================================

print("\n>>> Test 2: Account Type and Minimum Balance")

print(
    savings1.getAccountType(),
    "Minimum Balance: ₹",
    savings1.getMinimumBalance()
)

print(
    current1.getAccountType(),
    "Minimum Balance: ₹",
    current1.getMinimumBalance()
)


# ============================================================
# TEST 3: SAVINGS INTEREST
# ============================================================

print("\n>>> Test 3: Savings Account Interest")

try:

    interest = savings1.calculateInterest(2)

    print("Balance: ₹", savings1.getBalance())
    print("Interest Rate:", savings1.getInterestRate(), "%")
    print("Interest for 2 years: ₹", interest)

except ValueError as e:
    print("EXCEPTION:", e)


# ============================================================
# TEST 4: CURRENT ACCOUNT OVERDRAFT
# ============================================================

print("\n>>> Test 4: Current Account Overdraft")

try:

    current1.setPin(1234)

    print("Initial Balance: ₹", current1.getBalance())
    print("Overdraft Limit: ₹", current1.getOverdraftLimit())

    current1.withdraw(1500.0, 1234)

    print("After withdrawing ₹1500:")
    print("Balance: ₹", current1.getBalance())
    print("Overdraft Used: ₹", current1.getOverdraftUsed())
    print("Available Overdraft: ₹", current1.getAvailableOverdraft())
    print("Using Overdraft:", current1.isUsingOverdraft())

    current1.repayOverdraft(500.0)

    print("\nAfter repaying ₹500:")
    print("Balance: ₹", current1.getBalance())
    print("Overdraft Used: ₹", current1.getOverdraftUsed())

except AccountException as e:
    print("EXCEPTION:", e)


# ============================================================
# TEST 5: POLYMORPHISM
# ============================================================

print("\n>>> Test 5: Polymorphism")

for account in accounts:

    print(
        "Account #",
        account.getAccountNumber(),
        "| Type:",
        account.getAccountType(),
        "| Balance: ₹",
        account.getBalance()
    )


# ============================================================
# TEST 6: INVALID ACCOUNT CREATION
# ============================================================

print("\n>>> Test 6: Invalid Account Creation")

try:

    invalid_savings = SavingsAccount(
        1003,
        "Young User",
        16,
        500.0
    )

except ValueError as e:

    print("Invalid Age:", e)


try:

    invalid_current = CurrentAccount(
        1004,
        "Low Balance User",
        25,
        500.0
    )

except ValueError as e:

    print("Invalid Balance:", e)


# ============================================================
# TEST 7: SAVINGS PIN AND OPERATIONS
# ============================================================

print("\n>>> Test 7: Savings Account PIN and Operations")

try:

    savings2 = SavingsAccount(
        1005,
        "Bob Wilson",
        35,
        2000.0
    )

    savings2.setPin(1234)

    print("Initial Balance: ₹", savings2.getBalance())

    savings2.deposit(500.0)

    print("After deposit ₹500: ₹", savings2.getBalance())

    savings2.withdraw(300.0, 1234)

    print("After withdrawal ₹300: ₹", savings2.getBalance())

    accounts.append(savings2)

except AccountException as e:

    print("EXCEPTION:", e)


# ============================================================
# TEST 8: CURRENT ACCOUNT ACTIVE STATUS
# ============================================================

print("\n>>> Test 8: Current Account Active Status")

try:

    current2 = CurrentAccount(
        1006,
        "Charlie Green",
        40,
        3000.0
    )

    current2.setPin(1234)

    print("Initial Status:", current2.getStatus())

    current2.closeAccount()

    print("After closing:", current2.getStatus())

    try:

        current2.deposit(100.0)

    except AccountException as e:

        print("Deposit on closed account:", e)

    current2.reopenAccount()

    print("After reopening:", current2.getStatus())

    current2.deposit(100.0)

    print(
        "After deposit ₹100:",
        current2.getBalance()
    )

    accounts.append(current2)

except Exception as e:

    print("EXCEPTION:", e)


# ============================================================
# TEST 9: ALL ACCOUNTS SUMMARY
# ============================================================

print("\n>>> Test 9: All Accounts Summary")

print("-" * 70)

for account in accounts:

    display_account(account)

print("-" * 70)


print("\n" + "=" * 70)
print("ACTIVITY 8 TEST COMPLETED!")
print("=" * 70)