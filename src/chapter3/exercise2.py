# Program that calculates pay of a worker/user
# Depending on the number of hours worked and rate of payment
# including try, except
try:
    hours = int(input("Enter the hours worked: "))
    rate = float(input("Enter the payment rate: "))
    if hours > 40:
        payment = rate * 40
        extra = 1.5 * (hours - 40) * 10
        pay = payment + extra
        print(pay)
    if hours <= 40:
        payment = rate * hours
        print(payment)
except Exception:
    print("Error please enter digit")
