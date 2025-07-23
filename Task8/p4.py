#Write a program in python to take a sentence as input. Now count words in given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words in the sentence:", len(words))