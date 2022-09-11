
#for i in range(0,6):
#
#    for j in range(0,6-i):
#        print('*',end="")
#    print()
# 

tam_num = int(input('Informe um número impar : '))


if tam_num % 2 == 1:
    
    for a in range(1,tam_num+1):

        for b in range(1,a+1):
            print('*', end='')
        print()

    #for c in range(0,tam_num):
#
    #    for d in range(0,tam_num-c):
    #        print('*',end='')
    #    print()

else:
    print('número informado não é impar!')






