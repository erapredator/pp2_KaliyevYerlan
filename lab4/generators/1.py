def generate_squares(N):
    for i in range(N):
        yield i**2

k = int(input())
squares = generate_squares(k)

for i in squares:
    print(i)
