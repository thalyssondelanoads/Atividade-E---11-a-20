def imc():
    imc = (peso / altura**2)
    
    if imc < 25:
        print(f' Seu IMC é {imc:.2f} : Peso Normal ')

    elif 25 <= imc <= 30:
        print(f' Seu IMC é {imc:.2f} : Obesidade ')

    else:
        print(f' Seu IMC é {imc:.2f} : Obesidade Mórbida')

#--------------------------------

print('Calculadora de IMC ')
print('-------')

altura = float(input(' Qual sua altura? : '))
peso = float(input(' Qual seu peso? : '))
print('-------')

imc()
