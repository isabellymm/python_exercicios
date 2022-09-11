

def Cordenadas():


    x1 = int(input('Informe as cordenada de Xa : '))
    y1 = int(input('Informe as cordenadas de Ya : '))
    x2 = int(input('Informe as cordenada de Xb : '))
    y2 = int(input('Informe as cordenada de Yb: '))

    Distancia = ((x2 - x1)**2  + (y2 - y1)**2 ) **(0.5)

    print('A distância entre os pontulos é de : ' ,Distancia)

    

Cordenadas()