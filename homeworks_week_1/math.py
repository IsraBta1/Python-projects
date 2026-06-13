import math

number = float(input("Enter a number: "))

print(math.sqrt(number))

if math.sqrt(number) < 100:
    print(f"The square root of is less than 100.")
elif math.sqrt(number) > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")

    