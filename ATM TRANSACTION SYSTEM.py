#ATM TRANSACTION SYSTEM.

for i in range(3):
    amount=int(input("Enter withdraw money :"))
    if amount<500:
        print("Min Withdrawal 500 ")
    elif amount<10000:
        print("Processing....Cash Collected !")
    else:
        print("Limit Exceeded ! Max Limit 10000")
