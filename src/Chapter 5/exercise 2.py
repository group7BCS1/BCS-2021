list = []  # initializing array
number = 0
# repeatedly reads numbers until 'done' is entered
while True:
    numinput = input('Enter a number: ')
    if numinput == 'done':
        break
    try:
        number = float(numinput)
    except Exception:  # error message if input is not 'done' or a number
        print('Invalid input')
        continue
    list.append(numinput)  # puts all numinput into the list
if list:
    print('maximum', max(list), 'minimum', min(list))
