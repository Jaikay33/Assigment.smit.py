#Tasl 05 Done 
#       ***Fuel Cost Estimator***

print("***Fuel Cost Estimator***")
distance = int(input("Enter Distance: "))
fuel_average = int(input("Enter fuel average of your car: "))
fuel_price = int(input("Enter Fuel price: "))
Total_coast = (fuel_price / fuel_average * distance) 
total_fuel = (Total_coast / fuel_price)
print("Total Coast: ")
print(Total_coast)
print("Total fuel you want: ")
print(total_fuel)
if distance == 500:
    print("Check Tyre Pressure & Refulling Midway")

