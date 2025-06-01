#Task 6  Done
#      "***Movie Ticket Pricing***


print("***Movie Ticket Pricing***")
print("Enter today Day")
print("Enter your Age")

day = input("Enter today Day:")
age = float(input("Enter your Age:"))
ticket = 10

if age <=5:
    print(f"{ticket == 00}:Ticket = Free")
elif age >=60:
    print(f"{ticket == 5}:Ticket = $5")
elif day == "Monday":
    print(f"{ticket == 10}:Ticket = $10")
elif day == "Tuesday":
    print(f"{ticket == 10}:Ticket = $10")
elif day == "Wednesday":
    print(f"{ticket == 10}:Ticket = $10")
elif day == "Thursday":
    print(f"{ticket == 10}:Ticket = $10")
elif day == "Friday":
    print(f"{ticket == 10}:Ticket = $10")
elif day == "Saturday":
    print(f"{ticket == 12}:Ticket = $12")
elif day == "Sunday":
    print(f"{ticket == 12}:Ticket = $12")
else:
    print("Wrong input please enter valid input")

 