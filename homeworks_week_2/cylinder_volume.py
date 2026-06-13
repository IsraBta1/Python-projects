import math
"""Example 1"""
# Define a function named

def print_cylinder_volume():    
    """It a data very important for unknowing """
    """Compute and print the volume of a cylinder.
        Parameters: none
        Return: nothing"""

# get the radius and height from the user

radius = float(input("Enter the radius of a cylinder: "))

height = float(input("Enter the height of a cylinder: "))


# computer the volume of the cylinder.

volume = math.pi * radius**2 * height

# print the volume of the cylinder

print(f"Volume: {volume:.2f}")
