def open_file():
    prompt = input('Enter file: ')
    try:
        handle = open(prompt)
    except:
        print("Enter valid file")
        prompt = input('Enter file: ')
        handle = open(prompt)
    return handle


def process_file(file_object):
    lower_income = 'WB_LI '
    lower_middle = 'WB_LMI'
    upper_middle = 'WB_UMI'
    high_income = 'WB_HI '

    guide = """
  1 = low income
  2 = lower middle income
  3 = upper middle income
  4 = high income
  """

    income_level = input(f"{guide}\nEnter income level: ")
    count = 0
    total = 0
    year = input('Enter year: ')
    for line in open_file():
        if year == line[88:92]:
            if income_level == '1':
                if line[51:57] == lower_income:
                    apo = line[58:61]
                    percent = float(apo)
                    count += 1
                    total += percent
                    print(line.strip())
                    continue
            if income_level == '2':
                if line[51:57] == lower_middle:
                    apo = line[58:61]
                    percent = float(apo)
                    count += 1
                    total += percent
                    print(line.strip())
                    continue
            if income_level == '3':
                if line[51:57] == upper_middle:
                    apo = line[58:61]
                    percent = float(apo)
                    count += 1
                    total += percent
                    print(line.strip())
                    continue
            if income_level == '4':
                if line[51:57] == high_income:
                    apo = line[58:61]
                    percent = float(apo)
                    count += 1
                    total += percent
                    print(line.strip())

    print(f'This is the count {count}')
    print(f'This is the total {total}')
    print(f'This is the Average {total / count}')


def main():
    process_file(open_file())
    open_file().close()


if __name__ == '__main__':
    main()
