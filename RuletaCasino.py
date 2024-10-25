import random
colors = ["ROJO","NEGRO"]
numbers = range(0,37)

def color_user(datocolor):

    if datocolor not in colors:
        print("ERROR, elija un color valido!!")
    else:
        return datocolor
    
def number_user(datonumber):
    if datonumber not in numbers:
        print("ERROR, su numero no es valido!!")
    else:
        return datonumber
    
print("Porfavor introduzca su color de ruleta [Rojo o negro]: ")
datocolor = (input("").upper())

print("Porfavor introduzca su numero de ruleta [de 0 o 36]: ")
datonumber = (int(input("")))

number_win = random.choice(numbers)
color_win = random.choice(colors)

if color_user(datocolor) == color_win and number_user(datonumber) == number_win:
    print("Felicidades!! Has acertado!! tu numero fue",number_win," y tu color fue",color_win)

elif color_user(datocolor) == color_win:
    print("Ohhhh :(, Has acertado solo el color \n tu numero fue:",datonumber,"y el ganador fue: ",number_win)
    print("Sigue participando!!")
elif number_user(datonumber) == number_win:
    print("Ohhhh :(, Has acertado solo el numero \n tu color fue:",datocolor,"y el ganador fue: ",color_win)
    print("Sigue participando!!")
else: 
    print("No has acertado nada ;( suerte la proxima!!")