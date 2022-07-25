#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.



hora = int (input("Informe o total de suas horas trabalhadas:"))
valor_hora = float (input("Informe o valor de suas horas trabalhadas:"))

salario_bruto = (hora * valor_hora)

if (salario_bruto == 0 ):
    print("ERRO")

elif (salario_bruto <= 900):
   desconto_ir = 0

elif (salario_bruto <= 1500):
    desconto_ir = 5

elif (salario_bruto <= 2500):
    desconto_ir = 10

elif (salario_bruto > 2500):
    desconto_ir = 20

desconto_inss = 10
desconto_fgts = 11

ir = salario_bruto * (desconto_ir/100)
inss = salario_bruto * (desconto_inss/100)
fgts = salario_bruto * (desconto_fgts/100)
total_desconto = (inss + ir)
salario_liquido = (salario_bruto - inss - ir )

print()
print()
print("--------------------------------------------")
print("-------------------TABELA-------------------")
print("O salario Bruto : R$",salario_bruto)
print("(-) IR: R$",ir,)
print("(-) INSS: R$",inss,)
print("FGTS : R$",fgts,)
print("Total de descontos : R$",total_desconto)
print("Salário Liquido : R$",salario_liquido)
print("--------------------------------------------")
print()
print()