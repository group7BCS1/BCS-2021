print('Welcome to the vending machine change maker program')
print('Change maker initialized')
print('Stock contians:')
nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
print( '',nickel ,' Nickels\n',dime,'Dimes\n',quarter,'quarters\n',one,'Ones\n',five,'Fives\n')

while True:
    try:
        user_input=input("enter the purchase price(xx.xx) or 'q' to quite:\n ")
        if user_input == 'q':
            break
        print(user_input)
    except:
        print('invalid input')