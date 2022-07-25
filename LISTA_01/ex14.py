#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.  
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

peixe = float (input("Informe o peso(kg) do peixe:"))
if peixe >= 50:
  multa = float ((peixe - 50) * 4)
  print ("A multa sera de :",multa,"reais")
else:
  print ("O peixe não ultrapassou o limite")