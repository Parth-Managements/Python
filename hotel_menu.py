class Restaurant:
    def __init__(self):
        self.menu = {"dosa":100 , 'pizza':200 , 'pasta':150 , 'maggie':50 , 'icecream':70 , 'shake':80}
        self.tables = {}
        self.orders = {}



    def book_table(self, table_number, customer_name):
        if table_number not in self.tables:
            self.tables[table_number] = customer_name
            print(f"Table {table_number} booked ")
        else:
            print(f"Table {table_number} is already booked")

    def customer_order(self, table_number, *items):
        if table_number in self.tables and self.tables[table_number] == "Available":
            if table_number not in self.orders:
                self.orders[table_number] = []
            self.orders[table_number].extend(items)
            order_str = ""
            for item in items:
                order_str += item + ", "
            print(f"Order received from table {table_number}: {order_str[:-2]}")
        else:
            print(f"Table {table_number} is not available for orders.")

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for table, customer in self.tables.items():
            print(f"Table {table}: {customer}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.orders.items():
            print(f"Table {table} ordered: {', '.join(order)}")


restaurant = Restaurant()


while True:
    table_number = int(input("Enter table number to book (or 0 to finish booking): "))
    if table_number == 0:
        break
    customer_name = input("Enter customer name: ")
    restaurant.book_table(table_number)

while True:
    table_number = int(input("Enter table number to take order (or 0 to finish): "))
    if table_number == 0:
        break
    items = input("Enter items ordered (comma-separated): ").split(",")
    restaurant.customer_order(table_number, *items)

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()
