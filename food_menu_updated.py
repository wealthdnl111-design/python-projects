print("===== FOOD MENU =====")
print("1. Jollof Rice - ₦2,000")
print("2. Fried Rice - ₦2,500")
print("3. Beans - ₦1,500")

choice = input("Enter food choice (1-3): ")
quantity = int(input("Enter quantity: "))

match choice:
    case "1":
        food_name = "Jollof Rice"
        price = 2000
    case "2":
        food_name = "Fried Rice"
        price = 2500
    case "3":
        food_name = "Beans"
        price = 1500
    case _:
        food_name = None
        price = 0

if food_name:
    total = price * quantity
    print(f"You ordered {quantity} plate(s) of {food_name}.")
    print(f"Total = ₦{total:,}")
else:
    print("Invalid choice.")