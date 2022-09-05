#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.


lista1 = []
lista2 = []
random_lista = []


print('Lista 1 \n')
for i in range(2):
    lista1.append(int(input('Informe  O '+ str(i+1) + 'º' ' número interiro : ' )))
print()
print()
print('Lista 2 \n')
for x in range(2):
    lista2.append(int(input('Informe  O '+ str(x+1) + 'º' ' número interiro : ' )))
    

for index in range(10):
    random_lista.append(lista1[0])
    random_lista.append(lista2[0])
    random_lista.append(lista1[1])
    random_lista.append(lista2[1])

print(lista1)
print(lista2)
print(random_lista)