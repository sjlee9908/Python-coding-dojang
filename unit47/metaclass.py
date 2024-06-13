def replace(self, old, new):
    while old in self:
        self[self.index(old)]=new
    
AdvancedList=type('AdvencedList', (list, ), {'desc':'향상된 리스트', 'replace': replace})

x=AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1,100)
print(x)
print(x.desc)