# Find the maximum repeated character in a string without having O(n^2) complexity:

s = "heyhowareyou"
ch  = {}
for i in s:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1
print(ch)

# {'h': 2, 'e': 2, 'y': 2, 'o': 2, 'w': 1, 'a': 1, 'r': 1, 'u': 1}