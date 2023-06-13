#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
numero=int(input('Digite o número que você gostaria de saber a tabuada:'))
for i in range(1,11):
    resultado=numero*i
    print(f'{numero} x {i} = {resultado}')