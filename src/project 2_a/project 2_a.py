try:
    f_name = open('measles.txt')
except Exception:
    exit()

apo = input('Enter file name: ')
handle = open(apo, 'w')
year = input('Enter year:')

for line in f_name:
    if (year == line[88:92]) or (year == line[88:91]) or (year == line[88:90]) or (year == line[88:89]):
        handle.write(line)
    elif (year == 'all') or (year == 'ALL') or (year == ''):
        handle.write(line)
