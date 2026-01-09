#GYM ENTRY SYSTEM(USE OF AND)

def gym_entry(is_member,has_membership_card):
    if is_member==True and has_membership_card==True:
        return "ACCESS GRANTED"
    
    else:
        return "ACCESS DENIED"
print(gym_entry(True,True))
              
