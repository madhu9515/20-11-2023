s=(1,2,3,4,5,6,7,8)
x=list(filter(lambda n:n-2, s))
print(x)
y=list(filter(lambda n:n%2==0, s))
print(y)
z=list(filter(lambda n:n*2==12, s))
print(z)
