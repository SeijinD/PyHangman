import random

with open('greek.raw', 'r', encoding="utf8") as f:
    word = random.choice(f.readlines()).rstrip()

found = False
tries = 6
letters = []

def hide():
    hidden = ''
    for letter in word:
        if letter in letters:
            hidden += letter
        else:
            hidden += '-'
    return hidden

while not found and tries > 0:
    hidden_word = hide()
    if hidden_word == word:
        print("Congratsulation!")
        exit()
    print(hidden_word)
    letter = input("Type a letter: ")
    if letter in letters:
        print("Υou have already tried this letter.")
        continue
    letters.append(letter)
    if letter in word:
        print("The letter exists.")
    else:
        print("The letter not exists.")
        tries -= 1
    print(tries, " attempts remain.")
        
print("You lost!")
print("The word was ", word)
