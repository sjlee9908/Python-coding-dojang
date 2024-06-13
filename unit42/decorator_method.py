def trace(func):
    def wrapper(self, a,b):
        r=func(self, a, b)
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a,b,r))
        return r
    return wrapper

class Calc:
    @trace
    def add(self, a, b):
        return a+b
    
c=Calc()
print(c.add(10,20))