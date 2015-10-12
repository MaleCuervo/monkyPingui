# -*- coding: utf-8 -*-

import pilasengine
import pilasengine.colores


class Barra_tiempo(pilasengine.actores.Temporizador):
    #nueva barra de tiempo, con imagen y cambio de argumentos
    def iniciar(self):
        self.imagen = "data/152-clock.png"
        self.texto = self.pilas.actores.Texto("0")
        self.texto.color = pilasengine.colores.negro
        self.y = 160
        self.x = 260
        self.texto.y = 100
        self.texto.x = 250
        

class Nivel(pilasengine.escenas.Escena, pilasengine.actores.Mono,pilasengine.actores.Pingu,pilasengine.actores.Martian ):
    #escena del primer nivel. Se instancia la barra de tiempo y da inicio, 
    def iniciar(self):
        self.pilas.fondos.Selva()
        self.tiempo = Barra_tiempo(self.pilas)
        
        #Aparecen los personajes del primer nivel
        self.pilas.actores.Mono(x = 0 ,y = 0) 
        self.pilas.actores.Mono(x = -170)
        self.pilas.actores.Pingu(x = 170, y = -50)
        self.pilas.actores.Martian(x= 0,y = -170)
        
        #se asigna un mensaje al final
        self.tiempo.ajustar(30, self.hola_mundo)
        self.tiempo.comenzar()
          

    def hola_mundo(self):
        self.pilas.avisar("Fin del primer nivel")

