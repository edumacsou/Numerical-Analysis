from decimal import *
getcontext().prec = 20


def calcW(Xs):
    w = []
    for j in range(0, len(Xs)):
        produto = Decimal(1)
        for k in range(0, len(Xs)):
            if j != k:
                produto *= Decimal(Xs[j]-Xs[k])
        w.append(Decimal(1/produto))
    return w


def somatorioBaricentrico (x, Xs, w):
    somatorio = Decimal(0)
    for j in range(0, len(Xs)):
        somatorio += Decimal(w[j]/(x-Xs[j]))
    return somatorio


def baricentrico (x, Xs, Ys):
    resultado = []
    validador = 0
    w = calcW(Xs)
    for v in x:
        indice = 0
        i = 0
        while i < len(Xs):
            if v == Xs[i]:
                indice = i
                validador = 1
            i += 1
        if validador:
            resultado.append(Ys[indice])
            validador = 0
        else:
            p = somatorioBaricentrico (v, Xs, w)
            somatorio = Decimal(0)
            for j in range(0, len(Xs)):
                somatorio += Decimal((w[j]/(v-Xs[j]))*Ys[j])
            resultado.append(Decimal(somatorio/p))
    return resultado