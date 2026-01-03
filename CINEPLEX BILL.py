# CINEPLEX BILLING SYSTEM.

total_collection=0
while True:
    movie_name=input("Enter movie name 'stop':")
    if movie_name=="stop":
        break
    ticket_price=int(input("Ticket price :{movie_name}"))
    seats= int(input("Seats :{movie_name}"))
    bill=ticket_price*seats
    night_show= input("Need night show (yes/no):")
    if night_show=="yes":
        bill=bill+(50*seats)
    bill=bill+(bill*0.18)
    if seats>5:
        bill=bill-200
        print("OFFER :200")
    print(f"TOTAL BILL OF CINEPLEX {movie_name}:{bill}")
    total_collection=total_collection +bill

print(f"TOTAL CINEPLEX BILL TODAY :{total_collection}")
print("--THANK YOU! ")
