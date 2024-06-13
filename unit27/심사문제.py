import string

with open('words.txt', 'r') as file:
    words=file.readline()
    for word in words.split():
        if 'c' in word:
            print(word.strip(string.punctuation))
        
