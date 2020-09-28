from decimal import *
import functools as fn

def newton (x, Xs, Ys):
    F = diferencasDivididas(Xs, Ys)
    ptos = []
    for v in x:
        p = F[0]
        for i in range(1, len(F)):
            p += Decimal(F[i] * fn.reduce(lambda a,b: a*b, [v-xi for xi in Xs[0:i]]))
        ptos.append(p)
    return ptos


def diferencasDivididas(Xs, Ys):
    M = []
    M.append([[]])
    for i in range (1, len(Xs)+1):
        M.append([[]])
        M[i].append(Ys[i-1])
    
    for j in range (2, len(Xs)+1):
        for i in range (1, len(Xs)-j+2):
            M[i].append(Decimal(1/(Xs[i+j-2]-Xs[i-1]))*(M[i+1][j-1]-M[i][j-1]))
    return M[1][1:]