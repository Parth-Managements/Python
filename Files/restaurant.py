class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}
        self.tables = {}
        self.orders = {}

    def add_item(self, item_name, price):
        self.menu[item_name] = price

    def book_tables(self, table_num, seats):
        self.tables[table_num] = seats

    def customer_order(self, table_num, items):
        if table_num not in self.orders:
            self.orders[table_num] = []
        self.orders[table_num].extend(items)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: Rs {price}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for table, seats in self.tables.items():
            print(f"Table {table}: {seats} seats")

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, items in self.orders.items():
            print(f"Table {table}: {', '.join(items)}")

            
res = Restaurant("My Restaurant")
res.add_item("Pasta", 180)
res.add_item("Maggi", 150)
res.add_item("Coke", 90)
res.book_tables(1, 2)
res.book_tables(2, 4)
res.book_tables(3, 2)
res.customer_order(1, ["Pasta", "Coke"])
res.customer_order(2, ["Maggi"])
res.customer_order(3, ["Coke"])
res.print_table_reservations()
res.print_menu()
res.print_customer_orders()