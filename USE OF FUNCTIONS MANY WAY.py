#FUNCTIONS USE.

def grade_tracker():
    scores=[50]
    for i in range(3):
        last_scores=scores[-1]
        print(f"\n--TEST {i+1}--")
        choose=input("Enter Points (got/cut):")
        marks=int(input("Enter Marks:"))
        if choose=="got":
            new_scores=last_scores+marks
        else:
            new_scores=last_scores-marks
        scores.append(new_scores)
        print(f"CURRENT SCORES: {new_scores}")
    print(f" FINAL SCORES LIST: {scores}")
grade_tracker()


#FUNCTION WITH ARGUMENT.

def grade_tracker(start_point):
    scores=[start_point]
    for i in range(3):
        last_scores=scores[-1]
        print(f"\n--TEST {i+1}")
        choose=input("Enter Points (got/cut):")
        marks=int(input("Enter Marks:"))
        if choose=="got":
            new_scores=last_scores+marks
        else:
            new_scores=last_scores-marks
        scores.append(new_scores)
        print(f"CURRENT SCORES: {new_scores}")
    print(f"\n FINAL SCORE LIST: {scores}")
grade_tracker(20)

#MULTIPLE ARGUMENTS.

def grade_tracker(name,start_point):
       scores=[start_point]
       print(f"\n--REPORT FOR STUDENT:{name}--")
       for i in range(2):
           marks=int(input("Enter marks {name}:"))
           scores.append(scores[-1]+marks)
       print(f"FINAL HISTORY {name}: {scores}")
grade_tracker("Rahul",83)
grade_tracker("Sweety",84)


def report_card(name,score):
    print(f"STUDENT NAME: {name}")
    print(f"STUDENT SCORE: {score}")
report_card("Rahul",76)
report_card("Sweety",78)
              
# RETURN STATEMENT.

def add(a,b):
    result=a+b
    return result
total=add(10,30)
print(total+5)

def total_hisab(chini,chai):
    sum=chini+chai
    return sum
total=total_hisab(10,20)
print(f"TOTAL KHRCHA: {total}")

def calculater(a,b):
    sum =a+b
    return sum
ans=calculater(5,5)
print(f"TOTAL ANSWER: {ans}")

