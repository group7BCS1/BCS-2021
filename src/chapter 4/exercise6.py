#program to compute pay of a worker using a computepay functiom
def computepay(h, r):
    if h < 0 or r < 0:
        return None
    elif h > 40:
        return (40 * r + (h - 40) * 1.5 * r)
    else:
        return (h * r)
try:
    hrs = input("Enter Hours: ")
    hour = float(hrs)
    r = input("please input your rate: ")
    rate = float(r)
    pay = computepay(hour, rate)
    print(pay)
except Exception:
    print("Input a number")