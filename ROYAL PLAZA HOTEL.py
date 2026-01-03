# ROYAL PLAZA HOTEL .

hotel_earnings=0
while True:
    guest_name= input("Enter guest name 'checkout':")
    if guest_name=="checkout":
        break
    room_price=int(input(f"Enter room price {guest_name}:"))
    days= int(input(f" How many days ? :")) 
    breakfast=input("Need breakfast? (yes/no):")
    if breakfast=="yes":
        room_price=room_price+500   
    
    room_price =room_price+(room_price*0.12)
    total_bill=room_price*days               

    if days>5:
        total_bill =total_bill-1000
        
        print("APPLIED DISCOUNT:1000")

    print("TOTAL BILL{guest_name}:{total-bill}")
    hotel_earnings= hotel_earnings+total_bill

print(f"TOTAL HOTEL EARNINGS TODAY:{hotel_earnings}")
print("THANK YOU FOR VISITING ROYAL PLAZA HOTEL ")
