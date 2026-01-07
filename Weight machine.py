#WEIGHT GAIN OR LOSS IN GYM.

weight_history=[80]
for weight in range(4):
    last_weight=weight_history[-1]
    print(f"\n--WEEK {weight+1}--")
    choice=input("Enter Your Choice (gain/loss):")
    amount=int(input("Enter amount in kg :"))
    if choice=="loss":
        new_weight=last_weight-amount
    else:
        new_weight=last_weight+amount
    if new_weight<=75:
        print("CONGRATULATION!TARGET ACHIEVED!")
    weight_history.append(new_weight)
    print(f"CURRENT WEIGHT:{new_weight}")
final_diff=weight_history[-1]-weight_history[0]
print("FINAL REPORT OF YOUR WEIGHT")
print("\n"+"="*20)
print(f"WEIGHT HISTORY LIST:{weight_history}")

print(f"TOTAL WEIGHT DIFF.: {final_diff}")
        
