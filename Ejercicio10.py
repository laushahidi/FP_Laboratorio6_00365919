opcion=0
while opcion != 4:
  print("Conversor de unidades")
  print("(1) Fahrenheit a Celsius")
  print("(2) Celsius a Fahrenheit")
  print("(3) Kelvin a Celsius")
  print("(4) Salir")
  opcion=int(input("Ingrese la opcion: "))
  if opcion == 1:
    print(" ")
    print("Conversor de Fahrenheit a Celsius")
    x=float(input("Ingrese la temperatura en Fahrenheit: "))
    y=float((x-32)*(5/9))
    print(str(x) + "° Fahrenheit = " + str(y) + "° Celsius")
    print(" ")
  elif opcion == 2:
    print(" ")
    print("Conversor de Celsius a Fahrenheit")
    x=float(input("Ingrese la temperatura en Celsius: "))
    y=float(x*(9/5) + 32)
    print(str(x) + "° Celsius = " + str(y) + "° Fahrenheit")
    print(" ")
  elif opcion == 3:
    print(" ")
    print("Conversor de Kelvin a Celsius")
    x=float(input("Ingrese la temperatura en Kelvin: "))
    y=float(x-273.15)
    print(str(x) + "° Kelvin = " + str(y) + "° Celsius")
    print(" ")
  elif opcion != 4:
    print(" ")
    print("Opciones validas de 1 a 4")
    print(" ")
print("Salida exitosa")