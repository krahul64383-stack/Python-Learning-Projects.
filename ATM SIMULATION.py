# ATM SIMULATION GAME.

Balance = 2500
choice = 0
print("_____Welcome To Python ATM_____")
while choice!= 3:
    print("\n 1. Check Balance")
    print("\n 2. Withdraw money")
    print(" 3. Exit")

    choice=int(input("\n Choose your Choice(1-3):"))

    if choice==1:
        print(f"Your current Balance:{Balance}")
    elif choice==2:
        Amount=int(input("Enter Rupees:"))
        if Amount<=Balance:
            Balance= Balance-Amount
            print(f"{Amount}withdraw your rupees. New Balance:{Balance}")
        else:
            print("Money is not sufficient")
            
    elif choice==3:
         print("Thank You ! Visit Again.")
    else:
        print("Wrong choice ! Press 1,2 and 3.")

