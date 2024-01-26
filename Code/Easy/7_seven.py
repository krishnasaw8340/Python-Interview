'''
1. Find the Output:==>

Input -  "the sky is blue"
Output - "blue is sky the"


2. Remove Punctuation ( Exccept space)

'''
s = input("Enter string : ")
# the sky is blue
n = len(s)
lst = []
st = ''
for i in range (n-1,-1,-1):
    if s[i]!=' ':
        lst.append(s[i])
    else:
        lst.reverse()
        st += ''.join(lst)+ ' '
        lst = []
lst.reverse()
st += ''.join(lst)
print(st)
        


