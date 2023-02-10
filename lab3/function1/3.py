# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def my_function(numheads, numlegs):
    if numheads >= numlegs:
        print("number of legs are always more than number of heads")
    elif numlegs%2 != 0:
        print("number of legs can not be odd number")
    else :
        rabbit_count=(numlegs-2*numheads)/2
        chicken_count=numheads-rabbit_count
        print(int(chicken_count), int(rabbit_count))
numheads = int(input())
numlegs = int(input())
my_function(numheads, numlegs)
