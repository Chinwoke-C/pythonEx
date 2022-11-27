def calculate_bal(user_balance, user_total_charges, user_credit):
    new_balance = (balance + total_charges) - credit
    if new_balance < allowed_credit:
        print("credit limit exceeded")
    elif new_balance > allowed_credit:
        print("okay to pay")


if __name__ == '__main__':
    allowed_credit = 10000
    acct_no = int(input("Enter account no: "))
    balance = float(input("Enter account balance: "))
    total_charges = float(input("Enter total charge of all items"))
    credit = float(input("Enter total credit applied to customer account"))
    print(f'The status of customer account: {acct_no}')
    calculate_bal(balance, total_charges, credit)
