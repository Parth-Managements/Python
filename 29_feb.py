# # # d.update({'color':'Red','car':'bugati'})

# # d = {}
# # d['car'] = 'koenigsegg'
# # d['color'] = 'Black'
# # d['Engine'] = 'TFG'
# # d['name'] = 'Parth'
# # d['Grade'] = 'A'

# # pop=d.pop("Grade")
# # print(d)
# # print(pop)

# # popi=d.popitem()
# # print(d)
# # print(popi)

# a = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

# p= {}
# for i, k in a.items():
#     if k > 170:
#         p[i] = k

# print(p)



student={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
p={}

for i,k in student.items():
    if k[0] > 6 and k[1]>=70:
        p.update({i:k})

print(p)
       

