# MEDICAL CLINIC ENTRY.

for i in range(3):
    age= int(input("Enter your age :"))
    if age<18:
        print("Go to the :(Pediatrician):")
    elif age<60:
        print("Go to the :(General physician):")
    else:
        print("Go to the :(Senior Consultant):")
