
fhand = open('chapter7\mbox-short.txt')
for line in fhand:                      # Handles one line at a time
    shout = line.rstrip().upper()       # Removes newline and capitalizes
    print(shout)
