from math import *
from decimal import *
import numpy as np

# getcontext().prec define a quantidade de casas decimais a calculadas com precisão 
getcontext().prec = 8
# define novo valor pi com uma precisão maior que a nativa na biblioteca math
pi = Decimal('3.141592653589793238462643383279502884197169399375')

# Gera valores igualmente espaçados
def igualmenteEspacados(n, inicio = 0, fim = 1):
    ptos = []
    intervalo = Decimal(Decimal(fim-inicio)/(n-1))
    for j in range(n):
        ptos.append(Decimal(inicio+j*intervalo))
    return ptos

# Gera valores com espaçamento de Chebychev
def chebyshev(n, inicio = 0, fim = 0):
    if n == 1:
        return Decimal((fim-inicio)/2)
    cheb = list(map(cos, np.arange(0, pi+pi/(n-1), pi/(n-1))))
    if not(inicio == 0 and fim == 0):
        intervalo = (fim-inicio)/2
        cheb = list(map(lambda x: inicio+intervalo+x*intervalo, cheb))
    return list(map(Decimal, cheb))


# Calcula valores de polinomios de 3º grau
def valoresPoli3(n, inicio, fim, a = [2, -7, -22, 8]):
    Ys = []
    Xs = []
    intervalo = Decimal(Decimal(fim-inicio)/(n-1))
    for i in range(n):
        Xs.append(Decimal(inicio+(i*intervalo)))
    
    for j in Xs:
        aux = Decimal(0.0)
        aux += a[0] * (j ** 3)
        aux += a[1] * (j ** 2)
        aux += a[2] * j
        aux += a[3]
        Ys.append(aux)
    return Xs, Ys

# função sin() para graus
def seno(numDec):
    numRad = Decimal(pi/180)*Decimal(numDec)
    return Decimal(sin(numRad))

# Cálculo do erro entre duas séries de valores
def erro(x, y):
    if len(x) != len(y):
        print('Erro: quantidade diferente de elementos')
        exit()
    erros = []
    for i in range(len(x)):
        erros.append(np.abs(y[i]-x[i]))
    return erros