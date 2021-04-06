# program to calculate the pay given to a worker depending on te number of hours worked.
hours = int(input("Enter the hours worked: "))
rate = float(input("Enter the payment rate: "))
if hours > 40:
    payment = rate * 40
    extra = 1.5 * (hours - 40) * 10
    # we subtract because the hours exceeding 40 are rated differently
    pay = payment + extra
    print(pay)
if hours <= 40:
    payment = rate * hours
    print(payment)
