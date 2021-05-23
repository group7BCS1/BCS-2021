# Program prompting a user for a list and prints out the maximum and minimum of the number
list = []   # initialize array
while True:
    number = 0
    input_number = input("Enter a number: ")
    if input_number == "done":
        break
    else:
        try:
            number = float(input_number)
            list.append(input_number)
        except ValueError:
            print("Invalid input")
            quit()


print("Maximum:", max(list))
print("Minimum:", min(list))
