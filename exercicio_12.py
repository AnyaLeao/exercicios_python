#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço_inicial=float(input('Preço do produto:'))
desconto=(preço_inicial*5)/100
novo_preço=preço_inicial-desconto
print(f'O preço do produto com 5% de desconto fica {novo_preço:.2f}. Desconto de {desconto}')