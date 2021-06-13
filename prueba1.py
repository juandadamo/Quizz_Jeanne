import tkinter as tk
import numpy as np
import os
import PIL
import PIL
from PIL import ImageTk
from PIL import Image




cwd = os.getcwd() #Ruta actual del archivo
ventana = tk.Tk()
ventana.title('Test de Personaje') 

# getting screen's height in pixels
height = ventana.winfo_screenheight()
  
# getting screen's width in pixels
width = ventana.winfo_screenwidth()
ancho, alto = [np.int(width/3),np.int(height/2)]
ventana.geometry(f'{ancho:0d}x{alto:0d}')

#Titulo
Texto_t = tk.Text(ventana,height=1,width=30)#,width = ancho)
Texto_t.tag_configure("center", justify='center')
Texto_t.grid(row=0,columnspan=4)
textot = 'Cuál es tu comida favorita?'
Texto_t.insert('1.0', textot, 'color')



#def salida_pregunta

def salida_pregunta(p,window):
    print(p)
    window.destroy()
    return p
    



#Opcion 1
Texto_1 = tk.Text(ventana,height=8, width=15,)
Texto_1.grid(row=1, column=0)

image = Image.open(os.path.join(cwd,"imagenes/comidas/0_arroz.jpg"))
image = image.resize((150, 150), Image.ANTIALIAS) 
foto1 = ImageTk.PhotoImage(image)

Texto_1.image_create(tk.END, image=foto1) 


#Opcion 2
Texto_2 = tk.Text(ventana,height=8, width=15,)
Texto_2.grid(row=1, column=1)

image = Image.open(os.path.join(cwd,"imagenes/comidas/1_curry.jpg"))
image = image.resize((150, 150), Image.ANTIALIAS)
foto2 = ImageTk.PhotoImage(image)
Texto_2.image_create(tk.END, image=foto2) 

#Opcion 3
Texto_3 = tk.Text(ventana,height=8, width=15,)
Texto_3.grid(row=1, column=2)

image = Image.open(os.path.join(cwd,"imagenes/comidas/2_mila.jpg"))
image = image.resize((150, 150), Image.ANTIALIAS) 
foto3 = ImageTk.PhotoImage(image)
Texto_3.image_create(tk.END, image=foto3) 

#Opcion 4
Texto_4 = tk.Text(ventana,height=8, width=15,)
Texto_4.grid(row=3, column=0)

image = Image.open(os.path.join(cwd,"imagenes/comidas/3_asado.jpg"))
image = image.resize((150, 150), Image.ANTIALIAS) 
foto4 = ImageTk.PhotoImage(image)
Texto_4.image_create(tk.END, image=foto4) 

#Opcion 5
Texto_5 = tk.Text(ventana,height=8, width=15,)
Texto_5.grid(row=3, column=1)

image = Image.open(os.path.join(cwd,"imagenes/comidas/4_couscous.jpg"))
image = image.resize((150, 150), Image.ANTIALIAS) 
foto5 = ImageTk.PhotoImage(image)
Texto_5.image_create(tk.END, image=foto5)



#entrada
ancho_texto_px = 120
boton1 = tk.Button(ventana, text='Arroz Chino',pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
boton1.grid(row=2, column=0)

boton2 = tk.Button(ventana, text="Curry",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
boton2.grid(row=2, column=1)
boton3 = tk.Button(ventana, text="Milanesa con papas fritas",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
boton3.grid(row=2, column=2)
boton4 = tk.Button(ventana, text="Asado",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
boton4.grid(row=4, column=0)
boton5 = tk.Button(ventana, text="Couscous",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
boton5.grid(row=4, column=1)



boton5.configure(command=lambda button=boton5: salida_pregunta(button,ventana))






ventana.grid_columnconfigure(2, minsize=2)

ventana.mainloop()
