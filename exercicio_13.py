#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_inicial=float(input('Digite o salário do funcionário:'))
aumento=(salario_inicial*15)/100
salario_final=salario_inicial+aumento
print(f'O novo salário, com 15% de aumento, é de {salario_final:.2f}.')