"""Example 2"""

import math
# define function named main:

def main ():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    # compute the volume of the cylinder
    volume = math.pi * radius**2 * height

    #print the volume
    print(f"Volume: {volume:.2f}")

    """Start this program by calling the main function"""
main()

def compute_cylinder_volume (radius, height):
    
    volume = math.pi * radius**2 * height

    return volume
main()

