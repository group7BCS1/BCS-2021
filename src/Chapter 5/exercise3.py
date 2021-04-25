print('\nWelcome to the vending machine change maker program')
print('\nChange maker initialized')
print('\nStock contians:')
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
        user_input=float(user_input)
        user_input=((user_input*100)%5==0)
        if user_input>0 and ((user_input*100)%5==0):
            user_input=int(round(((user_input*100)%5==0),2))
            print('\ndeposit menu:\n')
            print("'n'-deposit a nickel\n'd'-deposit a dime\n'q'-depost a qaurter\n'o'-deposit a one dollar bill\n'f'-deposit a five dollar bill\n'c'-cancel the purchase\n")
            
        else:
            print('invalid input')
        print(user_input)
    except:
        print('invalid input')