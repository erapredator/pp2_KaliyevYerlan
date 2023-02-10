# Write a function that computes the volume of a sphere given its radius.
import math
def volume(radius):
    return round(4 * math.pi * (radius**3) / 3, 2)
radius = int(input("Enter a radius of a sphere in metres "))
print("Volume: ", volume(radius), "cubic meters")
