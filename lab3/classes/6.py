def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers = [12, 17, 19, 21, 24, 29, 31, 37, 41, 43]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list are:", prime_numbers)
