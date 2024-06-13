import math
import collections

Point2D=collections.namedtuple('point2D', ['x','y'])


p1=Point2D(x=30,y=20)
p2=Point2D(x=60, y=50)

a=p2.x-p1.x
b=p2.y-p1.y

c=math.sqrt((a*a)+(b*b))
print(c)
