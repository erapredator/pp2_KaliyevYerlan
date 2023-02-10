# You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    list.append(element)

def filter_prime(list):
    for x in list:
        if x ==1:
            list.remove(x)
        i = 2
        while i<x:   
            if x%i==0:
                list.remove(x)
                break
            i+=1
    print(list)
filter_prime(list)
 

