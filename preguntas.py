
# -*- coding: utf-8 -*-
import tkinter as tk
import numpy as np
import os
import PIL
from PIL import ImageTk
from PIL import Image

import personaje_clase
from personaje_clase import personaje

def salida_pregunta(p,window,jugador1,ventana_principal):
    jugador1.npregunta += 1
    print(p)
    window.destroy()
    if jugador1.npregunta == 1:
        paso_2(ventana_principal,jugador1)
    if jugador1.npregunta == 2:
        paso_3(ventana_principal,jugador1)
    if jugador1.npregunta == 3:
        paso_4(ventana_principal,jugador1)             
    if jugador1.npregunta == 4:
        paso_5(ventana_principal,jugador1)            
    if jugador1.npregunta == 5:
        paso_6(ventana_principal,jugador1) 
    if jugador1.npregunta == 6:
        paso_7(ventana_principal,jugador1) 
    if jugador1.npregunta == 7:
        print(jugador1.puntaje)
        
def accion():
    variable = tk.IntVar()
    v = variable.get()
    if v == 0:
        print("Desactivados")
    else:
        print(str(v)+" Activado")       
def paso_1(ventana_principal):
    cwd = os.getcwd() #Ruta actual del archivo
    jugador1 = personaje()
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Comidas!') 
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
    #Opcion 1
    Texto_1 = tk.Text(ventana,height=8, width=15,)
    Texto_1.grid(row=1, column=0)
    image_file = os.path.join(cwd,"imagenes/comidas/0_arroz.jpg")
    image = Image.open(image_file)
    
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto1 = ImageTk.PhotoImage(image)
    Texto_1.image = foto1                                #Sin esta instruccion la imagend entro de la funcion no se muestra. TK Tkinter issue
    Texto_1.image_create(tk.END, image=foto1) 


    #Opcion 2
    Texto_2 = tk.Text(ventana,height=8, width=15,)
    Texto_2.grid(row=1, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/comidas/1_curry.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS)
    foto2 = ImageTk.PhotoImage(image)
    Texto_2.image = foto2
    Texto_2.image_create(tk.END, image=foto2) 

    #Opcion 3
    Texto_3 = tk.Text(ventana,height=8, width=15,)
    Texto_3.grid(row=1, column=2)

    image = Image.open(os.path.join(cwd,"imagenes/comidas/2_mila.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto3 = ImageTk.PhotoImage(image)
    Texto_3.image = foto3
    Texto_3.image_create(tk.END, image=foto3) 

    #Opcion 4
    Texto_4 = tk.Text(ventana,height=8, width=15,)
    Texto_4.grid(row=3, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/comidas/3_asado.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto4 = ImageTk.PhotoImage(image)
    Texto_4.image = foto4
    Texto_4.image_create(tk.END, image=foto4) 

    #Opcion 5
    Texto_5 = tk.Text(ventana,height=8, width=15,)
    Texto_5.grid(row=3, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/comidas/4_couscous.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto5 = ImageTk.PhotoImage(image)
    Texto_5.image = foto5
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
    
    boton1.configure(command=lambda button=boton1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton2.configure(command=lambda button=boton2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton3.configure(command=lambda button=boton3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton4.configure(command=lambda button=boton4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton5.configure(command=lambda button=boton5: salida_pregunta(button,ventana,jugador1,ventana_principal))
    ventana.grid_columnconfigure(2, minsize=2)        

def paso_2(ventana_principal,jugador1):

    cwd = os.getcwd() #Ruta actual del archivo
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Pelis y series') 
    # getting screen's height in pixels
    height = ventana.winfo_screenheight()
      
    # getting screen's width in pixels
    width = ventana.winfo_screenwidth()
    ancho, alto = [np.int(width/3),np.int(height/2)]
    ventana.geometry(f'{ancho:0d}x{alto:0d}')

    #Titulo
    Texto_t = tk.Text(ventana,height=1,width=50)#,width = ancho)
    Texto_t.tag_configure("center", justify='center')
    Texto_t.grid(row=0,columnspan=4)
    textot = '¿Cuál de estas series o películas preferís?'
    Texto_t.insert('1.0', textot, 'color')
    #Opcion 1
    Texto_1 = tk.Text(ventana,height=8, width=15,)
    Texto_1.grid(row=1, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/pelis/0_naruto.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto1 = ImageTk.PhotoImage(image)
    Texto_1.image = foto1
    Texto_1.image_create(tk.END, image=foto1) 


    #Opcion 2
    Texto_2 = tk.Text(ventana,height=8, width=15,)
    Texto_2.grid(row=1, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/pelis/1_onepiece.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS)
    foto2 = ImageTk.PhotoImage(image)
    Texto_2.image = foto2
    Texto_2.image_create(tk.END, image=foto2) 

    #Opcion 3
    Texto_3 = tk.Text(ventana,height=8, width=15,)
    Texto_3.grid(row=1, column=2)

    image = Image.open(os.path.join(cwd,"imagenes/pelis/2_teen_titans.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto3 = ImageTk.PhotoImage(image)
    Texto_3.image = foto3
    Texto_3.image_create(tk.END, image=foto3) 

    #Opcion 4
    Texto_4 = tk.Text(ventana,height=8, width=15,)
    Texto_4.grid(row=3, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/pelis/3_gravity.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto4 = ImageTk.PhotoImage(image)
    Texto_4.image = foto4
    Texto_4.image_create(tk.END, image=foto4) 

    #Opcion 5
    Texto_5 = tk.Text(ventana,height=8, width=15,)
    Texto_5.grid(row=3, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/pelis/4_avengers.jpg"))
    image = image.resize((150, 120), Image.ANTIALIAS) 
    foto5 = ImageTk.PhotoImage(image)
    Texto_5.image = foto5
    Texto_5.image_create(tk.END, image=foto5)

    #entrada
    ancho_texto_px = 120
    boton1 = tk.Button(ventana, text='Obvio que Naruto',pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton1.grid(row=2, column=0)

    boton2 = tk.Button(ventana, text="Amo a One piece",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton2.grid(row=2, column=1)
    boton3 = tk.Button(ventana, text="Los jovenes titanes!",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton3.grid(row=2, column=2)
    boton4 = tk.Button(ventana, text="Gravity Falls",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton4.grid(row=4, column=0)
    boton5 = tk.Button(ventana, text="Avengers",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton5.grid(row=4, column=1)
    boton1.configure(command=lambda button=boton1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton2.configure(command=lambda button=boton2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton3.configure(command=lambda button=boton3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton4.configure(command=lambda button=boton4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton5.configure(command=lambda button=boton5: salida_pregunta(button,ventana,jugador1,ventana_principal))
    ventana.grid_columnconfigure(2, minsize=2)



def paso_3(ventana_principal,jugador1):
    cwd = os.getcwd() #Ruta actual del archivo
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Atención!') 
    # getting screen's height in pixels
    height = ventana.winfo_screenheight()
      
    # getting screen's width in pixels
    width = ventana.winfo_screenwidth()
    ancho, alto = [np.int(width/3),np.int(height)]
    ventana.geometry(f'{ancho:0d}x{alto:0d}')

    #Titulo
    Texto_t = tk.Text(ventana,height=10,width=50)#,width = ancho)
    Texto_t.tag_configure("center", justify='center')
    Texto_t.grid(row=0,columnspan=4)
    textot = '¿Alguien que no conoces te patea ¿que haces?'
    Texto_t.insert('1.0', textot, 'color')

    image = Image.open(os.path.join(cwd,"imagenes/patada.jpg"))
    image = image.resize((300, 400), Image.ANTIALIAS) 
    foto = ImageTk.PhotoImage(image)
    Texto_t.image = foto
    Texto_t.image_create(tk.END, image=foto)    
    
    
    #Opciones
    variable = tk.IntVar()
    texto1 = 'Lo pateo,si el no es bueno conmigo ¿porque yo si?'
    texto2 = 'Le digo que mire por donde va.'
    texto3 = 'Le digo que por favor se disculpe y que ya no haga eso.'
    texto4 = 'Le digo que le dire a la profesora.'
    texto5 = 'Primero me ubico en una distancia protegida como para que no me pueda patear, y luego le digo lo mismo que la tercera pregunta'        
    R1 = tk.Radiobutton(ventana, variable=variable, value=1, text=texto1, height=3,
                    width=60)
    R2 = tk.Radiobutton(ventana, variable=variable, value=2, text=texto2, height=3,
                    width=60)
    R3 = tk.Radiobutton(ventana, variable=variable, value=3, text=texto3, height=3,
                    width=60)
    R4 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto4, height=3,
                    width=60)
    R5 = tk.Radiobutton(ventana, variable=variable, value=5, text=texto5, height=4,
                    width=60,wraplength=300,justify='center')
    R1.configure(command=lambda button=R1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R2.configure(command=lambda button=R2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R3.configure(command=lambda button=R3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R4.configure(command=lambda button=R4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R5.configure(command=lambda button=R5: salida_pregunta(button,ventana,jugador1,ventana_principal))            
    R1.grid(row=1)
    R2.grid(row=2)
    R3.grid(row=3)
    R4.grid(row=4)
    R5.grid(row=5)
  

def paso_4(ventana_principal,jugador1):
    cwd = os.getcwd() #Ruta actual del archivo
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Secretos!') 
    # getting screen's height in pixels
    height = ventana.winfo_screenheight()
      
    # getting screen's width in pixels
    width = ventana.winfo_screenwidth()
    ancho, alto = [np.int(width/3),np.int(height)]
    ventana.geometry(f'{ancho:0d}x{alto:0d}')

    #Titulo
    Texto_t = tk.Text(ventana,height=10,width=50)#,width = ancho)
    Texto_t.tag_configure("center", justify='center')
    Texto_t.grid(row=0,columnspan=4)
    textot = '¿Que cosa mas prohibida has hecho?'
    Texto_t.insert('1.0', textot, 'color')

    image = Image.open(os.path.join(cwd,"imagenes/confidential.png"))
    image = image.resize((400, 200), Image.ANTIALIAS) 
    foto = ImageTk.PhotoImage(image)
    Texto_t.image = foto
    Texto_t.image_create(tk.END, image=foto)    
    
    
    #Opciones
    variable = tk.IntVar()
    texto1 = 'Beber una botella de leche directamente.'
    texto2 = 'Cruce una calle de la cual no tenia permiso cruzar.'
    texto3 = 'Le pegue a alguien.'
    texto4 = 'Me burle de alguien por su aspecto.'
    texto5 = 'Vi cosas para mayores de 18.'  
    texto6 = 'Me robe galletitas.'     
    texto7 = 'Rompi la casa de alguien mientras corria.'  
           
    R1 = tk.Radiobutton(ventana, variable=variable, value=1, text=texto1, height=3,
                    width=60)
    R2 = tk.Radiobutton(ventana, variable=variable, value=2, text=texto2, height=3,
                    width=60)
    R3 = tk.Radiobutton(ventana, variable=variable, value=3, text=texto3, height=3,
                    width=60)
    R4 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto4, height=3,
                    width=60)
    R5 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto5, height=3,
                    width=60)
    R6 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto6, height=3,
                    width=60)
    R7 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto7, height=3,
                    width=60)                                        
    R1.configure(command=lambda button=R1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R2.configure(command=lambda button=R2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R3.configure(command=lambda button=R3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R4.configure(command=lambda button=R4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R5.configure(command=lambda button=R5: salida_pregunta(button,ventana,jugador1,ventana_principal))            
    R6.configure(command=lambda button=R6: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R7.configure(command=lambda button=R7: salida_pregunta(button,ventana,jugador1,ventana_principal))                           
    R1.grid(row=1)
    R2.grid(row=2)
    R3.grid(row=3)
    R4.grid(row=4)
    R5.grid(row=5)
    R6.grid(row=6)
    R7.grid(row=7)







def paso_5(ventana_principal,jugador1):
    cwd = os.getcwd() #Ruta actual del archivo
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Fidelidad') 
    # getting screen's height in pixels
    height = ventana.winfo_screenheight()
      
    # getting screen's width in pixels
    width = ventana.winfo_screenwidth()
    ancho, alto = [np.int(width/3),np.int(height)]
    ventana.geometry(f'{ancho:0d}x{alto:0d}')

    #Titulo
    Texto_t = tk.Text(ventana,height=10,width=50)#,width = ancho)
    Texto_t.tag_configure("center", justify='center')
    Texto_t.grid(row=0,columnspan=4)
    textot = 'Alguien se burla de alguien que amas ¿que haces?'
    Texto_t.insert('1.0', textot, 'color')

    image = Image.open(os.path.join(cwd,"imagenes/bully.png"))
    image = image.resize((400, 200), Image.ANTIALIAS) 
    foto = ImageTk.PhotoImage(image)
    Texto_t.image = foto
    Texto_t.image_create(tk.END, image=foto)    
    
    
    #Opciones
    variable = tk.IntVar()
    texto1 = 'Protejo a la persona que amo humillando al agresor.'
    texto2 = 'Le digo a la persona que amo que nos vayamos.'
    texto3 = 'Dejo a la persona que amo sola, que se defienda sola.'
    texto4 = 'Empiezo a ponerme loco y rasguño al agresor.'  
    texto5 = 'Distraigo y burlo al agresor.'     
    texto6 = 'Lo golpeo hasta que sangre.'  
           
    R1 = tk.Radiobutton(ventana, variable=variable, value=1, text=texto1, height=3,
                    width=60)
    R2 = tk.Radiobutton(ventana, variable=variable, value=2, text=texto2, height=3,
                    width=60)
    R3 = tk.Radiobutton(ventana, variable=variable, value=3, text=texto3, height=3,
                    width=60)
    R4 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto4, height=3,
                    width=60)
    R5 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto5, height=3,
                    width=60)
    R6 = tk.Radiobutton(ventana, variable=variable, value=4, text=texto6, height=3,
                    width=60)

    R1.configure(command=lambda button=R1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R2.configure(command=lambda button=R2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R3.configure(command=lambda button=R3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R4.configure(command=lambda button=R4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R5.configure(command=lambda button=R5: salida_pregunta(button,ventana,jugador1,ventana_principal))            
    R6.configure(command=lambda button=R6: salida_pregunta(button,ventana,jugador1,ventana_principal))
    R1.grid(row=1)
    R2.grid(row=2)
    R3.grid(row=3)
    R4.grid(row=4)
    R5.grid(row=5)
    R6.grid(row=6)
    
    

def paso_6(ventana_principal,jugador1):

    cwd = os.getcwd() #Ruta actual del archivo
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Habilidades escolares!') 
    # getting screen's height in pixels
    height = ventana.winfo_screenheight()
      
    # getting screen's width in pixels
    width = ventana.winfo_screenwidth()
    ancho, alto = [np.int(width/3),np.int(height*0.6)]
    ventana.geometry(f'{ancho:0d}x{alto:0d}')

    #Titulo
    Texto_t = tk.Text(ventana,height=7,width=50)#,width = ancho)
    Texto_t.tag_configure("center", justify='center')
    Texto_t.grid(row=0,columnspan=4)
    textot = '¿En qué materia de la escuela sos más capaz?'
    Texto_t.insert('1.0', textot, 'color')
    image = Image.open(os.path.join(cwd,"imagenes/escuela_materia.png"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto = ImageTk.PhotoImage(image)
    Texto_t.image = foto
    Texto_t.image_create(tk.END, image=foto)
    #Opcion 1
    Texto_1 = tk.Text(ventana,height=8, width=15,)
    Texto_1.grid(row=1, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/plastica.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto1 = ImageTk.PhotoImage(image)
    Texto_1.image = foto1
    Texto_1.image_create(tk.END, image=foto1) 


    #Opcion 2
    Texto_2 = tk.Text(ventana,height=8, width=15,)
    Texto_2.grid(row=1, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/tecno.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS)
    foto2 = ImageTk.PhotoImage(image)
    Texto_2.image = foto2
    Texto_2.image_create(tk.END, image=foto2) 

    #Opcion 3
    Texto_3 = tk.Text(ventana,height=8, width=15,)
    Texto_3.grid(row=1, column=2)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/matematica.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto3 = ImageTk.PhotoImage(image)
    Texto_3.image = foto3
    Texto_3.image_create(tk.END, image=foto3) 

    #Opcion 4
    Texto_4 = tk.Text(ventana,height=8, width=15,)
    Texto_4.grid(row=1, column=3)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/lengua2.png"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto4 = ImageTk.PhotoImage(image)
    Texto_4.image = foto4
    Texto_4.image_create(tk.END, image=foto4) 

    #Opcion 5
    Texto_5 = tk.Text(ventana,height=8, width=15,)
    Texto_5.grid(row=3, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/edfisica.png"))
    image = image.resize((150, 120), Image.ANTIALIAS) 
    foto5 = ImageTk.PhotoImage(image)
    Texto_5.image = foto5
    Texto_5.image_create(tk.END, image=foto5)
    #Opcion 6
    Texto_6 = tk.Text(ventana,height=8, width=15,)
    Texto_6.grid(row=3, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/ciencias_nat.jpg"))
    image = image.resize((150, 120), Image.ANTIALIAS) 
    foto6 = ImageTk.PhotoImage(image)
    Texto_6.image = foto6
    Texto_6.image_create(tk.END, image=foto6)
    
    #Opcion 7
    Texto_7 = tk.Text(ventana,height=8, width=15,)
    Texto_7.grid(row=3, column=2)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/musica.png"))
    image = image.resize((150, 120), Image.ANTIALIAS) 
    foto7 = ImageTk.PhotoImage(image)
    Texto_7.image = foto7
    Texto_7.image_create(tk.END, image=foto7)
    #Opcion 8
    Texto_8 = tk.Text(ventana,height=8, width=15,)
    Texto_8.grid(row=3, column=3)

    image = Image.open(os.path.join(cwd,"imagenes/escuela/otra_cosa.jpg"))
    image = image.resize((150, 120), Image.ANTIALIAS) 
    foto8 = ImageTk.PhotoImage(image)
    Texto_8.image = foto8
    Texto_8.image_create(tk.END, image=foto8)    

    #entrada
    ancho_texto_px = 120
    boton1 = tk.Button(ventana, text='Plástica',pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton1.grid(row=2, column=0)

    boton2 = tk.Button(ventana, text="Tecnología",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton2.grid(row=2, column=1)
    boton3 = tk.Button(ventana, text="Matemática",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton3.grid(row=2, column=2)
    boton4 = tk.Button(ventana, text="Práctica de Lenguaje",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton4.grid(row=2, column=3)
    boton5 = tk.Button(ventana, text="Educación Física",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton5.grid(row=4, column=0)
    
    boton6 = tk.Button(ventana, text="Ciencias Naturales",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton6.grid(row=4, column=1)
    boton7 = tk.Button(ventana, text="Música",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton7.grid(row=4, column=2)
    boton8 = tk.Button(ventana, text="Otra Cosa",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton8.grid(row=4, column=3)            
    boton1.configure(command=lambda button=boton1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton2.configure(command=lambda button=boton2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton3.configure(command=lambda button=boton3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton4.configure(command=lambda button=boton4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton5.configure(command=lambda button=boton5: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton6.configure(command=lambda button=boton6: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton7.configure(command=lambda button=boton7: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton8.configure(command=lambda button=boton8: salida_pregunta(button,ventana,jugador1,ventana_principal))            
    ventana.grid_columnconfigure(2, minsize=2)
    
    
   
  

def paso_7(ventana_principal,jugador1):

    cwd = os.getcwd() #Ruta actual del archivo
    ventana = tk.Toplevel(ventana_principal)
    ventana.title('Podría pasar todo mi tiempo...') 
    # getting screen's height in pixels
    height = ventana.winfo_screenheight()
      
    # getting screen's width in pixels
    width = ventana.winfo_screenwidth()
    ancho, alto = [np.int(width/3),np.int(height*0.6)]
    ventana.geometry(f'{ancho:0d}x{alto:0d}')

    #Titulo
    Texto_t = tk.Text(ventana,height=7,width=50)#,width = ancho)
    Texto_t.tag_configure("center", justify='center')
    Texto_t.grid(row=0,columnspan=4)
    textot = '¿ Qué es lo que mas te apasiona?'
    Texto_t.insert('1.0', textot, 'color')
    image = Image.open(os.path.join(cwd,"imagenes/pasion.png"))
    image = image.resize((100, 150), Image.ANTIALIAS) 
    foto = ImageTk.PhotoImage(image)
    Texto_t.image = foto
    Texto_t.image_create(tk.END, image=foto)
    
    #Opcion 1
    Texto_1 = tk.Text(ventana,height=8, width=15,)
    Texto_1.grid(row=1, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/pasion/manga-manga-artist-artist-artists.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto1 = ImageTk.PhotoImage(image)
    Texto_1.image = foto1
    Texto_1.image_create(tk.END, image=foto1) 


    #Opcion 2
    Texto_2 = tk.Text(ventana,height=8, width=15,)
    Texto_2.grid(row=1, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/pasion/musica.jpeg"))
    image = image.resize((150, 150), Image.ANTIALIAS)
    foto2 = ImageTk.PhotoImage(image)
    Texto_2.image = foto2
    Texto_2.image_create(tk.END, image=foto2) 

    #Opcion 3
    Texto_3 = tk.Text(ventana,height=8, width=15,)
    Texto_3.grid(row=1, column=2)

    image = Image.open(os.path.join(cwd,"imagenes/pasion/running-couple.jpg"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto3 = ImageTk.PhotoImage(image)
    Texto_3.image = foto3
    Texto_3.image_create(tk.END, image=foto3) 

    #Opcion 4
    Texto_4 = tk.Text(ventana,height=8, width=15,)
    Texto_4.grid(row=3, column=0)

    image = Image.open(os.path.join(cwd,"imagenes/pasion/Lithe-Dancing-Woman-Silhouette.png"))
    image = image.resize((150, 150), Image.ANTIALIAS) 
    foto4 = ImageTk.PhotoImage(image)
    Texto_4.image = foto4
    Texto_4.image_create(tk.END, image=foto4) 

    #Opcion 5
    Texto_5 = tk.Text(ventana,height=8, width=15,)
    Texto_5.grid(row=3, column=1)

    image = Image.open(os.path.join(cwd,"imagenes/pasion/math.jpg"))
    image = image.resize((150, 120), Image.ANTIALIAS) 
    foto5 = ImageTk.PhotoImage(image)
    Texto_5.image = foto5
    Texto_5.image_create(tk.END, image=foto5)
  

    #entrada
    ancho_texto_px = 120
    boton1 = tk.Button(ventana, text='Dibujar',pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton1.grid(row=2, column=0)

    boton2 = tk.Button(ventana, text="Tocar un instrumento",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton2.grid(row=2, column=1)
    boton3 = tk.Button(ventana, text="Correr",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton3.grid(row=2, column=2)
    boton4 = tk.Button(ventana, text="Bailar o jugar algun que otro deporte",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton4.grid(row=4, column=0)
    boton5 = tk.Button(ventana, text="Matematicas",pady=5,padx=2,activebackground='#a8acfd',height=2,width=12,wraplength=ancho_texto_px,justify='center')
    boton5.grid(row=4, column=1)
             
    boton1.configure(command=lambda button=boton1: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton2.configure(command=lambda button=boton2: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton3.configure(command=lambda button=boton3: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton4.configure(command=lambda button=boton4: salida_pregunta(button,ventana,jugador1,ventana_principal))
    boton5.configure(command=lambda button=boton5: salida_pregunta(button,ventana,jugador1,ventana_principal))
           
    ventana.grid_columnconfigure(2, minsize=2)

