#PETROL EXPENSE TRACKER.

balance=[2000]
for balances in range(4):
    last_balance=balance[-1]
    print(f"\n--MONTH {balances+1}--")
    choice=input("Enter Your Choice (petrol/wallet):")
    amount=int(input("Enter money:"))
    if choice=="petrol":
        new_balance=last_balance-amount
    else:
        new_balance=last_balance+amount
    if new_balance<200:
        print("LOW BALANCE!PLEASE ADD MONEY TO WALLET")
    balance.append(new_balance)
    print(f"CURRENT BALANCE: {new_balance}")
final_diff=balance[-1]-balance[0]
print("TOTAL BALANCE OF YOUR WALLET")
print("\n"+"="*20)
print(f"BALANCE LIST:{balance}")
print(f"TOTAL BALANCE DIFF.: {final_diff}")
