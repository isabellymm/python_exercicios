#Faça um programa que lê as duas notas parciais 
#obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.


nota1 =  float (input("Informe sua nota: "))
nota2 =  float (input("Informe sua nota: "))

nota_media = float ((nota1 + nota2) / 2)


if nota_media >= 9:
   conceito = "A"

elif nota_media >= 7.5:
 conceito = "B"

elif nota_media >= 6:
 conceito = "C"

elif nota_media >= 4:
 conceito = "D"

elif nota_media >= 0:
 conceito = "E"


if conceito == "A" or "B" or "C":
    resultado = "Aprovado!"
elif conceito == "D" or "E":
    resultado = "Reprovado!"

print("NOTA 1 :",nota1)
print("NOTA 2 :",nota2)
print("MÉDIA :",nota_media)
print("CONCEITO :",conceito)



















