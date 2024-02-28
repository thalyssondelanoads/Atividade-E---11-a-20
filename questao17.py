def resto_calculo():
    if num2 == 0 or num1 == 0 or num1 == num2:
        num1_quadrado = num1 ** 2
        num2_quadrado = num2 ** 2
        print(f' O Quadrado do 1º Número = {num1_quadrado} ')
        print(f' O Quadrado do 2º Número = {num2_quadrado} ')
    
    elif num1 % num2 == 1:
        result1 = num1 + num2 + 1
        print(f' A soma {num1} + {num2} + Resto da divisão({1}) = {result1} ')
    
    elif num1 % num2 == 2:
        if num1 % 2 == 0:
            print(' O 1º Número é Par ')
        else:
             print(' O 1º Número é Impar ')
        if num2 % 2 != 0:
            print(' O 2º Número é Impar ') 
        else:
             print(' O 2º Número é Par ')
    
    elif num1 % num2 == 3:
        result3 = (num1 + num2) * num1
        print(f' A soma ({num1} + {num2}) x {num1} = {result3} ')
    
    elif num1 % num2 == 4 and num2 != 0:
        result4 = (num1 + num2) / num2
        print(f' A soma de {num1} + {num2} / {num2} = {result4:.2f}')
        
#---------------------------

print('Operações')
print('------------')

num1 = int(input('Digite um Número Inteiro: '))
num2 = int(input('Digite outro Número Inteiro: '))
print('------------')

resto_calculo()
