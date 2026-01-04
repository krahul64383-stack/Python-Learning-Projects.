# SMART DELIVERY FEE FUNCTION

def calculate_delivery(distance):
    if distance<=2:
        return "Free"
    elif distance<=5:
        return 20
    else:
        return 50
for i in range(3):
    dist=int(input("How much distance(km):"))
    result=calculate_delivery(dist)
    print(f"Your delivery charge :{result}")
