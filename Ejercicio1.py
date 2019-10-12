peli1=0
peli2=0
peli3=0

menor1=0
menor2=0

print("Ingrese el precio de la pelicula 1: ")
peli1=int(input())
print("Ingrese el precio de la pelicula 2: ")
peli2=int(input())
print("Ingrese el precio de la pelicula 3: ")
peli3=int(input())

if peli1>peli2 and peli1>peli3:
	menor1=peli2
	menor2=peli3
elif peli2>peli1 and peli2>peli3:
	menor1=peli1
	menor2=peli3
elif peli3>peli1 and peli3>peli2:
	menor1=peli1
	menor2=peli2

precio=menor1+menor2
print("La cantidad a pagar es de: $"+ str(precio))