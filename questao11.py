def opçao_num():
    if opçao > 3 or opçao <1:
        print('Inválido, digite uma opção de 1 a 3!')
    elif opçao == 1:
        print(f' A opção escolhida foi o número {num1}')
    elif opçao == 2:
        print(f' A opção escolhida foi o número {num2}')
    else:
        print(f' A opção escolhida foi o número {num3}')

#-----------------------------

print('Valor da Opção')
print('--------------')

opçao = int(input('Digite a opção de 1 a 3: '))
num1 = int(input('Digite o 1º Número: '))
num2 = int(input('Digite o 2º Número: '))
num3 = int(input('Digite o 3º Número: '))
print('--------------')

opçao_num()
