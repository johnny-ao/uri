#Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
a = float(input())
b = float(input())
c = float(input())

# Calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 
# e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
media = ((a*2) + (b*3) + (c*5)) / 10

print("MEDIA = %.1f"%(media))