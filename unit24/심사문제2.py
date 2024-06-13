li=input().split(';')
li=map(int, li)
li=list(li)
li.sort(reverse=True)

for i in li:
    print('{0:>9,}'.format(i))

