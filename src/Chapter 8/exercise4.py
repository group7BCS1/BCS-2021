# program opening romeo.txt, reading lines then splitting them into a list of words then adding the words to a list
my_list = []
fhand = open('romeo.txt')
for line in fhand:
    # Splitting line into array of words
    words = line.split()
for word in words:
    if word in my_list:
        continue
    my_list.append(word)
    # Printing the list in alphabetical order
    print(sorted(my_list))
