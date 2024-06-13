def A():
    x=10
    def B():
        x=20
    B()
    print(x)

A()
