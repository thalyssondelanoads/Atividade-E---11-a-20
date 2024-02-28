def media_maior():
    media = (num1 + num2 + num3 + num4 + num5) / 5
    
    print(f' A Média dos Números é {media} ')
    print('__________')
    print(' Os Números maiores que a Média são: ')
    if num1 > media:
        print(f'--> {num1} ')
    if num2 > media:
        print(f'--> {num2} ')
    if num3 > media:
        print(f'--> {num3} ')
    if num4 > media:
        print(f'--> {num4} ')
    if num5 > media:
        print(f'--> {num5} ')
    
#-------------------------------

print('Média e Números maiores que a Média!')
print('-----------')

num1 = int(input('Digite o 1° Número: '))
num2 = int(input('Digite o 2° Número: '))
num3 = int(input('Digite o 3° Número: '))
num4 = int(input('Digite o 4° Número: '))
num5 = int(input('Digite o 5° Número: '))
print('-----------')

media_maior()
