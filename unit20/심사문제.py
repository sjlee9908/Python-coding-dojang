number_begin, number_fin=map(int, input().split())

for i in range(number_begin, number_fin+1):
    if i%35==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)
