#EMPLOYEE BONUS TRACKER.

employe_data={}
def calculate_bonus(name,salary):
    employe_data["Name"]=name
    employe_data["Salary"]=salary
    if salary>50000:
        employe_data["bonus"]=5000
    else:
        employe_data["bonus"]=2000

name=input("Enter your name:")
salary=int(input("Enter your salary:"))
calculate_bonus(name,salary)
print(employe_data)
