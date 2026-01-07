#STUDENT GRADE & ATTENDANCE REPORT.

scores=[50]
for i in range(3):
    last_scores=scores[-1]
    print(f"\n--TEST {i+1}--")
    choose=input("Enter points (got/cut):")
    marks=int(input("Enter marks:"))
    if choose=="got":
        new_scores=last_scores+marks
    else:
        new_scores=last_scores-marks
    if new_scores>90:
        print("EXCELLENT PERFORMANCE!")
    scores.append(new_scores)
    print(f"CURRENT SCORE: {new_scores}")
final_diff=scores[-1]-scores[0]
print("FINAL SCORE")
print("\n"+"="*20)
print(f" SCORES LIST:{scores}")
print(f"TOTAL SCORE DIFF.: {final_diff}")
