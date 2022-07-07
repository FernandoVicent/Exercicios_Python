# Você tem uma aplicação financeira de 10 mil reais, que rende 0,7% ao mês.
# Você deseja comprar um carro de 12 mil reais, mas o preço do carro sobe à taxa de 0,4% ao mês.
# Escreva um programa que calcule quantos meses levará até que, com essa aplicação, você tenha dinheiro suficiente para comprar o carro à vista.
import time

aplic_financeiro = 10000
renda_mes = 1.007
mes = 0
valor_carro = 12000
taxa_carro = 1.004


while aplic_financeiro <= valor_carro:

    mes += 1
    aplic_financeiro = round(aplic_financeiro*renda_mes)
    valor_carro = round(valor_carro*taxa_carro)
    print(f"valor em conta: {aplic_financeiro}")
    print(f"valor do carro: {valor_carro}")
print(f"Em {mes} meses o valor de sua aplicação passou o valor do carro")