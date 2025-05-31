class Restaurant():
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []  # Changed from book_tables to avoid method conflict
        self.customer_orders = []  # Changed to list to store order dictionaries

    def add_items_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_table(self, table_number):  # Renamed to avoid conflict with attribute
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
        else:
            print(f"Table {table_number} is already booked")

    def customer_order(self, table_number, order):  # Renamed to avoid conflict
        if table_number in self.booked_tables:
            order_details = {'table_number': table_number, 'order': order}
            self.customer_orders.append(order_details)
        else:
            print(f"Table {table_number} is not booked yet")

    def print_menu_items(self):
        print("\nMenu Items:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")

    def print_table_reservations(self):  # Corrected method name
        print("\nBooked Tables:")
        for table in self.booked_tables:
            print(f"Table {table}")

    def print_customer_orders(self):
        print("\nCustomer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']}: {order['order']}")

# Create restaurant instance
restaurant = Restaurant()

# Add items to menu
restaurant.add_items_to_menu("Cheeseburger", 9.99)
restaurant.add_items_to_menu("Caesar Salad", 8)
restaurant.add_items_to_menu("Grilled Salmon", 19.99)
restaurant.add_items_to_menu("French Fries", 3.99)
restaurant.add_items_to_menu("Fish & Chips", 15)  # Removed extra colon

# Book tables
restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(3)

# Take orders
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")

# Print information
restaurant.print_menu_items()
restaurant.print_table_reservations()
restaurant.print_customer_orders()