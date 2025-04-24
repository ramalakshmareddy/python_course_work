print("===== Welcome to Python Swiggy =====")

users = {
    "ram": {"prime": True, "password": "ram@0393", "phone_number": "7036054598", "orders": []},
    "sai": {"prime": True, "password": "sai@07", "phone_number": "8954506307", "orders": []},
    "virat": {"prime": False, "password": "virat@18", "phone_number": "8089181818", "orders": []},
    "gill": {"prime": False, "password": "gill@97", "phone_number": "80897979797", "orders": []},
    "dinesh": {"prime": True, "password": "dinesh@45", "phone_number": "802454545", "orders": []}
}

prime_restaurants = {
    "PistaHouse": {"Haleem": 1000, "Biryani": 680, "Tandoori Chicken": 750, "Murgh Malai Kabab": 700},
    "Paradise": {"Biryani": 1030, "Paneer Curry": 1180, "Chilli Chicken": 1200, "Apollo Fish": 1980},
    "ShahGhouse": {"Dal Fry": 500, "Mutton Biryani": 1850, "Chicken Biryani": 1300},
    "Bawarchi": {"Mutton Kheema": 1550, "Afghan Chicken": 1450, "Mutton Maharaja": 1800},
    "ITCKohenur": {"Afghan Chicken": 1300, "Mutton Gosh": 1850, "Mutton Afghani": 1700}
}

normal_restaurants = {
    "Hot Bowl": {"Chicken Biryani": 250, "Mutton Biryani": 450, "Roti": 20, "Paneer Curry": 220},
    "Red Biryani": {"Chicken Biryani": 200, "Afghan Chicken": 350, "Dal Fry": 120, "Rumali Roti": 30},
    "Blue Star": {"Veg Noodles": 120, "Chicken Maggi": 150, "Chicken Noodles": 170},
    "Mifel": {"Chicken Biryani": 150, "Mutton Biryani": 300, "Chicken Keema": 200}
}

delivery_boys = ["Raj", "Amit", "Rekha", "Shiva"]

# Authentication
current_user = None

while not current_user:
    print("\n1. Login\n2. Exit")
    choice = input("Choose option: ")
    
    if choice == "1":
        user = input("Enter your name: ").lower()
        password = input("Enter password: ")
        if user in users and users[user]["password"] == password:
            current_user = users[user]
            print(f"Welcome {user.title()} to Swiggy!")
        else:
            print("Invalid username or password.")
    elif choice == "2":
        print("Exiting Swiggy.")
        break
    else:
        print("Invalid option.")

# After login
while current_user:
    print("Swiggy Menu\n1.View Restaurants\n2.Place Order\n3.View Order History\n4. Logout")
    option = input("Choose an option: ")

    if option == "1":
        print("\n--- Restaurants Available ---")
        if current_user["prime"]:
            for rest, items in prime_restaurants.items():
                print(f"\n{rest}")
                for item, price in items.items():
                    print(f"  - {item} : ₹{price}")
        else:
            for rest, items in normal_restaurants.items():
                print(f"\n{rest}")
                for item, price in items.items():
                    print(f"  - {item} : ₹{price}")

    elif option == "2":
        print("\n--- Place Your Order ---")
        cart = []
        total = 0
        if current_user["prime"]:
            restaurants = prime_restaurants
        else:
            restaurants = normal_restaurants

        for rest, items in restaurants.items():
            print(f"\n{rest}")
            for item, price in items.items():
                print(f"  - {item} : ₹{price}")

        while True:
            item_name = input("Enter item to add to cart (or 'done' to finish): ").title()
            if item_name.lower() == "done":
                break

            found = False
            for items in restaurants.values():
                if item_name in items:
                    price = items[item_name]
                    cart.append((item_name, price))
                    total += price
                    print(f"{item_name} added to cart.")
                    found = True
                    break
            if not found:
                print("Item not found.")

        if cart:
            delivery = delivery_boys[len(current_user["orders"]) % len(delivery_boys)]
            current_user["orders"].append({"cart": cart, "total": total, "delivery": delivery})
            print("\nOrder Placed Successfully!")
            print("Delivered by:", delivery)
            print("Total Amount: ₹", total)
        else:
            print("No items ordered.")

    elif option == "3":
        print("\n--- Order History ---")
        if not current_user["orders"]:
            print("No previous orders.")
        else:
            for i, order in enumerate(current_user["orders"], start=1):
                print(f"\nOrder {i} | Delivered by: {order['delivery']} | Total: ₹{order['total']}")
                for item, price in order["cart"]:
                    print(f"  - {item} : ₹{price}")

    elif option == "4":
        print("Logging out...")
        current_user = None

    else:
        print("Invalid option.")
