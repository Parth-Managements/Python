# p = {}
# num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# for i in range(1,10):
#     p[i] = num[i-1]


# print(p)

dict1={
    'dict one':{
        'red' : 'apple'
    },
    'dict two':{
        'yellow': {
            'green' : 'banana',
            'yellow' : 'banana'
        }
    }
}

dict1['dict two']['black'] = 'chocolate'
dict1['dict two']['blue'] = 'chocolate'
dict1['dict two']['Red'] = 'chocolate'

dict1['dict two']['yellow']['green']='guava'



print(dict1)

# print(dict1.get('dict one'))
# print(dict1.get('dict one').get('red'))
# print(dict1.get('dict two'))
# print(dict1.get('dict two').get('yellow'))
# print(dict1.get('dict two').get('yellow').get('green'))
# print(dict1.get('dict two').get('yellow').get('yellow'))

# print(dict1['dict one'])
# print(dict1['dict one']['red'])
# print(dict1['dict two'])
# print(dict1['dict two']['yellow'])
# print(dict1['dict two']['yellow']['green'])
# print(dict1['dict two']['yellow']['yellow'])





