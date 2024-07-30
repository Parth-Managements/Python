# # data22={
# #     'one':1,
# #     'two':2,
# #     'three':3,
# #     'four':4,
# #     'five':5
# # }

# # # print(data22['one'])
# # # print(data22['two'])
# # # print(data22['three'])
# # # print(data22['four'])
# # # print(data22['five'])

# # # print(data22.get('twel',23))
# # # print(data22.items())

# # for i in data22.keys():
# #     if(i=='three'):
# #         {
# #             print(data22['three'])
# #         }
    
# data21={
#     'one':100,
#     'two':200,
#     'three':300
# }

# counter=0   

# for k in data21.keys():
#     if(k=='one'):
#         counter = counter + (1 * data21['one'])
#     elif(k=='two'):
#         counter = counter + (2 * data21['two'])
#     else:
#         counter = counter + (3 * data21['three'])

# print(counter)

data20={
    1:1,
    2:2,
    3:3,
    4:4,
    5:5
}

list1=[]

for k,m in data20.items():
    list1.append(k*m)


print(list1)
