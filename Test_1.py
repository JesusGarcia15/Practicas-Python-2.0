from numpy import*
a = array([[4,2,5],[2,5,8],[2,4,3]], float)
print(a)
print("")
b = array([[18.0],[27.30],[16.20]], float)
print(b)
print("")
d = array([[1,0,0],[0,1,0],[0,0,1]], float)
print(d)
print("")
c = concatenate([a,b,d],axis=1)
print(c)
print("")
c[0,0:]=c[0,0:]/c[0,0]
print(c)
print("")
c[1,0:]=c[1,0:]-c[1,0]*c[0,0:]
c[2,0:]=c[2,0:]-c[2,0]*c[0,0:]
print(c)
print("")
c[1,1:]=c[1,1:]/c[1,1]
print(c)
print("")
c[0,1:]=c[0,1:]-c[0,1]*c[1,1:]
c[2,1:]=c[2,1:]-c[2,1]*c[1,1:]
print(c)
print("")
c[2,2:]=c[2,2:]/c[2,2]
print(c)
print("")
c[0,2:]=c[0,2:]-c[0,2]*c[2,2:]
c[1,2:]=c[1,2:]-c[1,2]*c[2,2:]
print(c)
print("")
x=c[:,3]
print(x)
print("")
r=dot(a,x)
print(r)


from Lineal import gaussjordan2
a = array([[4,2,5],[2,5,8],[2,4,3]], float)
b = array([[18.00],[27.30],[16.20]], float)
print(gaussjordan2(a,b))
