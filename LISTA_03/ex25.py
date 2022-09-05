#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
#se a média de idade da turma varia entre 1 e 25 ,26 e 60 e maior que 60; e então,
#dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.


idade = []

print('Digite [0] para sair do loop') 


while True:
    n = int(input('Informe as idades : '))
    if n == 0:
        break
    idade.append(n)

media_id = (sum(idade)) / len(idade)


print('A média das idade do grupo é :',media_id)
if media_id >= 1 and media_id <= 25:
    print('Jovem!')

elif media_id >= 26 and media_id <= 60:
    print('Adulto!')

elif media_id > 60:
    print('Idosa!')