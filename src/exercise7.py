a=float(input("Enter an amount to make change for;"))
x=a//20
b=(a%20)//10
c=((a%20)%10)//5
d=(((a%20)%10)%5)//1
t=((((a%20)%10)%5)%1)//0.25
r=(((((a%20)%10)%5)%1)%0.25)//0.1
m=((((((a%20)%10)%5)%1)%0.25)%0.1)//0.05
p=(((((((a%20)%10)%5)%1)%0.25)%0.1)%0.05)//0.01

print("your change is..")
print(round(x),"twenties")
print(round(b),"ten")
print(round(c),"five")
print(round(d),"ones")
print(round(t),"quarters")
print(round(r),"dimes")
print(round(m),"nickels")
print(round(p),"pennies")