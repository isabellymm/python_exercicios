#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print ('Informe a data no formato dd/mm/aaaa : ')
dia = int (input('Dia -->    '))
mes = int (input('Mês -->    '))
ano = int (input('Ano -->    '))

valid = True 

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or \
    mes == 10 or mes ==12:
    ultimo_dia = 31  
    valid = True

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    ultimo_dia = 30
    valid = True 

elif mes == 2:
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        ultimo_dia = 29
    else: ultimo_dia = 28
    
if dia < 1 or dia > ultimo_dia:
    valid = False

if (valid):
    print("Data : ",dia,"/",mes,"/",ano)
else:
    print('Data Inválida')