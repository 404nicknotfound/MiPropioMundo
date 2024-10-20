import sys

for i in range(100):
    print(i)
    if (i%3)==0:
        print(i,"fizz")

    if (i%5) ==0:
            print(i,"buzz")
            
    if(i%5) ==0 and (i%3)==0:
                print(i, "fizz buzz")
    else:
           print()
