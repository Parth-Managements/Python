# # n=int(input("Enter the number:"))

# # for i in range(n):
    
# #     if('3' in str(i) or '6' in str(i) ):
# #         continue
# #     else:
# #         print(i)
# sum = 0
# number = 0
# while number < 5:
#     number = int(input('Enter a positive number: '))
#     sum = sum + number
#     number+=1
# print("The sum of the numbers is", sum)
# thistuple=("apple","banana","cherry","orange","kiwi","melon","mango","grapes","pomegranate","papaya")

# print(thistuple[::-1])
# print(thistuple[:-5:-1])
# print(thistuple[4:7:1])

# tuple1 = ('abc','royal','pvt','ltd','Mango')
# print(f"The maximum is {max(tuple1)}")
# print(f"The minimum is {min(tuple1)}")
# y=list(tuple1)
# del y[2:5:]
# tuple1=tuple(y)
# print(f"After removing {tuple1}")

# y=list(tuple1)
# y.append('apple')
# y.append('banana')
# tuple1=tuple(y)
# print(f"After adding {tuple1}")
# tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# string=''
# for i in tup:
#     string=string+i

# print(string)

list1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(list1)):
    y=list(list1[i])
    y[2]=100
    list1[i]=tuple(y)

print(list1)
