# function to calculate the number of gallons used
def gallons_used(x, y):
    if y > x:
        gallons = (y - x) / 10
    else:
        x = 1000000000 - x
        gallons = (x + y) / 10
    print(f"Gallons of water used:{gallons:.2f}")
    return gallons


while True:
    customer_code = input("Enter Customer code: ")
    if customer_code == 'r' or customer_code == 'R':
        beginning_reading = int(input("Enter beginning reading"))
        ending_reading = int(input("Enter ending reading"))
        print(f"Customer code: {customer_code}")
        print(f"Beginning meter reading: {beginning_reading:09d}")
        print(f"Ending meter reading: {ending_reading:09d}")
        gallons = gallons_used(beginning_reading, ending_reading)
        bill = 5 + (gallons * 0.0005)
        print(f"Amount billed: ${bill:.2f}")
    elif customer_code == 'c' or customer_code == 'C':
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

