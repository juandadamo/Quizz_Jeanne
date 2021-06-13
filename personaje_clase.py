# -*- coding: utf-8 -*-
import numpy as np



class personaje:    
    def __init__(self):
        self.npregunta = 0
        self.puntaje = 0
        self.pregunta_actual = 0
        self.nombre = 'Nadie'
            
    def punto_pregunta(self,resultado):
        valor_actual = resultado*10 + np.int(10**0.5*np.random.randn())
        self.pregunta_actual = valor_actual
        self.puntaje += self.puntaje + self.pregunta_actual
            
    def descubre(self):
        if self.puntaje <100:
            self.nombre = "Hinata Hyuga"
        elif self.puntaje<200:
            self.nombre = "Sasuke Uchiha"

    
        
