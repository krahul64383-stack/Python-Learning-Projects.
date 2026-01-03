# ZIPPY CAR RENTAL.

total_rent_income=0
while True:
    name=input("Enter customer name 'stop':")
    if name=="stop":
        break
    car_type=input("Enter car type..{name}(SUV,SEDAN):")
    daily_rent=int(input(f" How much one day rent? {car_type} :"))
    days=int(input(f" How many days ?:"))
    daily_rent=daily_rent+(daily_rent*0.10)
    bill=daily_rent*days
    full_tank=input("Need full tank (yes/no):")
    if full_tank=="yes":
        bill=bill+3000
    if days>7:
        bill=bill-2000
        print("APPLIED DISCOUNT:2000")
        
    print(f"customer:{name} car:{car_type}")
    print(f"TOTAL RENT BILL {name}:{bill}")
    total_rent_income=total_rent_income+bill

    
print(f"--TOTAL RENT INCOME TODAY:{total_rent_income}")
print("--THANK YOU !--")
