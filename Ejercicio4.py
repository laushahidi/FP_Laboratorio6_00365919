from random import * 
print("Juego: adivina un número aleatorio")
n=int(input("Piensa e ingresa un número del 1 al 10: "))
m=randrange(1,10)
k=0
while n != m:
  if n > m:
    print("El numero ingresado es mayor al numero aleatorio")
    k+=1
    n=int(input("Piensa e ingresa otro número del 1 al 10: "))
  elif n < m:
    print("El numero ingresado es menor al numero aleatorio")
    k+=1
    n=int(input("Piensa e ingresa otro número del 1 al 10: "))
if n == m:
  print("¡Adivinaste!")
  print("Número de intentos: ")
  k=k+1
  print(int(k))