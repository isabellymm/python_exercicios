#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.


resposta = input("Informe o periodo em que estuda (V) (M) (N) :")


if resposta == 'V':
    print("Boa Tarde")
elif resposta == 'M':
    print("Bom Dia")
elif resposta == 'N':
    print("Boa Noite")
else:
    print("Inválido")

    