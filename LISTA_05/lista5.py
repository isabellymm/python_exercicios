soma = 0
lista = []
remove = ["[", "]"]
    
    
for i in range(10):
    n =  int(input('Digite o '+str(i+1)+'º numero: '))


    if n % 3 == 0 or n % 5 == 0:
        lista.append(n)
        soma += n

lista_str = str(lista)


for cont in remove:
    lista_str = lista_str.replace(cont , "")


resultado = print((lista_str).replace(',' , ' +') , '=' , soma)


