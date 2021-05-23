# Program reading through a mail box ad splits lines starting with "From" into words
text = input(" Enter a file name: ")
fhand = open('text')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
    print(f"There were {count}")
