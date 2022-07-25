#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


arquivo = float (input("Informe o tamanho do arquivo para download ( em MB) :"))
velocidade = float (input('Informe a velocidae de sua internet (em MBPS) : '))

tempo = arquivo / velocidade 
minuto = tempo / 60

print ('O tempo aproximado para download do arquivo usando este link e de: %.2f minutos'%minuto)