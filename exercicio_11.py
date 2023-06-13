#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litrode tinta pinta uma área de 2m².
largura=float(input('Digite a largura da parede:'))
altura=float(input('Digite a altura da parede:'))
area=largura*altura
quantidade_de_tinta=area/2
print(f'Será necessário {quantidade_de_tinta:.2f} litros de tinta.')
