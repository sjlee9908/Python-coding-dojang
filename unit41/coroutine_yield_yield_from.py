def number_coroutine():
    x=None
    while True:
        x=(yield x)
        if x==3:
            return x

def print_coroutine():
    while True:
        x=yield from number_coroutine()
        print('print_coroutine:', x)

co=print_coroutine()
next(co)

x=co.send(1)
print(x)

x=co.send(2)
print(x)

co.send(3)