# example 4
# the variables e and f can be any floating
# point numbers from any calculation

e = 7.135
f = 7.128

if abs(e - f) < 0.01:
    print(f"{e} and {f} are close enough so")
    print("we'll consider them so be equal")

else:
    print(f"{e} and {f} are not close and")
    print("before not equal")