# quanto vc ganha por hora (input) e os numeros de horas trabalhadas
# Calcule e mostre o total do seu salário no referido mês
# descontados 11% para o Imposto de Renda
# 8% para o INSS 
# 5% para o sindicato
#alário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
# o salário líquido.
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valor = float (input ("Informe o valor recebido por hora: "))
hora = float (input ("Informe o total de horas trabalhadas por mês: "))

salario_bruto = float (valor * hora)
imposto = float ( salario_bruto * (11/100))
inss = float (salario_bruto * (8/100))
sind = float (salario_bruto * (5/100))
salario_liquido = (salario_bruto - imposto - inss - sind)
print ("                      TABELA                       ")
print ("---------------------------------------------------")
print ("+ Salário Bruto : R$",salario_bruto)
print ("- IR (11%) : R$",imposto)
print ("- INSS (8%) : R$",inss)
print ("- Sindicato ( 5%) : R$",sind)
print ("= Salário Liquido : R$",salario_liquido)
print ("---------------------------------------------------")