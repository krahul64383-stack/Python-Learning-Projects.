# SHOP STOCK MANAGER.

stock_history=[100]
def check_stock(current_stock,order_qty):
    if order_qty<=current_stock:
        status="Available"
        remaining=current_stock-order_qty
    else:
        status="No stock"
        remaining=current_stock
    return status,remaining
for i in range(3):
    name=input("Enter customer name:")
    qty=int(input("How many items?:"))

    last_stock=stock_history[-1]
    status,updated_stock=check_stock(last_stock,qty)

    stock_history.append(updated_stock)

    print(f"Hello {name} , {status} ,Remaining stock : {updated_stock}")

print("Stock Update History:" , stock_history)
