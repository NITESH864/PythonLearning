'''Write a program in python to take a sentence as input. Now in given sentence
replace a word with another word.'''

sentence = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

new_sentence = sentence.replace(old_word, new_word)
print("Updated sentence:", new_sentence)