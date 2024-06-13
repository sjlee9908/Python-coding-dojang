def calc():
    expression=(yield)
    while True:
        num1, oper, num2=expression.split(' ')
        num1=int(num1)
        num2=int(num2)
        if oper=='+': expression=(yield num1+num2)
        elif oper=='-': expression=(yield num1-num2)
        elif oper=='*': expression=(yield num1*num2)
        elif oper=='/': expression=(yield num1/num2)

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()