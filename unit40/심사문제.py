def prime_number_generator(start, stop):
    primenum=[]
    for i in range(start, stop):
        for j in range(2,i):
            if i%j ==0:
                break
            elif j==i-1 and i%j!=0:
                primenum.append(i)
    yield from primenum
    




start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')