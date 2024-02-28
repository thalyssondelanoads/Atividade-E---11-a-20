def valores():
    print(' ADIÇÃO - 1')
    print(' SUBTRAÇÃO - 2')
    print(' MULTIPLICAÇÃO - 3')
    print(' DIVISÃO - 4')
    
#---------------------------    
    
def calculos():
    if operaçao == 1:
        soma = num1 + num2 
        print(f' {num1} + {num2} = {soma} ')
    
    elif operaçao == 2:
        subt = num1 - num2
        print(f' {num1} - {num2} = {subt} ')
    
    elif operaçao == 3:
        mult = num1 * num2
        print(f' {num1} x {num2} = {mult} ')
    
    elif operaçao == 4:
        div = num1 / num2
        print(f' {num1} / {num2} = {div:.2f} ')
        
#---------------------------

print('Calculadora Simples')
print('------------')

valores()

print('------------')
num1 = int(input('Digite o 1º Número: '))
operaçao = int(input('Digite o Número da Operação que deseja: '))
num2 = int(input('Digite o 2º Número: '))
print('------------')

calculos()
