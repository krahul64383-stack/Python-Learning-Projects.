#WHILE LOOP.
#NUMBER GUSSING GAME.

secret_number=7
user_guess=0
while user_guess!=secret_number:
    user_guess=int(input("Enter Guess Number (1-10):"))
    if user_guess==secret_number:
        print("CONGRATULATION! YOU GOT RIGHT NUMBER")
    else:
        print("WRONG ANSWER! TRY AGAIN")
print("THE END")
