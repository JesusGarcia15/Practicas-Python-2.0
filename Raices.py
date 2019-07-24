#Esta funcion realiza la biseccion de una grafica
import numpy as np
def f(x):
    return x - np.sin(x)
a = -2
b = 2
error = 0.1
while error > 1e-8:
    c = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fc = f(c)
    if fc == 0:
        raiz = c
        break
    elif fa * fc < 0:
        b = c
    elif fb * fc < 0:
        a = c
    raiz = c
    error = abs(fc)
print(raiz)

#Esta funcion realiza el metodo Newton Raphson
def f(x):
    return x**4 - 10*x**3 + 3*x**2 + x + 23
def Df(x):
    return 4*x**3 - 30*x**2 + 6*x + 1
x0 = 9#se realiza un cambio para encontrar el primer punto
i = 1
error = ((x0 - x0+1))/ x0
while error > 1e-8:
    x1 = x0 - f(x0) / Df(x0)
    x0 = x1
    print('Interacion', i, "raiz aproximada: ", x0)
    i +=1
    break
