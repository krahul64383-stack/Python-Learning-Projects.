# RESTURANT BILLING SYSTEM.

order={}
total=0
while True:
    name=input("Enter dish name ('done'):")
    if name=="done":
        break
    cost=int(input(f"{name} cost:"))
    order[name]=cost
    total=total+ cost

print("\n---YOUR RESTURANT BILL---")
for dish in order:
    print(f"{dish}.....{order[dish]}")
print("---------------")
print(f"TOTAL PAYABLE AMOUNT:{total}")
print("---THANK YOU ! VISIT AGAIN---")
