print("===== FOOD MENU =====")
print("1. Jollof Rice")
print("2. Fried Rice")
print("3. Beans")
print("4. Yam")
print("5. Exit")

choice = input("Select an option (1-5): ")

match choice:
    case "1":
        print("You selected Jollof Rice.")
    case "2":
        print("You selected Fried Rice.")
    case "3":
        print("You selected Beans.")
    case "4":
        print("You selected Yam.")
    case "5":
        print("Goodbye!")
    case _:
        print("Invalid option. Please select 1-5.")