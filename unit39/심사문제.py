def stot(start):        
    second=start%60
    minute=start//60
    hour =0
    if minute>59:
        hour=minute//60
        minute%=60
        if hour ==24:
            hour=0
    return hour, minute, second

class TimeIterator:
    def __init__(self, start, stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start< self.stop:
            hour, minute, second=stot(self.start)
            self.start+=1
            return "{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)
        else:
            raise StopIteration

    def __getitem__(self, index):
        hour, minute, second= stot(self.start+index)
        return "{0:02d}:{1:02d}:{2:02d}".format(hour, minute, second)






start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')