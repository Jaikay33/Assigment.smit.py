#Task 2 Done
#        ***Age Group classifier***

print("***Age Group classifier***")

age = int(input("Enter your Age:"))

if age <=12:
    print("Child")
elif age >= 13 and age <19:
    print("Teen Ager")
elif age <= 64 and age >=19:
    print("Adult")
else:
    print("senior")
