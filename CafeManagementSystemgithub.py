# starpoint Menu
menu = {
    "Espresso": 150, "Americano": 180, "Cappuccino": 200,
    "Latte": 220, "Mocha": 250, "Frappuccino": 300,
    "Caramel Macchiato": 280, "Cold Brew": 260,
    "Pastry": 120, "Croissant": 150, "Bagel": 100, "Muffin": 130
}

# GST rate
GST_RATE = 0.18

# Cart to store orders
cart = {}

# Function to update and display the bill
def update_bill():
    total = sum(menu[item] * qty for item, qty in cart.items())
    if not cart:
        print("Your cart is empty!")
    else:
        print("\nYour Cart:")
        for item, qty in cart.items():
            print(f"{item} x {qty} = {menu[item] * qty}")
        print(f"\nTotal: {total}\n")

# Add items to cart
def add_to_cart(item, qty):
    if qty > 0:
        cart[item] = cart.get(item, 0) + qty
        print(f"{qty} {item}(s) added to the cart.")
    else:
        print("Invalid quantity. Please enter a value greater than 0.")

# Remove items from cart
def remove_from_cart(item, qty):
    if item in cart:
        if qty >= cart[item]:
            del cart[item]
            print(f"All {item}(s) removed from the cart.")
        else:
            cart[item] -= qty
            print(f"{qty} {item}(s) removed from the cart.")
    else:
        print(f"{item} is not in the cart.")

# Checkout
def checkout():
    if not cart:
        print("Your cart is empty!")
    else:
        subtotal = sum(menu[item] * qty for item, qty in cart.items())
        gst = subtotal * GST_RATE
        total = subtotal + gst
        print("\nYour Order:")
        for item, qty in cart.items():
            print(f"{item} x {qty} = {menu[item] * qty}")
        print(f"\nSubtotal: {subtotal:.2f}")
        print(f"GST (18%): {gst:.2f}")
        print(f"Total: {total:.2f}")
        print("\nThank you for visiting Starpoint Cafe!")
    exit()

# Main application
def cafe_management():
    while True:
        print("\n--- Starpoint Cafe Menu ---")
        for item, price in menu.items():
            print(f"{item}: {price} INR")

        print("\nOptions:")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart and bill")
        print("4. Checkout")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            item = input("Enter the item name: ").strip()
            if item in menu:
                try:
                    qty = int(input(f"Enter the quantity of {item}: "))
                    add_to_cart(item, qty)
                except ValueError:
                    print("Invalid input. Quantity must be a number.")
            else:
                print("Item not found in the menu.")
        
        elif choice == "2":
            item = input("Enter the item name: ").strip()
            if item in menu:
                try:
                    qty = int(input(f"Enter the quantity to remove for {item}: "))
                    remove_from_cart(item, qty)
                except ValueError:
                    print("Invalid input. Quantity must be a number.")
            else:
                print("Item not found in the menu.")

        elif choice == "3":
            update_bill()

        elif choice == "4":
            checkout()

        elif choice == "5":
            print("Thank you for visiting Starpoint Cafe!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the application
cafe_management()