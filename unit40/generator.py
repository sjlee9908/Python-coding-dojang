def number_generation(stop):
    n=0
    while n<stop:
        yield n
        n+=1

for i in number_generation(3):
    print(i)