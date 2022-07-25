#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


x = int (input("Digite um número: "))

if x > 0:
    print ("Esse número é positivo!")
elif x == 0:
    print("Esse número é 0!")
else:
    print("Esse número é negativo!")