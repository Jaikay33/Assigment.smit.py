#Task 4 Done
#     ***Call Center Wait Time Estimeter***

print("***Call Center Wait Time Estimeter***")

people_ahead = int(input("How many people are ahead of you in the call center queue? "))

# Check if there is anyone ahead
if people_ahead == 0:
    print("You're next!")
else:
    print("Estimating wait time...")
    total_wait = 0
    
    for person in range(1, people_ahead + 1):
        print(f"Serving person {person}...")
        total_wait += 3  # Each person takes 3 minutes
    
    print(f"Estimated wait time: {total_wait} minutes.")