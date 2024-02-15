usr_type = input("mf what is your blood type. if you don't know check and put the data in\n")
print(usr_type)
#Problem Statement
#A specialty donation allows you to give more of what patients need in just one appointment. #During
#your donation, one part of your blood is collected, while the rest is returned to your body. #This process
#is called apheresis (AY-fur-EE-sis).

#In this decision problem, you are to determine the best types of donation for a particular #blood type
#based on the following table. You must also check if any invalid blood types are entered at the #user
#prompt.

#If your blood type is O+ or O-
#Double Red Cells
#Whole Blood
if usr_type == ('O+' or 'O-'):
    print('the patient can give us Double Red Cells && Whole Blood ')
#If your blood type is A+
if usr_type == ('A+'):
    print('the patient can donate Plasma && Platelets')
#Plasma
#Platelets

#If your blood type is A-
if usr_type == ('A-'):
    print('the patient can donate both Double Red Cells && Platelets. Yay')
#Double Red Cells
#Platelets

#If your blood type is B+
if usr_type == ('B+'):
    print('the patient can donate both Plasma && Platelets')
#Plasma
#Platelets

#If your blood type is B-
if usr_type == ('B-'):
    print("the patient can donate both Double Red Cells && Platelets")
#Double Red Cells
#Platelets

#If your blood type is AB+ or AB-
if usr_type == ('AB+' or 'AB-'):
    print("Well well well... seems like they can donate both Plasma and Platelets")
#Plasma
#Platelets
