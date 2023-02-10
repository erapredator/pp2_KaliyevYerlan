# Write a function that accepts string from user and print all permutations of that string
def permutations(data, index=0):
    if index == len(data):
        print("".join(data))
    else:
        for i in range(index, len(data)):
            data[index], data[i] = data[i], data[index]
            permutations(data, index + 1)
            data[index], data[i] = data[i], data[index]

string = input("Enter a string: ")
permutations(list(string))