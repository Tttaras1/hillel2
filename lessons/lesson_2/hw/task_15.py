balance = 10000
amount = 2500
is_card_active = True
is_blocked = False

withdrawal_limit = 5000
is_operation_valid = True

if not is_card_active:
    is_operation_valid = False
    print("Your card is not active")
elif is_blocked:
    is_operation_valid = False
    print("Your card is blocked")
elif amount <= 0:
    is_operation_valid = False
    print("Withdrawal amount invalid")
elif amount > withdrawal_limit:
    is_operation_valid = False
    print(f"Withdrawal amout exceeds {withdrawal_limit} amount")
elif amount > balance:
    is_operation_valid = False
    print(f"Withdrawal amout exceeds your balance")

if is_operation_valid:
    balance = balance - amount
    print(f"Success, remaining balance: {balance}")
