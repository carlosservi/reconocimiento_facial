import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.reconocimiento_facial import reconocimiento
from src.registro import registrarse

#Función para registrarse
def registrarse_usuario():
    registrarse()

#Función para reconocimiento
def reconocimiento_funcion():
    reconocimiento()

#Función de la interfaz inicial con la lógica
def interfaz_inicial():

    ventana = tk.Tk()
    ventana.title("Aplicación de Reconocimiento Facial")
    ventana.resizable(0,0)

    # Obtener el ancho y la altura de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (600 // 2)
    y = (altura_pantalla // 2) - (500 // 2)

    # Configurar las coordenadas de la ventana4
    ventana.geometry(f"600x500+{x}+{y}")

    # Cargar la imagen
    imagen = Image.open("Imagenes/silueta.jpg")
    imagen = imagen.resize((400, 400), Image.ANTIALIAS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear el widget Label para mostrar la imagen
    label_imagen = ttk.Label(ventana, image=imagen_tk)
    label_imagen.pack()

    # Estilo para los botones
    estilo_boton = ttk.Style()
    estilo_boton.configure("TButton", font=("Arial", 12))

    # Marco para los botones
    marco_botones = ttk.Frame(ventana)
    marco_botones.pack(side="bottom", padx=20, pady=30)

    # Botón de registrarse
    boton_registrarse = ttk.Button(marco_botones, text="Registrarse", command=registrarse_usuario, style="TButton")
    boton_registrarse.pack(side="left", padx=20)

    # Botón de loguearse
    boton_loguearse = ttk.Button(marco_botones, text="Reconocimiento", command=lambda: reconocimiento_funcion(), style="TButton")
    boton_loguearse.pack(side="left", padx=20)

    # Ejecutar la interfaz gráfica
    ventana.mainloop()
    return 
    
