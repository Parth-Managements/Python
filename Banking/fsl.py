class Restaurant:
    def __init__(self):
        self.order_d = {}
        self.add_menu = {"dosa": 100, 'pizza': 200, 'pasta': 150, 'maggie': 50, 'icecream': 70, 'shake': 80}
        self.book_table = {1: 'reserved', 2: 'reserved', 3: 'available', 4: 'available', 5: 'reserved'}

    def order(self, token, *item):
        m = list(item)
        self.order_d.update({token: m})

    def reserve(self, table_no):
        if self.book_table.get(table_no) == "reserved":
            print(f'Table number {table_no} is reserved')
        elif self.book_table.get(table_no) is None:
            print(f'Table number {table_no} is not available')
        else:
            print(f'Table number {table_no} is booked!')
            self.book_table[table_no] = "reserved"

    def print_menu(self):
        print(self.add_menu)

    def print_reserve(self):
        print(self.book_table)

    def print_order(self):
        print(self.order_d)

    def bill(self):
        pass


obj = Restaurant()
obj.reserve(3)
obj. print_menu
obj.print_reserve
obj.print_order