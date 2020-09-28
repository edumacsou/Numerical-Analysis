from baricentrico import *
from utilidades import *
from lagrange import *
from newton import *
from decimal import *
from neville import *
import matplotlib.pyplot as plt


# Definição dos valores dos eixos de interpolação
XsIE = igualmenteEspacados(50 ,-180, 180)
XsCheb = chebyshev(50, -180, 180)
senoIE = list(map(seno, XsIE))
senoCheb = list(map(seno, XsCheb))

# Definição dos pontos a serem usados para os testes
testes = igualmenteEspacados(500 ,-180, 180)
senoTeste = list(map(seno, testes))


######################################################################################


''' Valores igualmente Espaçados '''


# Cálculos  de interpolação com função Seno

lagrangeIE = lagrange (testes, XsIE, senoIE)
baricentricoIE = baricentrico (testes, XsIE, senoIE)
newtonIE = newton (testes, XsIE, senoIE)
nevilleIE = neville (testes, XsIE, senoIE)


# Gráfico 1 : Resultados da interpolação em todos os algoritmos com função seno

plt.figure(1)
plt.subplot(211)
plt.plot(testes, lagrangeIE, color = 'green')
plt.plot(testes, baricentricoIE, color = 'blue')
plt.plot(testes, newtonIE, color = 'red')
plt.plot(testes, nevilleIE, color = 'aqua')
plt.plot(testes, senoTeste, color = 'yellow')
plt.title('Valores igualmente espaçados')
plt.ylabel('Valores Calculados')

# Gráfico 2: Erros entre os algoritmos e os valores esperados

plt.subplot(212)
plt.plot(testes, erro(lagrangeIE, senoTeste), color = 'green')
plt.plot(testes, erro(baricentricoIE, senoTeste), color = 'blue')
plt.plot(testes, erro(newtonIE, senoTeste), color = 'red')
plt.plot(testes, erro(nevilleIE, senoTeste), color = 'aqua')
plt.ylabel('Erro')

#######################################################################################


''' Valores de Chebyshev '''


# Cálculos de interpolação com função Seno

lagrangeCheb = lagrange (testes, XsCheb, senoCheb)
baricentricoCheb = baricentrico (testes, XsCheb, senoCheb)
newtonCheb = newton (testes, XsCheb, senoCheb)
nevilleCheb = neville (testes, XsCheb, senoCheb)


# Gráfico 3: Resultados da interpolação em todos os algoritmos com função seno

plt.figure(2)
plt.subplot(211)
plt.plot(testes, lagrangeCheb, color = 'green')
plt.plot(testes, baricentricoCheb, color = 'blue')
plt.plot(testes, newtonCheb, color = 'red')
plt.plot(testes, nevilleCheb, color = 'aqua')
plt.plot(testes, senoTeste, color = 'yellow')
plt.title('Valores de Chebyshev')
plt.ylabel('Valores Calculados')

# Gráfico 4: Erros entre os algoritmos e os valores esperados

plt.subplot(212)
plt.plot(testes, erro(lagrangeCheb, senoTeste), color = 'green')
plt.plot(testes, erro(baricentricoCheb, senoTeste), color = 'blue')
plt.plot(testes, erro(newtonCheb, senoTeste), color = 'red')
plt.plot(testes, erro(nevilleCheb, senoTeste), color = 'aqua')
plt.ylabel('Erro')

plt.show()