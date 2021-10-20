learn = 'python is easy and fun.'
print(len(learn))
'''this is to print the length of the string.'''
print(learn.upper()) # prints the string in uppercase
print(learn.lower()) # prints the string in lowercase
print(learn.capitalize()) #capitalizes the first letter of the string
print(learn.title()) #capitalizes all the first letters of words in the string
print(learn.find('e'))
print(learn.find('and')) #looks for the letter/word mentioned in the parenthesis. this returns the index
'''if the find function cannot find the asked word, it returns -1 and is there are more than one occurrence of the asked
word, it only returns the index of the first occurrence'''
print('e' in learn)
print('and' in learn) #this finds the letter/word inthe string and returns a bool ie. true or false
print(learn.replace('python','nothing')) #replaces the first word with the word mentioned after it.
print(learn.count('y')) #counts the number of occurrences of the asked letter/word.
print(learn.endswith('fun.')) #checks if the string really ends with the asked word/letter