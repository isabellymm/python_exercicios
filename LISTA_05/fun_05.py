def JurosCompostos ():
    
    C = float(input('Informe o Valor Total : '))
    i = float(input('Taxa de Juros [Anual] : '))
    n = int (input('Periodo em Anos : '))

    Montante = C * (1 + i/100)**n

    return Montante


juros_comp = JurosCompostos()
print(juros_comp)
