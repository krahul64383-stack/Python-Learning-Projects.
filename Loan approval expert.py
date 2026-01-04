# LOAN APPROVAL EXPERT.

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
    name= input("Enter customer name :")
    sal=int(input("Enter your salary :"))
    score=int(input("Enter your score :"))
    status,intrest=loan_check(sal,score)
    print(f"Customer : {name},Loan : {status},Intrest Rate : {intrest}")
