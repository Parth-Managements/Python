# a=int(input("a dog's age in human years:"))
# if(a<=2):
#     b=a*10.5
# else:
#     b=(a-2)*4+21
# print(f"The dog's age in dog years is {b}")



# a=input("Input the name of month: ")
# odd=["January","March","May","July","August","October","December"]
# even=["April","June","September","November"]
# if(a in odd):
#     print("No. of days: 31 Days")
# elif(a in even):
#     print("No. of days: 30 Days")
# else:
#     print("No. of days: 28/29 Days")
    
# Looping Starts

# str1='12345123456'
# str2=''
# for i in str1:
#     if(i not in str2):
#        str2+=(i) 
# print(str2)

list1=[11,22,33,44,55,66,77,88,99,00]
even=0
odd=0
for i in list1:
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(f"Sum of even is {even}")
print(f"Sum of odd is {odd}")