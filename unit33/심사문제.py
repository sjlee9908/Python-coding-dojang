def countdown(n):
    def count():
        nonlocal n
        n-=1
        return n+1
    return count

    
n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
