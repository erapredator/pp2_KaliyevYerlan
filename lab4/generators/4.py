def func(a, b):
    for i in range(a, b+1):
        yield i*i

        
a = int(input())
b = int(input())
f = func(a, b)

for i in f:
    print(i)