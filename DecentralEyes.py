## Kritik Kaushal
## TKS
## September 11, 2018
## DecentralEyes
## For Demo only


import random

fname_list=["Janette", "Patrice", "Zoraida", "Melodie", "Joyce", "Elmira", "Paul", "Jada", "Ricardo", "Landon", "Kasha", "Winter", "Victoria", "Nohemi", "Viva", "Mellissa", "Jama", "Quinn", "Damon", "Jahseh", "Chante", "Edda", "Julieta", "Carlos", "Shay", "Marlin", "Adelina", "Dorsey", "Myriam", "Jacquelynn"]    #First Names
lname_list=["Smith", "Welbeck", "Wilshere", "Kaushal", "Tan", "Jain", "Bhanji", "Ma", "Kane", "Sturridge", "Jones", "Roberts", "Sharma"]


            
cred_score = random.randint(1, 100) #Gives a random score out of 100 for how good a citizen's credit score is
crime_score = random.randint(1,100) #No crimes=100. Each crime (even small ones) takes away something
edu_score = random.randint(1, 100) #More education=greater score
income_score = random.randint(1, 100) #Higher income=more GDP for country=higher score
#aok_score = random.randint(1,100) #Acts of Kindness score, provided via camera surveilance
finance_score = random.randint(1, 100) #pay bills, insurance, clear debts on time

human_score = (cred_score + crime_score + edu_score + income_score + finance_score)/5
token = (human_score/20)
token = round(token, 2)

phone_num = random.randint(4160000000, 4169999999)
ID = random.randint(1, 999999)
age = random.randint(10, 80)

print("Name: ", random.choice(fname_list), random.choice(lname_list))
print("Age: ", age)
print("Phone Number: ", phone_num)
print("DecentralEyes ID: ", ID)
print(" ")
print("Your score is", human_score)
print("You get", token, "tokens")

"""
Created for ShyftHACK
"""

