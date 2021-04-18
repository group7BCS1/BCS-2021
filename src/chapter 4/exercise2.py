#program that returns function investment to the nearest penny
try:
 c = int(input("Enter initial amount of investment: "))
 r = float(input("Yearly interest rate: "))
 t = int(input("Number of years until maturation: "))
 n = int(input("Number of times interest is compounded per year: "))
 p = c*((1+r/n)**(t*n))
 print(round(p, 2))
except Exception:
    print("Enter numeric values")