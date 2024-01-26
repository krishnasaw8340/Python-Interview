# Sort a dictiionary / Bu using a dict comprehension:

# dict1 = {545:"Apple", 686:"Mango", 223: "Banana", 123: "Grapes"}

# d = sorted(dict1.keys())
# dict1 = {}
# for i in d:
#     dict2[i] = dict1[i]
# print(dict2)


dict1 = {545:"Apple", 686:"Mango", 223: "Banana", 123: "Grapes"}

for key, value in sorted(dict1.items()):
    print(f'{value}:{key}')
 
'''
Output: 
Grapes:123
Banana:223
Apple:545
Mango:686
'''