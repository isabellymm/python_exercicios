#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.


lado1 = float (input("Informe o lado do triãngulo:"))
lado2 = float (input("Informe o lado do triãngulo:"))
lado3 = float (input("Informe o lado do triãngulo:"))

tri_possivel = lado1 + lado2
if tri_possivel > lado3:
    tri_verdadeiro = "O Triangulo é possível!"

else:
    print("O Triangulo não é possível!")

if lado1 == lado2 == lado3:
    tri = "O Triangulo é Equilátero"

elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    tri = "O Triangulo é  Isósceles"

elif lado1 != lado2 != lado3:
    tri =  "Triangulo é Escaleno"



print(tri_verdadeiro)
print(tri)


   
