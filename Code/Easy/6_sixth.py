# Create a fibbonacci series bu sing a Recursion:

# 0 1 1 2 3 5 8 

def fibbo (n):
    if n <=1:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)

n = int(input("How many terms ?"))
if n <=0:
    print("Enter positive number")
else:
    for i in range(n):
        print(fibbo(i))
