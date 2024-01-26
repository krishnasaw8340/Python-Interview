# Generate a Infinite Fibonacci Series Bu using a generator:


def fibo():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
f1 = fibo()
# for i in f1:
#     print(i)
# count = 0
# if( count <= 10):
#     print(next(f1))
#     count = count + 1


print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))




