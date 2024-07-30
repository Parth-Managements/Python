# list1=['23',56,'78','45',78,90]
# list2=[]

# list1.pop(1)
# print(list1)
# list1.pop(1)
# print(list1)

# list1=list2
# del list1
# print(list2)

list1=[45,78,90,23,56,12,4,32,32]
# print(list(reversed(list1)))
# list2=list1
# list2.append(45)
# list2.append(78)
# print(list2)

list2=list(reversed(list1))
list2.extend(['45','78'])
print(list2)

print(list(sorted(list1)))

print(list(sorted(list1,reverse=True)))




