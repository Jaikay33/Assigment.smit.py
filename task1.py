# Task 1:
#       ***Simple shopping cart total calculator***  

print("***Simple shopping cart total calculator***")

def shopping_cart_total():
    total = 0.0

    print("Enter the prices of items one by one.")
    print("Type 'done' when you are finished.\n")

    while True:
        user_input = input("Enter item price: ")

        if user_input.lower() == 'done':
            break

        try:
            price = float(user_input)
            if price > 1000:
                discount = price * 0.10
                discount -= price
                print(f"10% discount applied. Discounted price: $v{price:.2f}")
            total += price
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")

    print(f"\nFinal total amount: ${total:.2f}")


# Run the calculator
shopping_cart_total()


