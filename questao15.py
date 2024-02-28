def salario():
  salario1 = hora_aula1 * valor_hora1
  salario2 = hora_aula2 * valor_hora2

  print(f' Salário do Profº 1 = {salario1:.2f} Reais')
  print('------------')
  print(f' Salário do Profº 2 = {salario2:.2f} Reais')
  print('------------')
  
  if salario1 > salario2:
      print(' O Maior Salário é do Profº 1')
  elif salario2 > salario1:
      print(' O Maior Salário é do Profº 2')
  else:
      print(' 0s Salários são Iguais')
      
#----------------------------

print('Comparação de Salários')
print('------------')

hora_aula1 = float(input('Horas de Aula do 1° Professor: '))
valor_hora1 = float(input('Valor por Hora de Aula do 1° Professor: '))
print('------------')

hora_aula2 = float(input('Horas de Aula do 2° Professor: '))
valor_hora2 = float(input('Valor por Hora de Aula do 2° Professor: '))
print('------------')

salario()
