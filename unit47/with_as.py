class OpenHello:
    def __enter__(self):
        self.file=open=('hello.txt', 'w')
        return self.file
    
    def __exit__(self, exc_type, sec_value, traceback):
        self.file.close()

with OpenHello() as hello:
    hello.write('hello, world!')