def func(n):
    for i in range(n , 0 , -1):
        yield i

n = int(input())
f = func(n)
for i in f:
    print(i)