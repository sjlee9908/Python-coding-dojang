def number_coroutine():
    try:
        while True:
            x=(yield)
            print(x, end=' ')
    except GeneratorExit:
        print('')
        print('코루틴 종료')

co=number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()