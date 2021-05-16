word = input("Enter a word: ")
letter = input("Enter a letter: ")


def count(word, letter):
    letter_num = 0
    for a in word:
        if letter is a:
            letter_num += 1
            print(letter_num)


count(word, letter)