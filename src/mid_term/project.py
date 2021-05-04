# function to calculate the number of gallons used
def gallons_used(x, y):
    if y > x:
        gallons = (y - x) / 10
    else:
        x = 1000000000 - x
        gallons = (x + y) / 10
    print("Gallons of water used: ", round(gallons, 2))
    return gallons


while True:
    customer_code = input("Enter Customer code: ")
    beginning_reading = int(input("Enter beginning reading"))
    ending_reading = int(input("Enter ending reading"))
    print(f"Customer code:{customer_code}")
    print(f"Beginning meter reading:{beginning_reading:09d}")
    print(f"Ending meter reading:{ending_reading:09d}")
    gallons = gallons_used(beginning_reading, ending_reading)

