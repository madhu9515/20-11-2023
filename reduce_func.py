from functools import reduce
l=[1,2,3,4,5]
x=reduce(lambda a,b:a+b,l)
print(x)

print('-- reduce function takes 2 arguments as parameters one is function ,another is varibkle we are given')
print('-- number of inputs and outputs are different')
from functools import reduce
ll=[1,2,3,4,5]
xx=reduce(lambda a,b:a if a%2==0 else b)
print(xx)


