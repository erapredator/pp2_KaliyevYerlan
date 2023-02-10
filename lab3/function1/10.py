# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Note: don't use collection set.
def unique_list(lst):
    unique_elements = []
    for element in lst:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    list.append(element)

new_list = unique_list(list)

print(new_list)
