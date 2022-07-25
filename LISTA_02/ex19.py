#Faça um Programa que leia um número inteiro menor que 1000 
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.

numero = int(input('Digite um numero inteiro positivo: '))

unidade = numero % 10

numero = (numero - unidade)/10
dezena = numero % 10

numero = (numero - dezena)/10
centena = numero

dezena = int(dezena)
centena = int(centena)
print(centena,'centena(s),',dezena,'dezena(s) e',unidade,'unidade(s)')
