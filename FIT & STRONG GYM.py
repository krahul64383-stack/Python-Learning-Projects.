#FIT & STRONG GYM.

gym_revenue = 0
while True:
    name=input("Enter customer name 'close':")
    if name == "close":
        break
    fee = int(input(f"Enter monthly fee {name} :"))
    months = int(input(f"How many months {name}? :"))
    trainer =input("Need personal trainer? (yes/no):")
    if trainer=="yes":
        fee=fee+1000
        print("Trainer Added:+1000/month")

    bill=fee*months
    if months>6:
        bill=bill-1500
        print("APPLIED DISCOUNT :1500")

    print("TOTAL BILL{name}:{bill}")
    gym_revenue = gym_revenue+bill

print("_"*30)
print(f"TOTAL GYM REVENUE TODAY:{gym_revenue}")
print("FIT & STRONG GYM-STAY HEALTHY")
