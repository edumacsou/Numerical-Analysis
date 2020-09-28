from decimal import *
getcontext().prec = 20

def L(x, Xs, i):
    produto = 1
    for k in range(len(Xs)):
        if k != i:
            produto *= Decimal((x-Xs[k])/(Xs[i]-Xs[k]))
    return produto

def lagrange (x, Xs, Ys):
    lagrange = []
    for v in x:
        resultado = Decimal(0)
        for i in range(len(Ys)):
            resultado += Decimal(Ys[i]*L(v, Xs, i))
        lagrange.append(resultado)
    return lagrange