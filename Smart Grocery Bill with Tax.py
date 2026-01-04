# SMART GROCERY BILL WITH TAX.

def final_price(item_price):
    if item_price>=500:
        tax=item_price * 0.18
    else:
        tax = item_price * 0.05

    total = item_price + tax
    return tax,total
for i in range(3):
    price= float(input("Enter price :"))
    tax,total= final_price(price)
    print(f"Price :{price}, Tax : {tax}, Total : {total}")
