def sum_coroutine():
    try:
        total=0
        while True:
            x=(yield)
            total+=x
    except RuntimeError as e:
        print(e)
        yield total

co=sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))
