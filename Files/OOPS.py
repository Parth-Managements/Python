# class Student:
#     name = 'Rahul'
#     roll = 49
#     std = 5

#     def att(self,flag):
#         if flag:
#             print("present")
#         else:
#             print("not present")

#     def display(self):
#         print(self.name)
#         print(self.roll)
#         print(self.std)


# obj = Student()

# obj.display()
# flag = bool(input(""))
# # obj.att('flag')
# print(flag)


# ------------------------------ Initialiser , Constructor , input object , call object -------------------------------------------------------




# class Constructor:

#     def __init__(self) :
#         self.name="Rahul"
#         self.roll=49
#         self.std=8

#     def display(self):
#         print(f'Name = {self.name}')
#         print(f'Roll no. = {self.roll}')
#         print(f'Std = {self.std}')

#     def __str__(self) -> str:
#         return "Bro seriously You try to hack to me LOL!!!!!!"
    
#     def __call__(self):
#         print("Object is called")
        


# obj = Constructor()
# obj.display()
# print(obj)
# obj()

# ------------------------------ Class object , static method -------------------------------------------------------

# class Example:

#     data="royal"

#     def __init__(self) :
#         data="Techno"
#         pass

#     @classmethod
#     def clsmethod(self):
#         print(self.data)

#     @staticmethod
#     def stsmethod():
#         print("In static")



# v=Example()

# print(v.data)
# v.stsmethod()

# class Employee:

#     def __init__(self) :
#         self.name={
#             "E7876" : "ADAMS",
#             "E7499" : "JONES",
#             "E7900" : "MARTIN",
#             "E7698" : "SMITH"

#         }

#         self.salary={
#             "E7876" :  50000,
#             "E7900" :  50000,
#             "E7499" :  45000,
#             "E7698" :  55000


#         }

#         self.dept={
#             "E7876" : "ACCOUNTING",
#             "E7499" : "RESEARCH",
#             "E7900" : "SALES",
#             "E7698" : "OPERATIONS"
#         }

#     def  assign(self,emp_id,dept):
#         if self.dept.get(emp_id) == None:
#             print("NO")
#         else:
#             self.dept.update({emp_id:dept})

#         print(self.dept)


#     def overtime(self,emp_id,hours):
#         if self.salary.get(emp_id) == None:
#             print("No")
#         else:
#             ot = hours-50
#             amount=(ot * (self.salary.get(emp_id)/50))
#             return amount
        
#     def show(self,emp_id):
#         if self.name.get(emp_id)==None:
#             print("NO")
#         else:
#             print(f'Employee Name = {self.name.get(emp_id)}')
#             print(f'Employee Salary = {self.salary.get(emp_id)}')
#             print(f'Employee Department = {self.dept.get(emp_id)}')





# c=Employee()
# # c.assign(emp_id='E7876',dept='Manager')
# x=c.overtime('E7876',51)
# print(x)
# c.show('E7876')


# -------------------------------------Inheritnce-------------------------------------------


# class A:
#     pass

# class B(A):
#     def display(self):
#         print("in B")

# class C(B,A):
#     pass

# class D(C,B,A):
#     pass


# obj = D()
# obj . display()
# print(D.__mro__)

#--------------------------------MCD------------------------------------


# class MCD:
#     menu = {
#             "Burger":200,
#             "Pizza":500,
#             "French fries":100,
#             "Noodles":180
#     }
#     def display(self):
#         print(self.menu)

# class India(MCD):
    
#     labour={
#             "Men":3,
#             "Women":4,
#             "Manager":2,
#             "Accountant":1
#     }
#     def display(self):
#         print(self.labour)

# class Ahmedabad(India,MCD):
#     def __init__(self):
#         self.menu.update({"Dosa":150})

# obj = Ahmedabad()
# obj.display()
# print(obj.menu)


#-------------------------Encapsulation-------------------------------

class Amazon:
    _pr_name = "TV"
    __pr_price = "40000"

    def display(self):
        print(self._pr_name)
        print(self.__pr_price)

    def _change_name(self,new_name):
        self._pr_name = new_name
        print(self._pr_name)

    def __change_price(self,price):
        self.__pr_price = price
        print(self.__pr_price)
        
class User(Amazon):
        pass


             
obj = Amazon()
obj1 = User()
obj.display()
obj1._change_name("My Tv")
# obj.__change_price(1500)

        


        
        
            



        


        