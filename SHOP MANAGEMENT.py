'''
#SHOP MANAGEMENT.

stock_history=[100]
for stock in range(3):
    last_stock=stock_history[-1]
    choice=input("Enter Your Choice: (Sell/Buy):")
    if choice=="Sell":
        new_stock=int(input("Enter Sell ?:"))
        total_stock=last_stock-new_stock
    else:
        new_stock=int(input("Enter Buy ?:"))
        total_stock=last_stock+new_stock
    stock_history.append(total_stock)

print(f"CURRENT STOCK: {total_stock}")
print("\n"+ "="*20)
print("FINAL STOCK IN SHOP ")
print(f" TOTAL STOCK: {stock_history[-1]-stock_history[0]}")
'''
#SHOP MANAGEMENT.

stock_history=[100]
growth_log=[0]
for stock in range(3):
    last_stock=stock_history[-1]
    print(f"\n--Transaction {stock+1}--")
    choice=input("Enter Your Choice: (sell/buy):")
    if choice=="sell":
        new_stock=int(input("Enter Sell ?:"))
        total_stock=last_stock-new_stock
    else:
        new_stock=int(input("Enter buy ?:"))
        total_stock=last_stock+new_stock
    current_growth=total_stock-stock_history[0]
    stock_history.append(total_stock)
    growth_log.append(current_growth)
    print(f"Current Stock:{total_stock}")
print("\n" + "=" *20)
print("FINAL STOCK AND GROWTH IN STOCK")
final_diff=stock_history[-1]-stock_history[0]
if final_diff>0:
    status="TOTAL BUY"
    val=final_diff
elif final_diff<0:
    status="TOTAL SELL"
    val=abs(final_diff)

else:
    status="NO CHANGE"
    val=0
print(f"RESULT: {status} {val}")
print(f"FULL GROWTH: {growth_log}")
print("="*20)














    



























