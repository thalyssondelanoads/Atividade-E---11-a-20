def aprovação():
    media = (nota1 + nota2) / 2
    
    if media >= 7:
        print(f'--> Média: {media:.2f} - Aprovado')
    elif media < 7:
        print(f'--> Média: {media:.2f} - Prova Final')
        print('------------')
        prova_final = float(input('Digite a Nota da Prova Final: '))
        
        nota_final = (media + prova_final) / 2
        
        print('------------')
        if nota_final >= 5:
            print(f'--> Média: {nota_final:.2f} - Aprovado')
        else:
            print(f'--> Média: {nota_final:.2f} - Reprovado')

# ---------------------------

print('Aprovado ou Reprovado')
print('------------')

nota1 = float(input('Digite a Nota 1: '))
nota2 = float(input('Digite a Nota 2: '))
print('------------')

aprovação()
