#Task 07  Done
#      ***ATM Withdrawl Simulator***

print ("***ATM Balance Simulator***")

balance = 1000
amount = int(input("Enter your Amount: "))

if (amount%100 != 0):
     print("Error Insuffecient balance")
elif (amount > balance):
        print("Deny")
elif amount - balance:
        print("Payment Approved ")
        print ("current Balance:" )
        print (balance - amount) 

        