#Faça um programa que leia o nome de um vendedor, 
# o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, 
# informar o total a receber no final do mês, com duas casas decimais.
name = raw_input()
salary = float(input())
sales = float(input())

commission = sales * 0.15

total = commission + salary

print("TOTAL = R$ {:.2f}".format(total))