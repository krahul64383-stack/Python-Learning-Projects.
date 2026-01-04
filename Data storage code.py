# Data Storage Code (Loan Memory)

all_results=[]
def loan_check(salary,credit_score):
    if salary>=50000:
        if credit_score>=700:
            status="Approved"
            intrest="8%"
        else:
            status="Approved"
            intrest="12%"
    else:
        status="Rejected"
        intrest="N/A"
    return status,intrest

for i in range(3):
    name=input("Enter name:")
    sal=int(input("Enter salary:"))
    score=int(input("Enter score:"))

    status,intrest = loan_check(sal,score)
    all_results.append(status)

    print(f"Cutomer : {name},Status : {status},Intrest : {intrest}")

print("\n--FINAL DAY MEMORY REPORT--")
print("All decision record :",all_results)
