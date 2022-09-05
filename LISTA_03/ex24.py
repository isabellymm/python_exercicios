#Faça um programa que calcule o mostre a média aritmética de N notas.


notas = []

print('Digite [0] para sair do loop')     

while True:
    n = int(input('Informe as notas : '))
    if n ==0:
        break
    notas.append(n)

media_ari = (sum(notas) / len(notas))

print('A média das notas é : ',media_ari)