# THE RENT AND EXPENSE MANAGER( KHRCHA HISAB GAME).

pocket_money = 10000
choice = 0

print("*******Welcome To Expense Manager******")
while choice!= 3:
    print(f"\n Your remaining money:{pocket_money}")
    print(" 1. Add Expense")
    print(" 2. Check Status")
    print(" 3. Exit.")

    choice=int(input("Choose option(1-3):"))

    if choice==1:
        spent= int(input("spent money"))
        if spent<=pocket_money:
            pocket_money= pocket_money -spent
            print(f"ok,{spent} Done.")
        else:
            print("Out of capacity ! is not sufficient money.")
    elif choice==2:
        if pocket_money>2000:
            print("Now You are able to spent money.")
        else:
            print("Caution! money has low.")
    elif choice==3:
        print("Your money is too low means Empty! BYE.")
                   
