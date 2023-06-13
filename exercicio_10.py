#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Dia 13/06/2023 - 1 Dólar = 4,86 Real brasileiro
quantidade_em_Real=float(input('Digite a quantidade de dinheiro, em Reais:'))
valor_em_dolar=quantidade_em_Real/4.86
print(f'Você possui {valor_em_dolar} dólares.')
