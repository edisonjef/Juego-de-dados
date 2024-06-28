import os
import random

billetera = 1000000
minimo_de_mesa = 10

def jugar():
    os.system('cls')
    global billetera
    while True:
        ingreso = input("Ingrese 'S' para salir o enter para jugar: ").lower()
        if ingreso == 's':
            print("Saliendo del juego...Gracias por jugar con Casino Vaiajo")
            break
        else:
            print(f"Su saldo es: ${billetera}".center(110))
            numero =""
            while not (numero.isdigit() and 2<= int(numero) <=12):
                numero = input("ingrese el numero que saldra entre 2 Y 12:\n")
            numero = int(numero)
            
            apuesta= ""
            while not (apuesta.replace(".","").isdigit() and minimo_de_mesa <= float(apuesta) <= billetera):
                apuesta = input(f"Ingrese su apuesta entre {minimo_de_mesa} y {billetera}:\n")    
            apuesta = int(apuesta)
            
            dado_1 = random.randint(1,6)
            dado_2 = random.randint(1,6)
            
            print(f"Salio:\n dado 1: {dado_1} - Dado 2: {dado_2} \nsuma en Total: {dado_1+dado_2}")
       
            
            if numero == (dado_1 + dado_2):
                saldo= apuesta*10
                print(f"Ganaste: ${saldo}")
            
            else:
                saldo = -apuesta 
                print(f"Lo siento perdiste, Suerte enla proxima.\nPerdiste: ${apuesta}")
                    
        billetera += saldo
        
   

jugar()