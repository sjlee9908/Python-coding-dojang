n1,n2=map(int, input().split())
a={i for i in range(1,n1+1) if n1%i==0}
b={i for i in range(1,n2+1) if n2%i==0}





divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)
