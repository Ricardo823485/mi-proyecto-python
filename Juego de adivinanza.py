import random 

MINIMO = 1
MAXIMO = 5

numero_azar = random.randint(MINIMO, MAXIMO)

while True:
    intento_usuario = int(input("Introdice un numero: "))
    if numero_azar != intento_usuario:
        print("Has fallado")
    else:
        print("Has acertado!")
        break
    
    
import random

MINIMO = 1
MAXIMO = 5

numero_azar = random.randint(MINIMO, MAXIMO)

while True: 
    intento_usuario: int(input("Introduce un numero: ")) # type: ignore
    if intento_usuario > numero_azar:
        print("Te has pasado del numero que habia pensado " + str(intento_usuario))
    elif intento_usuario < numero_azar:
        print("Te has bajado mucho del 1numero que yo habia pensado " + str (intento_usuario))
    else:
        print("Has acertado acepto mi derrota!")
        break
        
        

       
