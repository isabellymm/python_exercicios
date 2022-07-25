#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

alt = (input('Informe a sua altura : '))

homem = (72.7 * alt) - 58
mulher = (62.1 * alt ) - 44.7

print('Seu peso ideal se for homem é de :',homem)
print('Seu peso ideal se for mulher de :',mulher)