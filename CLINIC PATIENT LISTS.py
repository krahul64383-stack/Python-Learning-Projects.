#CITY CLINIC PATIENT LIST.

patients={}
total_patients=0
while True:
    name=input("Enter Patient name ('exit'):")
    if name=="exit":
        break
    disease=input(f"{name}....diseas:")
    patients[name]=disease
    total_patients=total_patients+1

print("\n-----PATIENTS LIST---")
for name in patients:
    print(f"{name}.....{patients[name]}")
print("----------")
print(f" TOTAL PATIENTS LIST:{total_patients}")
print("---WISH YOU ALWAYS HAPPY AND HEALTHY---")
