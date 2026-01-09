def electricity_bill(name,units):
    if units<=100:
        rate=5
    elif units<300:
        rate=8
    else:
        rate=12
    total_bill=units*rate
    if total_bill>2000:
        total_bill=total_bill+200
        
    else:
        tax=0
    return f"HELLO! {name} YOUR ELECTRICITY BILL: {total_bill}"
print(electricity_bill("Rahul",286))
             
