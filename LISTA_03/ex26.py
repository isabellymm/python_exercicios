#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.



eleitores = []
votos = []
cand1 = 0
cand2 = 0
cand3 = 0

eleitores =int(input('Qual o número total de eleitores : '))
print()
print('Pra votar nos candidatos')
print()
print('Candidato 1 --> [1]')
print('Candidato 2 --> [2]')
print('Candidato 3 --> [3]')
print()


for n in range(eleitores):
    votos.append(int(input('Voto do ' + str(n+1) + 'º' ' eleitor : ' '\n')))




for num in votos:
    if num == 1:
        cand1 += 1

    elif num  ==2:
        cand2 += 1
    
    elif num == 3:
        cand3 += 1

print('==' * 15 + 'Resultado' + '==' * 15)

print('Candidato 1 recebeu ',cand1,' votos')
print('Candidato 2 recebeu ',cand2,' votos')
print('Candidato 3 recebeu ',cand3,' votos')
