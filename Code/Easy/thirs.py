# Wheather a string is palindrome or not:

s = "madam"
if (s== s[::-1]):
    print("Yes")
else:
    print("No")


s = "nitin"
n = len(s)
x= 0
for i in range(n):
    if(s[i] != s[n-i-1]):
        x = 1
        break
if(x==0):
    print("Yes")
else:
    print("No")