print('\nWelcome to the vending machine change maker program')
print('\nChange maker initialized')
print('\nStock contains:')
nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
print('', nickel, ' Nickels\n', dime, 'Dimes\n', quarter, 'quarters\n', one, 'Ones\n', five, 'Fives\n')

while True:
    try:
        user_input = input("enter the purchase price(xx.xx) or 'q' to quite:\n ")
        if user_input == 'q':
            break
        user_input = float(user_input)
        user_input = ((user_input * 100) % 5 == 0)
        if user_input > 0 and ((user_input * 100) % 5 == 0):
            user_input = int(round(((user_input * 100) % 5 == 0), 2))
            print("\ndeposit menu:\nMenu for deposits:\n 'n' - deposit a nickel\n 'd' - deposit a dime",\
        "\n 'q' -deposit a quarter\n 'f' -deposit a five dollar bill",\
        "\n 'c' -cancel the purchase")
        print("\nPayment due: ", dollars, "dollars and", cents, "cents")
        deposit_str = input("indicate your deposit: ")
        while user_input > 0:
            if not deposit_str.isdigit():
                if deposit_str =='n':
                    user_input -= 5
                    nickels += 1
                    dollars = user_input // 100
                    cents = user_input - (dollars *100)
                elif deposit_str == 'd':
                    user_input -= 25
                    quarters += 1
                    dollars = total_cents //100
                    cents = total_cents - (dollars * 100)
                elif deposit_str == 'o':
                    user_input -= 100
                    ones += 1
                    dollars = total_cents // 100
                    cents = total_cents - (dollars * 100)
                elif deposit_str =='f':
                    user_input -= 500
                    fives += 1
                    dollars = total_cents -(dollars * 100)
                elif deposit_str == 'c':
                    break
                    else:
        print("Illegal deposit: ", deposit_str)
            if user_input > 0:
                print("\nPayment due: ", dollars, "dollars and", cents, "cents")
                deposit_str = input('Indicate your deposit: ')
            else:
                if user_input == 0:
                    print("\nPlease take the change below.\n No change due.")
                    break
                change_quarters = abs(user_input) // 25
                if change_quarters > quarters:
                    change_quarters = quarters












