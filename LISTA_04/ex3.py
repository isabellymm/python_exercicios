#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


Num_List = []

for i in range(0,4):
    Num_List.append(int(input('Digite as Notas : ')))

media = sum(Num_List) / 4

print('A média foi de :',media)