import math
from datetime import datetime

"""
Student: Israel Jose Betancourt
Course 111 Programming with functions
Introduction of the program: This program calculates the volume of a tire based on user input for the width,
aspect ratio, and diameter of the tire. The formula used for the calculation is V = (pi * w^2 * a * (w * a + 2540 * d)) / 10,000,000,000, 
where w is the width in millimeters, a is the aspect ratio, and d is the diameter in inches. The result is displayed in liters with two decimal places.
The program also records the user's input and the calculated volume in a text file named "volumes.txt" along with the current date and the user's name.
"""
# get the name of the user
print("Hello, my name is Volume, nice to meet you.")
user_name = input("what is your name?: ").capitalize()
print(f"\nNice to meet you {user_name}, Welcome to tire volume calculator.")
enter = ""
print(f"\nGreat {user_name}, let's get started!")   


# width of the tire in millimeters
width = float(input(f"Please {user_name}, Enter the width of the tire in mm (ex 205): "))

# a is the aspecto ratio of the tire
aspect_ratio = float(input(f"Please {user_name}, Enter the aspect ratio of the tire (ex 60): ")) 

# d is the diameter of the wheel in inches
diameter = float(input(f"Please {user_name}, Enter the diameter of the wheel in inches (ex 15): "))

# volument formula: V = (pi * w^2 * a * (w * a + 2540 * d)) / 10,000,000,000
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000

print(f"\nThe approximate volume is {volume:.2f} liters")

"""Date time and writing name's user"""
date = datetime.now() # get the current date and time
formatted_date = date.strftime("%Y/%m/%d") # format the date as "YYYY/MM/DD"
with open("volumes.txt", "at") as file: # open the file in append mode
    file.write(f"[{formatted_date}] - Width: {width}, Aspect Ratio: {aspect_ratio}, Diameter: {diameter}, Volume: {volume:.2f} liters, Name: {user_name}\n") # write the formatted date, user input, and calculated volume to the file

print(f"{formatted_date}")