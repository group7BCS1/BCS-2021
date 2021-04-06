# Algorithm calculating the corresponding prices for the number of people attending the user's wedding
people = int(input("Enter number of people"))
if people <= 50:
    print("$4,000")
elif people <= 100:
    print("$10,000")
elif people <= 200:
    print("$15,000")
else:
    print("$20,000")
