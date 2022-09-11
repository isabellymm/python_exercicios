def leiaNumeros(qtdMax):

    numeros = []

    for i in range(qtdMax):
        n = int(input('Digite o '+str(i+1)+'º numero: '))
        numeros.append(n)
    
    return numeros

def mediaPositiva(listaNumeros):
    media = 0
    soma = 0
    qtd=0
    for numero in listaNumeros:
        if (numero > 0):
            soma += numero
            qtd+=1

    media = soma / qtd
    return media

def mediaNegativa(listaNumeros):
    media = 0
    soma = 0
    qtd=0
    for numero in listaNumeros:
        if (numero < 0):
            soma += numero
            qtd+=1

    media = soma / qtd
    return media


lista = leiaNumeros(10)
mediaP = mediaPositiva(lista)
mediaN = mediaNegativa(lista)

print('Medias:')
print('Positiva: ',mediaP)
print('Negativa: ', mediaN)