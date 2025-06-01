#Task 08 Done
#      ***Simple Survey Tally System***

 #vote counters
vote_A = 0
vote_B = 0
vote_C = 0

print("Simple Survey Tally System")
print("Vote for one of the options: A, B, or C")
print("Type 'stop' to finish voting\n")

while True:
    vote = input("Enter your vote (A, B, or C): ").strip().upper()
    
    if vote == "STOP":
        break
    elif vote == "A":
        vote_A += 1
    elif vote == "B":
        vote_B += 1
    elif vote == "C":
        vote_C += 1
    else:
        print("Invalid vote. Please enter A, B, C, or 'stop'.")

# Display results
print("\nVoting Results:")
print(f"Option A: {vote_A} votes")
print(f"Option B: {vote_B} votes")
print(f"Option C: {vote_C} votes")

# Know the winner
votes = {"A": vote_A, "B": vote_B, "C": vote_C}
max_votes = max(votes.values())
winners = [option for option, count in votes.items() if count == max_votes]

if len(winners) == 1:
    print(f"\nThe winner is Option {winners[0]}!")
else:
    print("\nIt's a tie between: " + ", ".join(winners))
