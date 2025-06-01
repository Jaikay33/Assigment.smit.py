#Task 9   Done
#     ***Paackage Weight Checker (Shipping App)***

print("***Paackage Weight Checker (Shipping App)***")

package_weight = int(input("Enter the weight of package:"))
price_package_weight = 10

if package_weight <=1:
    print(f"Light package price_package_weight = $5 ")
elif (package_weight <=5 and package_weight >=1):
    print(f"Regular Package price_package_weight = $10")
elif package_weight >=5:
    if package_weight >=20:
        print("Deny Shipment")
    elif package_weight >=5:
        print(f"Heavy Package weight Price of package_weight = $15")

 