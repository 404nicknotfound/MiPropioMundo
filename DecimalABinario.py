def d_a_b(decimal):
    if decimal == 0:
        return "0"
    
    binario = " "
    while decimal > 0:
        residuo = decimal % 2 #nos quedamos con lo que sobra
        binario+= str(residuo) #almacenamos en caracteres y autoguardamos para mantener el dato
        decimal = decimal //2 #dividimos para seguir con el proceso

    return binario

input_number = int(input("Introduce el numero decimal: "))
resultado = d_a_b(input_number)
print("Su numero decimal en binario es: ", resultado)
    
