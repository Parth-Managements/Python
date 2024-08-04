# a=int(input("Enter a "))

# def odev (a):
#     if(a%2==0):
#         print(f"{a} is even")
#     else:
#         print(f'{a} is odd')

# odev(a)

# def details(name,year,std,address,roll):
#     print(name,year,std,address,roll)

# details('Rohit',std=12,address='CG Road',roll=32,year=2024)

# def example(*args):
#     for i in args:
#         if(i=='apple'):
#             print("The color is Red")


# example('banana','mango','kiwi','pomegranate','apple')


# def examlpe(*k,**c):

#     list1=[]

#     for i in k:
#         list1.append(i*i)

#     print(list1)

#     c.pop('key3')


#     c['key4'] = 'value4'

#     print(c)


    
# examlpe(1,2,3,4,5,key1='value1',key2='value2',key3='value3')

#-------------------------------------------- Function loop ----------------------------------------------------
# def sum(a , b):
#     return a+b

# def ans(a,b):
#     return sum(a,b)

# print(ans(5,5))

#-------------------------------------------- Function loop ----------------------------------------------------

a=int(input("Enter your choice: 1.Factorial 2.Palindrome 3.Even/odd\n"))


if(a==1):
    b = int(input("Enter a number: "))
    factorial = 1


    for i in range(1, b + 1):
        factorial *= i
        
    print("Factorial of", b, "is", factorial)

if(a==2):
    s1=str(input("Enter your string\n"))
    
    if s1 == s1[::-1]:
        print("It is palindrome")


if(a==3):
    num=int(input("Enter the number"))

    if(num%2==0):
        print(f"{num} is even")

    else:
        print(f"{num} is odd")






