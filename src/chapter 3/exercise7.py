# program evaluating what John's decision will be depending on the location and pay of the job.
# including try, except
try:
    g = input("Enter job location: ")
    b = int(input("Enter pay: "))
    if g.upper() == "MBARARA" and b < 4000000:
        print("No Thanks, I can find something better")
    elif g.upper() == "MBARARA" and b > 4000000:
        print("I can work with this")
    elif g.upper() == "KAMPALA" and b >= 10000000:
        print(" I can work with this")
    elif g.upper() == "KAMPALA" and b < 10000000:
        print("No way!")
    elif g.upper() == "SPACE" and b >= 0:
        print("Without doubt i will work")
    elif b >= 6000000:
        print("I will surely work")
    else:
        print("NO THANKS")
except Exception:
    print("INVALID ENTRY")
