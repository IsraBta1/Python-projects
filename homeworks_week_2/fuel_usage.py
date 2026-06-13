def main():
    pass
    # get an odometer value in U.S miles from the user.
start_miles = float(input("Enter the first odometer reading (miles): "))

    #get another odometer value in U.S miles from the user.
end_miles = float(input("Enter the second odometer reading (miles): "))

    #get a fuel amount in U.S gallons from the user.
amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    # call the miles_per_gallon function and store

miles_per_gallon = ()
lp100k_from_mpg = ()

mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
lp100k = lp100k_from_mpg(mpg)
    #display the results for the user to see.
print(f"{mpg:.1f} miles of gallon")
print(f"{lp100k:.2f} liters per 100 kilometers") 

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg

def p100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k
main()