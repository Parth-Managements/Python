# Restaurant
# Write a Python class Restaurant with attributes like  methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.
# Note: Use dictionaries and lists to store the data.

# orders={"order_no":[],}
# foods={"dosa":200}
# tables={"1":reserverd


# add_menu {item : price}
class r:
    def _init_(self):
        self.order = {}
        self.add_menu = {"maggie":100 , 'pasta':150 , 'pizza':200 , 'manchurian':60 , 'icecream':70 , 'Milkshake':80}
        self.book_table={1:'reserved' , 2:'reserved' , 3:'available' , 4:'available' , 5:'reserved'}
    
    def order(self,token,*item):
        m = list(item)
        self.order_d.update({token:m})

    def reserve(self,tabel_no):
        if(self.book_table.get(tabel_no)=="Reserved"):
            print(f'Table number {tabel_no} is reserved')
        elif (self.book_table.get(tabel_no)==None):
            print(f'{tabel_no} is not available ')
        else:
            print(f'{tabel_no} is booked !')
            self.book_table[tabel_no]="Reserved"

    
            
        

    def print_menu(self):
        print(self.add_menu)

    def print_reserve(self):
        print(self.book_table)

    def print_order(self):
       print(self.order)



obj = r()
r.reserve(30)