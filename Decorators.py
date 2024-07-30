# def factorial_decorator(func):
#     def inner(n):
#         if n < 0:
#             return 1
#         elif n == 0 or n == 1:
#             return 1
#         else:
#             return func(n)
#     return inner

# @factorial_decorator
# def calculate_factorial(n):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     return fac

    
# # print(calculate_factorial(2))

# def decor1(func):
#     print("decor 1")
#     def inner():
#         print("1")
#         x = func()
#         return x * x
#     return inner

# def decor2(func):
#     print("decor 2")
#     def inner():
#         print("2")
#         x = func()
#         return 2 * x
#     return inner

# @decor2
# @decor1
# def something():
#     num = 10
#     return num

# result = something()
# print(result) 

def print_P(func):
    def wrapper():
        print("P")
        return func()
    return wrapper

def print_a(func):
    def wrapper():
        print("a")
        return func()
    return wrapper

def print_rth(func):
    def wrapper():
        inps = "rth"
        return func()
    return wrapper

@print_P
@print_a
@print_rth
def print_name():
    pass  

print_name()

