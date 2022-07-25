# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_horas = float (input("Informe o valor da suas horas: "))
trab_horas = float (input("Infome as horas trabalhadas no mês:"))

mensal = (trab_horas * valor_horas)
print ("O seu salário mensal foi de:",mensal)