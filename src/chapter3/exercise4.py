# program confirming the voting status of a user depending on the user's age
# including try, except
try:
    age = int(input("Enter age: "))
    if age >= 18:
        print("YOU CAN VOTE.")
    elif age >= 0:
        print("YOU CAN NOT VOTE.")
    else:
        print("YOU ARE A TIME TRAVELLER")
except Exception:
    print("Please enter a numeric value ")
