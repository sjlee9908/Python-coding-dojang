class Person:
    count =0

    def __init__(self):
        Person.count+=1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다'.format(Person.count))

james=Person()
maria=Person()

Person.print_count()
