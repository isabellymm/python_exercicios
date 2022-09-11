from math import sqrt

def inverte_sinal(valor):
    
    invert = valor * -1
    return invert


def soma(termo_1, termo_2):

    sum = termo_1 + termo_2
    return sum

def subtração(minuendo, subtraendo):

    sub = minuendo - subtraendo
    return sub
    
def multiplicação(multiplicando, multiplicador):

    multip = multiplicando * multiplicador
    return multip

def divisao(dividendo, divisor):
    
    div = dividendo / divisor
    return div 

def quadrado(valor):
 
    quad = valor * valor
    return quad

def raiz(valor):

    return sqrt(valor)

def delta(a, b, c):

    return subtração(quadrado(b), multiplicação(multiplicação(4, a), c))

def bhaskara():

    print('=' * 12 + 'Bhaskara' + '=' * 12)
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    r1 = divisao(
        soma(inverte_sinal(b), raiz(delta(a, b, c))),
        multiplicação(2, a))

    r2 = divisao(
        subtração(inverte_sinal(b), raiz(delta(a, b, c))),
        multiplicação(2, a))

    print('Para a equação: ', a, 'x^2 + ', b, 'x + ', c, ' = 0')
    print('As raizes são: ', r1, ' e ', r2)
    print('=' * 32)

bhaskara()