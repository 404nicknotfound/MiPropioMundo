import sys
from operaciones import suma, resta, multi, division, potencia

print("CALCULADORA OPERACIONES:\n 1. suma \n 2. Resta \n 3. Multiplicacion \n 4. Division \n 5. Potencia")
operacion = int(input("Porfavor elija el codigo de la operacion: "))

valor1 = int(input("Porfavor introduzca su primer digito: "))
valor2 = int(input("Porfavor introduzca su segundo digito: "))

if operacion == 1:
    print("-----Bienvenido a suma----- ")
    print("Su primer valor es:", valor1, " y su segundo valor es:",valor2)
    print(suma(valor1,valor2))
    quit()
elif operacion == 2:
    print("-----Bienvenido a resta-----")
    print("Su primer valor es:", valor1, " y su segundo valor es:",valor2)
    print(resta(valor1,valor2))
    quit()
elif operacion == 3:
    print("-----Bienvenido a multiplicacion-----")
    print("Su primer valor es:", valor1, " y su segundo valor es:",valor2)
    print(multi(valor1,valor2))
    quit()
elif operacion == 4:
    print("-----Bienvenido a Division-----")
    print("Su primer valor es:", valor1, " y su segundo valor es:",valor2)
    print(division(valor1,valor2))
    quit()
elif operacion == 5:
    print("-----Bienvenido a potencia-----")
    print("Su primer valor es:", valor1, " y su segundo valor es:",valor2)
    print(potencia(valor1,valor2))
    quit()
else:
    print("¡ERROR, SELECCIONE UNA OPERACION VALIDA!!")
