import turtle as t

n=6
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(n):
    t.fd(100)
    t.rt(360/n)
t.end_fill()
