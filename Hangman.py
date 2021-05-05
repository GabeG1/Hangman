import random
import linecache


def split(word): 
    return [char for char in word]  

def is_in_word(word, guess):
    temp = word.replace(guess, '')
    if word == temp:
        return False
    return True

f = open("words.txt", "r")
num_lines = sum(1 for line in open('words.txt'))

randLine = random.randint(1, num_lines)
randWord = linecache.getline('words.txt', randLine)
randWord = randWord.strip("\n")
hidden = []
for char in randWord:
    hidden.append("_")

print("\n", randWord, sep = '')
f.close

worcChars = split(randWord)

guesses = 0
while guesses < 6:
    for ele in hidden:
        print(ele, "", end = '')
    print()
    print("Tries Left: ", 6 - guesses, sep = '', end = '')
    print()
    inp = input("Enter a letter: ")
    if not is_in_word(randWord, inp):
        guesses += 1
    else:
        ind = 0
        for c in randWord:
            if c == inp:
                i = randWord.index(inp, ind)
                print(i)
                hidden[i] = inp
                ind += i + 1
    if "_" not in hidden:
        print("you won")
        exit()

print("You lost")



