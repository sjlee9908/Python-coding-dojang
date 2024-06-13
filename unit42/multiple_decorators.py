def decorator1(func):
    def wrapper():
        print('decorator 1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator 2')
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print('hello')

hello()
