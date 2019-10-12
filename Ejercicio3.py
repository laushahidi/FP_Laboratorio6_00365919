print("CUENTA PARES (1)")
seguir=bool(True)
pares=0
while seguir:
  n=int(input("Escriba un número par: "))
  while n % 2 != 0:
    n=int(input(str(n) + " no es un número par. Inténtelo de nuevo: "))
  if n % 2 == 0:
    pares=pares+1
  r=str(input("¿Quiere escribir otro número par? (S/N): "))
  while r != "S" and r != "s" and r != "N" and r!= "n":
    r=str(input("Respuesta incorrecta. ¿Quiere escribir otro número par? (S/N): "))
  seguir=(r=="S" or r=="s")
print("Ha escrito " + str(pares) + " números pares.")