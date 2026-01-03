# THE SMART ELECTRICITY BIL CALCULATOR.

for i in range(3):
    units= int(input("enter unit :"))
    if units<100:
        price= units * 5 
    elif units<200:
        price= units * 8 
    else:
        price= units * 12 

    print(f"ALL HOUSE :{units} Total Bill :{price}")
