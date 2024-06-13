class Person:
    def __init__(self, name, age, address, wallet):
        self.name=name
        self.age=age
        self.address= address
        self.__wallet=wallet

maria=Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet-=10000
