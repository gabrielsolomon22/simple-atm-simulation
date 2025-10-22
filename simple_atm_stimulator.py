pin = "123456"
account_balance = float(100000)
pin_request = input("Hello User, Kindly enter your pin: ")
if pin_request == pin:
    print("PIN confirmed")
    print("""1 - withdraw
2 - make deposits
3 - check balance
Choose an option""")
    option = input("1, 2 or 3: ")
    if option == "1":
        amount = float(input("Enter amount: "))
        if amount <= account_balance - 100:
            print("$",amount)
            new_account_balance = account_balance - amount
            print(f"Withdrawal successful. New balance: ${new_account_balance}")
        else:
            print("insufficient funds. Minimum balance of $100 required")
    elif option == "2":
        amount_1 = float(input("Enter amount: "))
        new_account_balance_1 = account_balance + amount_1
        print(f"Deposit successful. New balance: ${new_account_balance_1}")
    elif option == "3":
        print("$",account_balance)
    else:
        print("invalid option, kindly try again and enter from the within option: 1, 2 or 3.")
else:
    print("invalid pin")
