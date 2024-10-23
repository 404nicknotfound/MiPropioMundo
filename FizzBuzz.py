

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz\n ")
    elif i % 3 == 0:
        print("Fizz\n")
    elif i % 5 == 0:
        print("Buzz\n")
    else:
        print(i,"\n")

# ya que se esta utilizado los "elif", es necesario colocar en prioridad el mas complejo, 
# debido a que si no se utiliza pasara a los mas sencillos