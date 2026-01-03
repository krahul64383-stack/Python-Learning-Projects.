#FRESH & JUICY CORNER.

shop_total =0
while True:
    juice_name=input("Enter juice name 'quit' :")
    if juice_name == "quit":
        break
    juice_price= int(input(f" {juice_name} price:"))
    qty = int(input("glasses? :"))
    topping =input("Extra topping? (yes/no):")
    if topping=="yes":
        juice_price=juice_price+10

    current_bill=juice_price*qty
    shop_total=shop_total+ current_bill

print(f" FINAL FRESH & JUICY CORNER BILL : {shop_total}")
print("-------------")
print("--THANK YOU ! VISIT AGAIN ")
