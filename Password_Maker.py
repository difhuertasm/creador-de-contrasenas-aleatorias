from tkinter import Tk, Label, Entry, Button, Menu, messagebox, Spinbox
from tkinter import *
import tkinter as tk
import random

'''_______________________Ventana de inicio___________________________'''

def cerrar_ventana_inicial():
    inicio.destroy()

# Ventana de inicio
inicio = tk.Tk()
inicio.overrideredirect(True)# Elimina la barra de título.

# Obtiene el tamaño de la pantalla
ancho_pantalla = inicio.winfo_screenwidth()
alto_pantalla = inicio.winfo_screenheight()
#Asigna tamaño de ventana creada
ancho_ventana = 385
alto_ventana = 380
#Ajusta posición de la ventana en el centro
x_pos = (ancho_pantalla // 2) - (ancho_ventana // 2)
y_pos = (alto_pantalla // 2) - (alto_ventana // 2)
#Centra la ventana
inicio.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")
#Ajusta el tamaño de la ventana
inicio.minsize(width = ancho_ventana , height = alto_ventana)
imagen = PhotoImage(file="PW_M.png")
etiqueta_imagen = Label(inicio, image = imagen).place(x = 0, y =0)
# Configura el tiempo de vida de la ventana 4000 milisegundos = 4s.
inicio.after(4000, cerrar_ventana_inicial)

# Ejecuta la ventana principal
inicio.mainloop()

'''_______________________Algoritmo___________________________'''

estado_valido = False  # Variable de estado global

def info(): #Mensaje en pestaña Info
    messagebox.showinfo("Password Maker 2.0", "Creador de contraseñas seguras versión 1.0. Creado por el ing. D. Fernando Huertas M.")

def generar_contraseña():

    global contraseña, estado_valido #Para uso en otras funciones

    letras = "ABCDFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
    digitos = "0123456789"
    especiales = "!@#$%^&*_+-<>?"

    parte0 = random.choice(especiales) #Escoge alfanuméricos aleatorios 
    parte1 = txt5.get().capitalize() #Pone mayuscula a la palabra ingresada

    lista_digitos = []

    if int(txt0.get()) > (len(txt5.get()) + 2): # Longitud de la clave debe ser mayor que la palabra mas dos (alfanuméricos).
        for i in range(int(txt0.get()) - (len(txt5.get()) + 2)):
            lista_digitos.append(random.choice(digitos))
        parte2 = ''.join(lista_digitos)

        contraseña = parte0 + parte1 + parte2 + parte0
        txt2.delete(0, tk.END)
        txt2.insert(0, contraseña)
        estado_valido = True # Cambia estado y continua el proceso en la siguiente función.
    else:
        txt2.delete(0, tk.END)
        txt2.insert(0, "Contraseña no generada.\n")
        estado_valido = False # No cambia estado si no genera clave.

def guardado(contraseña):
    global txt3, txt4, estado_valido 

    # Ocultar mensajes anteriores
    txt3.place_forget()
    txt4.place_forget()

    if estado_valido:
        with open('contraseña.txt', 'w') as file:
            file.write(contraseña)
        txt3.place(x=70, y=242) #Imprimir mensaje en la parte inferior de la interfaz.
        txt4.place(x=60, y=260)
    else:
        with open('contraseña.txt', 'w') as file:
            file.write("NULL")
        messagebox.showinfo("No hay ninguna contraseña por guardar", "Intente de nuevo. Ingrese una longitud de contraseña mayor a la palabra ingresada.")

'''________________Creación del marco principal_________________'''

ventana = Tk()
ventana.title("Password Maker 1.0")
ventana.minsize(width=435, height=340)
ventana.config(padx=35, pady=35, bg='#13171c')

# Barra superior
barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

ayuda_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Ayuda', menu=ayuda_menu)
ayuda_menu.add_command(label='Acerca de...', command=info)

guardar_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Guardar', menu=guardar_menu)
guardar_menu.add_command(label='Contraseña generada', command=lambda: guardado(txt2.get()))

'''________________Creación de componentes________________________'''
enunciado1 = Label(text="Contraseñas seguras mediante caracteres alfanuméricos.", font=("Arial", 10), bg='#13171c', fg="#DBEBF9")
enunciado1.place(x=10, y=0)

enunciado2 = Label(text=" Tipo: caracter-palabra-número-caracter. Ejemplo:'$Xyz001$'' ", font=("Arial", 10), bg='#13171c', fg="#DBEBF9")
enunciado2.place(x=0, y=18)

etiqueta1 = Label(text="Longitud de contraseña:", font=("Arial", 10), bg='#13171c', fg="#DBEBF9")
etiqueta1.place(x=30, y=55)

etiqueta2 = Label(text="Palabra deseada en contraseña:", font=("Arial", 10), bg='#13171c', fg="#DBEBF9")
etiqueta2.place(x=0, y=100)

txt0 = Spinbox(ventana, from_=0, to=20, bg='#1b2126', fg='#DBEBF9')
txt0.place(x=180, y=55)

txt1 = Label(ventana, text='Su contraseña es: ', font=("Arial", 10), bg='#13171c', fg="#DBEBF9")
txt1.place(x=0, y=200)

txt2 = Entry(ventana, bg='#1b2126', fg='#DBEBF9', width=40)
txt2.place(x=115, y=200)

txt3 = Label(ventana, text='Contraseña guardada exitosamente.', font=("Arial", 10), bg='#13171c', fg="#DBEBF9")
txt4 = Label(ventana, text='¡Guárdala bien para recordarla después!', font=("Arial", 10), bg='#13171c', fg="#DBEBF9")

txt5 = Entry(ventana, bg='#1b2126', fg='#DBEBF9')
txt5.place(x=224, y=100)

boton = Button(ventana, text='Crear contraseña', font=("Arial", 10), bg='#275fac', fg='#DBEBF9', command=generar_contraseña)
boton.place(x=122, y=145, width=120, height=30)

ventana.mainloop()
