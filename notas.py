import sys

notas = [3,2,5,4,3]
total= 0

for nota in notas:
    total+=nota


print(total)
pos=len(notas)
calificacion= total/pos
print("su promedio es de ",calificacion)