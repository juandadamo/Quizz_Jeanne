# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np
import os
import PIL
from PIL import ImageTk
from PIL import Image

import personaje_clase
from personaje_clase import personaje


def salida_pregunta(p,window):
    print(p)
    window.destroy()
    return p
def newWindow():
    pregunta = tk.Toplevel(ventana_principal)
    labelExample = tk.Label(pregunta, text = "New Window")
    buttonExample = tk.Button(pregunta, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()
    buttonExample.configure(command=lambda button=buttonExample: salida_pregunta(button,pregunta))

ventana_principal = tk.Tk()
ventana_principal.title('Test de Personaje')

#Opcion 1
Texto_1 = tk.Text(ventana_principal,height=12, width=55,)
data_win = Texto_1.winfo_screenmmwidth() 
ancho_win =  np.int(data_win / 1)
Texto_1.grid(row=0, column=0)
image = Image.open("portada.png")
image = image.resize((ancho_win, np.int(150*ancho_win/300)), Image.ANTIALIAS) 
foto1 = ImageTk.PhotoImage(image)
Texto_1.image_create(tk.END, image=foto1) 

boton1 = tk.Button(ventana_principal, text='Comenzar',pady=5,padx=2,activebackground='#a8acfd',height=4,width=45,wraplength=ancho_win,justify='center',command = newWindow) 
boton1.grid(row=1, column=0)



ventana_principal.mainloop()




