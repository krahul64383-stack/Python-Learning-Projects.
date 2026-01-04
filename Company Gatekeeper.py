# COMPANY GATEKEEPER.

def check_security(job_role):
    if job_role=="CEO":
        access= "high"
        status="allowed"
    elif job_role=="Staff":
        access="medium"
        status="allowed"
    else:
        access="zero"
        status="blocked"
    return access,status

for i in range(3):
    name=input("Enter employee name :")
    role=input("Enter your role :")
    access,status=check_security(role)
    print(f"EMPLOYEE : {name}, Access: {access}, Status: {status}")
