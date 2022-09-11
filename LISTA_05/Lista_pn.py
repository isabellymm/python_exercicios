#Resolução ---> if dentro de ListaNumeros

def leiaNumeros (qtdMax):
    numeros = []

    for i in range(qtdMax):
        n = int(input('Digite o '+str(i+1)+'º numero: '))
        numeros.append(n)

    return numeros 

def MediaPositiva(ListaNumeros):
    media = 0 
    qtd = 0
    sum = 0
    numero = float

    for numero in ListaNumeros:
        if numero > 0: 
            sum += numero
            qtd +=1

            if qtd == 0:
                break
            else:
                media = sum / qtd
    return media

def MediaNegativa(ListaNumeros):
    media = 0 
    qtd = 0
    sum = 0
    numero = float
    

    for numero in ListaNumeros:
        if numero < 0 : 
            sum += numero
            qtd+=1

            if qtd == 0:
                break
            else:
                media = sum / qtd
    return media

   


lista = leiaNumeros(10)
mediaP = MediaPositiva(lista)
mediaN = MediaNegativa(lista)


print('Medias: ')
print('Positivo' , mediaP)
print('Negativo' , mediaN)