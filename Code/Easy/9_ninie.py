# Find the maximum and minimum value from a list without using a predefined function:

lst = [2,45,21,787,3,1]
n = len(lst)
min_val = lst[0]
max_val = lst[1]
for i in range(1,n):
    if min_val > lst[i]:
        min_val = lst[i]
for i in range(1,n):
    if max_val < lst[i]:
        max_val = lst[i]
print(min_val)
print(max_val)