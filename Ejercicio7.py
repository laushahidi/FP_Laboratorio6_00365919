print("Cuadrilatero de asteriscos")
n=int(input("Ingrese un numero: "))
a="*"
for i in range(0, n):
  for j in range(0, n):
    print(a, end= "")
  print()