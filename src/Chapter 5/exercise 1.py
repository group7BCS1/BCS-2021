total = 0
count = 0
# repeatedly reads numbers until 'done' is entered
while True:
    numinput = input('Enter a number: ')
    if numinput == 'done':
        print('Total: ', total, 'Count: ', count, 'Average: ', float(total) / count)
        break
    else:
        try:
            numinput = int(numinput)
            # runs total of numbers entered
            total = total + numinput
            # counting the numbers that have been entered
            count = count + 1
        except Exception:
            # error message if input is not 'done' or a number
            print('Invalid input')