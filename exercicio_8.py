#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor_em_metros=float(input('Digite o valor em metros:'))
cm=valor_em_metros*100
mm=valor_em_metros*1000
print(f'{valor_em_metros} equivale a {cm:.2f} centímetros e {mm:.2f} milímetros.')