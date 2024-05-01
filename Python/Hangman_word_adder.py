## the purpouse of this code is to add new words to the hangman game without any duplicates
for words in open("hangman_words.txt"):
    words = words.split()
    final = list(set(words))
print (final, len(final))
open('hangman_words.txt', 'w').close()
words = open('hangman_words.txt', 'w')
for word in final:
    words.write(word + " ")
words.close()
