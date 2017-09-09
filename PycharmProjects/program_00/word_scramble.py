# Scramble a user-inputted word and print out all letter combinations
# where consecutive letters are not the same as they are in the original
# word.
# Example
# -------
# INPUT: word
# OUTPUT:
# wrod
# wdro
# owdr
# odwr
# odrw
# rwdo
# rwod
# rodw
# rowd
# dwro
# dowr
# dorw
# drow
# drwo

word = raw_input("Word: ")

# loop through letters in the word
for letter in word:
    # loop through the subsequent letters
    for i, c in enumerate(word):
        if word[i] != letter:
            str = letter + c
            if word.find(str) == -1:
                print str