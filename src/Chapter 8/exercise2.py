text = input("Enter a file name: ")
fhand = open("text")
for line in fhand:
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != "From":
        continue
    print(words[2])
