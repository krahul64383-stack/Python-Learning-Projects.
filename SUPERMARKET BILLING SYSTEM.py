#THE SUPER MARKET BILLING SYSTEM.

bill_data={}
while True:
    name=input("Enter Product name ('pay'):")
    if name=="pay":
        break
    cost= int(input("Enter price:"))
    bill_data[name]=cost

print("\n---Final bill---")
print(bill_data)     
