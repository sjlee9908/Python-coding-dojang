x = 10
y = 3

def get_quotient_remainder(x,y):
    return x//y, x%y


quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
