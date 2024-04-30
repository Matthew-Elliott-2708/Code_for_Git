##random word (randomness) gives _ _... for 
##len of word when guess letter right puts in place else write 1 at a time 
##   0
##  -|-
##  / \
## file with words open file otherwise looks cluttered
dead = 0 
word = "o"
while dead != 6:
    guess = input("Please guess the word: ")
    if guess == word:
        print("CONGRATULATIONS YOU GUESSED CORRECTLY!")
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