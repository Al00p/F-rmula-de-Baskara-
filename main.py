import math

print("FÓRMULA DE BASKARA")
print("Este programa tem a única utilidade de facilitar sua vida :)")

a = float(input("Qual o valor de A? "))
b = float(input("Qual o valor de B? "))
c = float(input("Qual o valor de C? "))


while a == 0:
  print("A NÃO PODE SER NULO OU NEGATIVO!")
  a = int(input("Qual o valor de A? "))

delta = b**2 - 4*a*c

if delta < 0: 
  print("Δ NÃO PODE SER NEGATIVO!")
else:
  raizdelta = math.sqrt(delta)

  x = ((-b) + raizdelta)/2*a
  y = ((-b) - raizdelta)/2*a

  print(a,"X²+ ",b,"X + ",c)

  print("X' da equação é: ",round(x,2))
  print("X'' da equação é: ",round(y,2))
