# Sort a list without using a Sort keyword:

# 1. Sorting in python can be do by using .sort() in List:

list1 = [41,3,45,89,3,1,0,8776,2,45,98,24]
n = len(list1)

for i in range (n):
    for j in range(i+1, n):
        if(list1[i]>list1[j]):
            list1[i], list1[j] = list1[j], list1[i]
print(list1)