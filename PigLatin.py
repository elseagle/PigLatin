#PIG LATIN

'''
Pig Latin is a game of alterations played on the English language game. To createpig latin for of a word;
the initial consonant sound is transposed to the end of the word and an 'ay' is affixed. Example:
'banana' would yield 'ananabay'. Make a program that converts a word or a sentence to pig latin.
For added difficulty, if users input only numbers notify them of a translation error


take the first consonant to the back and append ay
'''
#user inputs the word and the input is converted into a list
word = list(input("Kindly enter word: "))
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 
'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V','W', 'X', 'Y', 'Z']
print(word)

# a loop through our word to find the first consonant
for con in word:
    if con in consonants:
        word.remove(con)
        word.append(con)
        word.append('ay')
        pig_latin = ''.join(word)
        break
    else:
        pass
#another loop to detect number or symbols have been inputed
while True:
    if con not in consonants and con not in vowels:
        print('Wrong entry! You have entered a symbol or number')
        break
    else:
        print(pig_latin)
        break
