class MakeCalc(type):
    def __new__(metacls, name, bases, namespace):
        namespace['desc']='계산 클래스'
        namespace['add']=lambda self, a, b:a+b
        return type.__new__(metacls, name, bases, namespace)

Calc=MakeCalc('Calc', (), {})

c=Calc()
print(c.desc)
print(c.add(1,2))
