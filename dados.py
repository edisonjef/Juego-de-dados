import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random


billetera = 1000000
minimo_de_mesa = 10
respuesta="Buena suerte"

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
        
   

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Dados - Casino Vaiajo")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.iconbitmap("dados.ico")

# Fondo
bg_image = Image.open("fondo.jpg") # con la biblioteca PIL obre la imagen
bg_image = bg_image.resize((500, 600), Image.LANCZOS)#redimenciona la imagen
bg_photo = ImageTk.PhotoImage(bg_image)#convierte la imagen en compatible con TK

bg_label = tk.Label(ventana, image=bg_photo)# crea un label en la ventana y le pone la imagen
bg_label.place(relwidth=1, relheight=1)# hace que la imagen ocupe todo el  ancho u alto de la ventana

# Título
label_titulo = tk.Label(ventana, text="A jugar", bg="black", fg="red", font=("carrier", 22))
label_titulo.place(x=200, y=10, width=100, height=50)

# Saldo
saldo_label = tk.Label(ventana, text=f" Tu Saldo Es: ${billetera}", bg='#ffffff', font=('Helvetica', 12, 'bold'))
saldo_label.place(x=145, y=70, width=200, height=30)  # Coloca debajo de label_titulo

# Entrada para el número
numero_label = tk.Label(ventana, text="Ingrese el número que saldrá entre 2 y 12:", bg='#ffffff', font=('Helvetica', 12))
numero_label.place(x=145, y=120,width=300, height=30)
numero_entry = tk.Entry(ventana, bg='white', highlightthickness=0)
numero_entry.place(x=230, y=150,width=100, height=30)

# Entrada para la apuesta
apuesta_label = tk.Label(ventana, text=f"Ingrese su apuesta entre ${minimo_de_mesa} y {billetera}:", bg='#ffffff', font=('Helvetica', 12))
apuesta_label.place(x=145, y=180,width=300, height=30)
apuesta_entry = tk.Entry(ventana, bg='white', highlightthickness=0)
apuesta_entry.place(x=230, y=210,width=100, height=30)

# Botón para jugar
jugar_button = ttk.Button(ventana, text="Jugar", style='RoundedButton.TButton', command=jugar)
jugar_button.place(x=230, y=330,width=100, height=30)


# Botón para salir
salir_button = ttk.Button(ventana, text="Salir", style='RoundedButton.TButton', command=lambda: ventana.destroy())
salir_button.place(x=230, y=360,width=100, height=30)

#respuestas
# Caja de texto para mostrar resultados con fondo blanco y borde invisible
resultado_text = tk.Text(ventana, height=10, bg='blue', font=('Helvetica', 12), bd=0)
resultado_text.place(x=120, y=400,width=300, height=100)
resultado_text.configure(state='disabled')#evita que el usuario pueda escribir en el
resultado_text.place_forget()  # Oculta inicialmente



# Ejecutar el bucle principal de tkinter
ventana.mainloop()



