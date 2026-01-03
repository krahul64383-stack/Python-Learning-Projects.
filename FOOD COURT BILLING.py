# FOOD COURT BILLING.

total_income=0
while True:
    item_name=input("Enter item name  'exit':")
    if item_name=="exit":
        break
    price= int(input("Enter price :{item_name}"))
    price=price+(price*0.05)
    qty= int(input("Enter qty :{item_name}"))
    bill=price*qty
    if bill>1000:
        bill=bill-100
        print("OFFER :100 ")
    print(f" TOTAL BILL OF RESTURANT {item_name}:{bill}")
    total_income= total_income+bill

print(f"TOTAL RESTURANT BILL TODAY :{total_income}")
print("---THANK YOU ! VISIT AGAIN ---")
