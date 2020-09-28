from decimal import *
getcontext().prec = 20

def neville (x,Xs,Ys):
    ptosNeville = []
    for v in x:
        M=[]
        for i in range(len(Xs)):
            M.append([])
            for k in range(i):
                M[i].append([])
            for j in range(i, len(Xs)):
                if i == 0:
                    M[i].append(Ys[j])
                else:
                    p1 = (v - Xs[j-i])*M[i-1][j]
                    p2 = (v - Xs[j])*M[i-1][j-1]
                    M[i].append((p1-p2)/(Xs[j]-Xs[j-i]))
        tam1 = len(M)-1
        ptosNeville.append(M[tam1][tam1])
    return ptosNeville



''' Método Recursivo (Muito Demorado)

def neville(x, Xs, Ys):
    neville = []
    for v in x:
        neville.append(P(v, Xs, Ys, 0, len(Xs)-1))
    return neville

def P(x, Xs, Ys, i, j):
    print('P({},{}) OK'.format(i, j))
    if i == j:
        return Ys[i]
    return ((x-Xs[j])*P(x, Xs, Ys, i, j-1) - (x-Xs[i])*P(x, Xs, Ys, i+1, j))/Xs[j]-Xs[i]
'''