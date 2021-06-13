# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np
import os
import PIL
from PIL import ImageTk
from PIL import Image

import personaje_clase
from personaje_clase import personaje
from preguntas import salida_pregunta,paso_1

cwd = os.getcwd() #Ruta actual del archivo

def paso_1p():
    paso_1(ventana_principal)


ventana_principal = tk.Tk()
ventana_principal.title('Test de Personaje')

#Start Menu
Texto_1 = tk.Text(ventana_principal,height=12, width=55,)
data_win = Texto_1.winfo_screenmmwidth() 
ancho_win =  np.int(data_win / 1)
Texto_1.grid(row=0, column=0)
image = Image.open("portada.png")
image = image.resize((ancho_win, np.int(150*ancho_win/300)), Image.ANTIALIAS) 
foto1 = ImageTk.PhotoImage(image)
Texto_1.image_create(tk.END, image=foto1) 

boton1 = tk.Button(ventana_principal, text='Comenzar',pady=5,padx=2,activebackground='#a8acfd',
height=4,width=45,wraplength=ancho_win,justify='center',command = paso_1p )
boton1.grid(row=1, column=0)



ventana_principal.mainloop()




