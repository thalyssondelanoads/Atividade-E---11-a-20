def quadrante():
    if 0 < angulo < 90:
        print('O Ângulo está no Q1')
    
    elif 90 <= angulo < 180:
        print('O Ângulo está no Q2')
    
    elif 180 <= angulo < 270:
        print('O Ângulo está no Q3')
    
    elif 270 <= angulo <= 360:
        print('O Ângulo está no Q4')
        
    else:
        print(' Essa Medida de Ângulo NÃO existe')
    
#--------------------------------

print('Quadrante de uma Medida de Ângulo')
print('------------')

angulo = float(input('Digite a Medida do Ângulo: '))
print('------------')

quadrante()
