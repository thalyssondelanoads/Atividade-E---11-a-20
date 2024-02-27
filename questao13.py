def maior():
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
        print(f' O Maior Número é {num1}')
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
        print(f' O Maior Número é {num2}')
    elif num3 > num2 and num3 > num1 and num3 > num4 and num3 > num5:
        print(f' O Maior Número é {num3}')
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
        print(f' O Maior Número é {num4}')
    else:
        print(f' O Maior Número é {num5}')
    
#-----------------------------

def menor():
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        print(f' O Menor Número é {num1}')
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        print(f' O Menor Número é {num2}')
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        print(f' O Menor Número é {num3}')
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        print(f' O Menor Número é {num4}')
    else:
        print(f' O Menor Número é {num5}')
    
#------------------------------

print('Número Maior e Menor')
print('--------------')

num1 = int(input('Digite o 1º Número: '))
num2 = int(input('Digite o 2º Número: '))
num3 = int(input('Digite o 3º Número: '))
num4 = int(input('Digite o 4º Número: '))
num5 = int(input('Digite o 5º Número: '))
print('--------------')

maior()
menor()
