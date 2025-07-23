'''Write a program in python to take a sentence as input. Now count occurrence of
‘The’ word in given sentence.'''

sentence = input("Enter a sentence: ")
words = sentence.split()
count = sum(1 for word in words if word.lower() == 'the')
print("Occurrence of 'The':", count)