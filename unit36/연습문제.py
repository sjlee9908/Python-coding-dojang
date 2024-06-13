class AdvancedList(list):
    def replace(self, old, new):
        self[self.index(old)]=new



x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)
