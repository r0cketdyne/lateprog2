# Programming Assignment 2 -- File: Prog2.py
# MATTHEW STEPHENSON 2/15/2024
## This program assists a healthcare practitioner determing what patients can donate at blood
###########################################################
usr_type = input("If you have data related to the patient's blood type, please put it in\n")
print(usr_type)

# If your blood type is O+ or O-
if usr_type in ('O+', 'O-'):
    print('the patient can give us Double Red Cells && Whole Blood ')

# If your blood type is A+
elif usr_type == 'A+':
    print('the patient can donate Plasma && Platelets')

# If your blood type is A-
elif usr_type == 'A-':
    print('the patient can donate both Double Red Cells && Platelets. Yay')

# If your blood type is B+
elif usr_type == 'B+':
    print('the patient can donate both Plasma && Platelets')

# If your blood type is B-
elif usr_type == 'B-':
    print("the patient can donate both Double Red Cells && Platelets")

# If your blood type is AB+ or AB-
elif usr_type in ('AB+', 'AB-'):
    print("Well well well... seems like they can donate both Plasma and Platelets")

#elif statements weren't needed. but at the last moment decided this implementation made sense
#if you want to see original implementation. please ask for a link to the github repo
#via discord at any time. commit history is there
#elif wasn't explicityle necessary.
#some of the comments were used as a kind of wireframe to piece together this 
#solution. a translation of the flow chart used in the lectures.
