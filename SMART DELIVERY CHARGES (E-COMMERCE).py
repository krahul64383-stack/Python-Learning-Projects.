# SMART DELIVERY CHARGES (E- COMMERCE).

for i in range(3):
    distance=int(input("Enter distance (km):"))
    price= int(input("Enter price (rs):"))
    if price>1000:
        print("Free")
    elif distance<5:
        print(" Your Delivery Charges Free")
    elif distance<15:
        print(" Your Delivery Charges (50)")
    else:
        print("Your Delivery Charges (100)")
    
    
