from numpy import*
def gaussjordan1(a,b):
    n = len(b)
    c = concatenate([a,b,d],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
                    print(c[i,j])
    x=c[:,n]
    return x

def gaussjordan2(a,b):
    n = len(b)
    c = concatenate([a,b],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+n):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
                    print(c[i,j])
    x=c[:,n]
    return x

def gaussjordanIn(a,b):
    n = len(b)
    I=identity(n)
    c = concatenate([a,b],axis = 1)
    c = concatenate([c,I],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,2*n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,2*n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    Inv=c[:,n+1:]
    return Inv

def Gauss1(a,b):
    n = len(b)
    c = concatenate([a,b],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range(e,n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    print(c)
    for i in range (n,1):
        x = 0
        for j in range(i,n):
            x = x + 
