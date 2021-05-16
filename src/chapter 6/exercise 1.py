fruit = input("Enter a word: ")
index = (len(fruit)-1)
while index >= 0:
    letter = fruit[index]
    index = index - 1
    print(letter)
