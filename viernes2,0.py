
from datetime import date

#pedimos los valores al usuario
año = int(input("porfavor, introduce el año: "))
mes = int(input("porfavor, introduce el mes: "))

fecha = date( año, mes, 13) #cuadramos la fecha para hallar un viernes 13
dia = fecha.isoweekday() #encontramos el dia de la semana, siendo domingo 0 y sabado 6
if dia == 5:
    print("la fecha:", fecha, "es viernes 13!!")
else: 
    print("la fecha:", fecha, "no es un viernes 13:(")

       

