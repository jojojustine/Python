#First Duplicate
from array import *

a = array('i',[1,2,3,4])
print(a)
for i in a:
    print(i)

a.append(5)
print(a)
print(len(a))
del a[0]
print(a)
a.pop()
print(a)
a[2:3] = array('i',[1])
print(a)

