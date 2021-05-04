# PROGRAM COMPUTING AND DISPLAYING INFORMATION FOR A UTILITY COMPANY THAT SUPPLIES WATER
# function to calculate the number of gallons used
def gallons_used(x, y):
    if y > x:
        gallons = (y - x) / 10
    else:
        # incase the beginning reading is bigger than the ending reading
        x = 1000000000 - x
        gallons = (x + y) / 10
    print(f"Gallons of water used:{gallons:.2f}")
    return gallons


while True:
    customer_code = input("Enter Customer code: ")
    # r is the code for residential
    if customer_code == 'r' or customer_code == 'R':
        beginning_reading = int(input("Enter beginning reading"))
        ending_reading = int(input("Enter ending reading"))
        print(f"Customer code: {customer_code}")
        # adding 09d because if a single digit is inserted, the leading zeros are added
        print(f"Beginning meter reading: {beginning_reading:09d}")
        print(f"Ending meter reading: {ending_reading:09d}")
        # replacing x and y with the beginning and ending readings respectively
        gallons = gallons_used(beginning_reading, ending_reading)
        bill = 5 + (gallons * 0.0005)
        # formatting the amount to print the value with 2 fractional digits
        print(f'Amount billed: ${bill:.2f}')
    elif customer_code == 'c' or customer_code == 'C':
        # c is the code for commercial
        beginning_reading = int(input("Enter beginning reading"))
        ending_reading = int(input("Enter ending reading"))
        print(f"Customer code:{customer_code}")
        print(f"Beginning meter reading:{beginning_reading:09d}")
        print(f"Ending meter reading:{ending_reading:09d}")
        gallons = gallons_used(beginning_reading, ending_reading)
        if gallons <= 4000000:
            bill = 1000
        else:
            bill = 1000 + ((gallons - 4000000) * 0.00025)
        print(f"Amount billed:${bill:.2f}")
    elif customer_code == 'i' or customer_code == 'I':
        # i is the code for industrial
        beginning_reading = int(input("Enter beginning reading"))
        ending_reading = int(input("Enter ending reading"))
        print(f"Customer code:{customer_code}")
        print(f"Beginning meter reading:{beginning_reading:09d}")
        print(f"Ending meter reading:{ending_reading:09d}")
        gallons = gallons_used(beginning_reading, ending_reading)
        if gallons <= 4000000:
            bill = 1000
        elif 4000000 < gallons <= 10000000:
            bill = 2000
        else:
            bill = 2000 + (gallons - 10000000) * 0.00025
        print(f"Amount billed: ${bill:.2f}")
    else:
        print("Invalid Entry")
        break
