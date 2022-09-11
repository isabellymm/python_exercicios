parar = ''
while parar != 'S':

    diabetes = input('É diabético  [S/N] : ')
    if diabetes == 'S':
        print('Remédio não recomendado')
        break
    gestante = input('É gestante [S/N] : ')
    if gestante == 'S':
        print('Remédio não recomendado')
        break
    else:
    
        sexo = input('Sexo [F/M] : ')
        idade = int(input('Informe a idade :'))
        peso = float(input('Informe o Peso : '))
        temperatura = float(input('Informe a temperatura : '))

        
    if sexo == 'F':
        
        if idade < 7:
            print('Idade menor que 7, programa não dara a dosagem!')

        elif idade >= 7 and idade <= 18:
            
            if temperatura < 37:
                print('Temperatura menor que 37, programa não dara a dosagem!')

            elif temperatura >= 37 and temperatura <= 37.9:
                gotas = peso / 6
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura >= 38 and temperatura <= 39.9:
                gotas = peso / 4                                          
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura > 39.9:
                gotas = peso / 3 
                print('Dosagem:' ,gotas, 'gotas')


    if sexo == 'F':

        if idade > 19 :

            if temperatura < 37:
                print('Temperatura menor que 37, programa não dara a dosagem!')
        
            elif temperatura >= 37 and temperatura <= 37.9:
                gotas = peso / 4
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura >= 38 and temperatura <= 39.9:
                gotas = peso / 3
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura > 39.9:
                gotas = peso / 2
                print('Dosagem:' ,gotas, 'gotas')

    if sexo == 'M':

        if idade < 7:
            print('Idade menor que 7, programa não dara a dosagem!')

        elif idade >= 7 and idade <= 18:

            if temperatura < 37:
                print('Temperatura menor que 37, programa não dara a dosagem!')

            elif temperatura >= 37 and temperatura <= 37.9:
                gotas = peso / 5
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura >= 38 and temperatura <= 39.9:
                gotas = peso / 4
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura > 39.9:
                gotas = peso / 2
                print('Dosagem:' ,gotas, 'gotas')

    if sexo == 'M':

        if idade > 19 :

            if temperatura < 37:
                print('Temperatura menor que 37, programa não dara a dosagem!')
        
            elif temperatura >= 37 and temperatura <= 37.9:
                gotas = peso / 4
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura >= 38 and temperatura <= 39.9:
                gotas = peso / 3
                print('Dosagem:' ,gotas, 'gotas')

            elif temperatura > 39.9:
                gotas = peso / 1
                print('Dosagem:' ,gotas, 'gotas')

    parar = input('Parar programa! -->[S/N] :')
    