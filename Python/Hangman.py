##random word (randomness) gives _ _... for 
##len of word when guess letter right puts in place else write 1 at a time 
##   0
##  -|-
##  / \
## file with words open file otherwise looks cluttered

#artifical randomness#
for words in open("hangman_words.txt"):
    words = words.split()
    final = list(set(words))
print (final, len(final))
open('hangman_words.txt', 'w').close()
words = open('hangman_words.txt', 'w')
for word in final:
    words.write(word + " ")
words.close()

file = open("hangman_words.txt")
all = file.read().split()
word = all[:1]
for single in word:
     final_word = single

print(final_word)
win = False
underscores = " "
dead = 0 
print(" |‾|")
print(" |")
print(" |")
print(" |")
print("_|_")
for letters in range(len(final_word)):
    underscores += "_ "
print(underscores)
while dead != 6 and win == False:
    i = 0
    guess = input("Please guess a letter or the whole word : ")
    if guess == final_word:
        print("CONGRATULATIONS YOU GUESSED CORRECTLY!")
        win = True
    elif guess in final_word:
        print(guess)
        list_final_word = list(final_word)
        for letters in range(len(final_word)):
            if guess == list_final_word[1:i]:
                print(i)
                i += 1
            else:
                i += 1
    else:
        dead += 1
    if dead == 1:
        print(" |‾|")
        print(" | 0")
        print(" |")
        print(" |")
        print("_|_")
    elif dead == 2:
        print(" |‾|")
        print(" | 0")
        print(" | |")
        print(" |")
        print("_|_")
    elif dead == 3:
        print(" |‾|")
        print(" | 0")
        print(" |-|")
        print(" |")
        print("_|_")
    elif dead == 4:
        print(" |‾|")
        print(" | 0")
        print(" |-|-")
        print(" |")
        print("_|_")
    elif dead == 5:
        print(" |‾|")
        print(" | 0")
        print(" |-|-")
        print(" |/")
        print("_|_")
if dead == 6:
    print(" |‾|")
    print(" | 0")
    print(" |-|-")
    print(" |/ \\")
    print("_|_")
    print("You lost!")