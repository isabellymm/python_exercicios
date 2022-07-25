#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.


dia = int (input('Informe um búmero correspondente a semana [entre 1 e 7]: '))


if dia == 1 :
    print('Domingo')

elif dia == 2 :
    print('Sugunda')

elif dia == 3 :
    print('Terça')

elif dia == 4 :
    print('Quarta')

elif dia == 5 :
    print('Quinta')

elif dia == 6 :
    print('Sexta')

elif dia == 7 :
    print('Sábado')

else:
    print('Erro : número invalído !')



