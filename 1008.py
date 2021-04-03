#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, 
# o valor que recebe por hora e calcula o salário desse funcionário. 
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
number = int(input())
hour = int(input())
valueHour = float(input())

salary = hour * valueHour

print("NUMBER = {0}".format(number))
print("SALARY = U$ {:.2f}".format(salary))