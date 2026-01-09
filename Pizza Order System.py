#Pizza Order System.

def pizza_deliver(size,is_student,has_coupon):
    if size=="small":
        base_price=200
    elif size=="medium":
        base_price=400
    else:
        base_price=600
    if is_student==True and has_coupon==True:
        discount=100
    elif is_student==True:
        discount=50
    else:
         discount=0
    final_bill=base_price-discount
    return f"FINAL BILL {final_bill}"
print(pizza_deliver("medium",False,True))
             
