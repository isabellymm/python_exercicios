#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.


lista = []

for n in range(0,5):
    lista.append(int(input("Dgite 5 números: ")))

print(max(lista))