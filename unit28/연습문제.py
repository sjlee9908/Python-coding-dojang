n = int(input())
text = input()
words = text.split()


if n>len(words):
    print('wrong')
    
else:
    n_gram = zip(*[words[i:] for i in range(n)])                           
    for i in n_gram:
        print(i)
