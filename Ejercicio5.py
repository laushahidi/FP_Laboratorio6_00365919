i=1000
x=0
c="¿Cuanto desea retirar? $"
q="¿Cuanto desea depositar? $"
m="La transacción ha sido exitosa. Su saldo actual es: $"
n="No tiene suficiente saldo en su cuenta, por favor digite otra cantidad. Su saldo actual es: $"
nv="Caracter invalido. " 
print("CAJERO AUTOMATICO")
print("Saldo actual: $" + str(i))
t=str(input("¿Que desea realizar? Retiro (r) - Deposito (d) - Salir (s): "))

while t != 's' and t != 'S':
  if (t == "r" or t == "R") and i > 0:
    x=float(input(c))
    if x <= i:
      i=i-x
      z=str(m) + str(i)
    else:
        z=str(n) + str(i)
  elif t == "d" or t == "D":
    x=float(input(q))
    i=i+x
    z=str(m) + str(i)
  else:
    z=nv
  print(z)
  if i == 0:
    t=str(input("¿Que desea realizar? Deposito (d) - Salir (s): "))
  else:
    t=str(input("¿Que desea realizar? Retiro (r) - Deposito (d) - Salir (s): "))
if t == "s" or t == "S":
  print("Salida exitosa")