print("Multiplos de un numero en un rango dado (del 10 al 100)")
x=int(input("Ingrese un numero: "))
print("Los multiplos de " + str(x) + " dentro del rango de 10 al 100 son: ")
for i in range(10, 101):
  if i % x == 0:
    print(str(i))