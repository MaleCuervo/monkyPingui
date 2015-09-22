# coding: utf-8

import pilasengine
pilas = pilasengine.iniciar()
texto_ayuda = """Tenes que ganar"""

class PantallaAyuda(pilas.escena.Base):
    #en esta pantalla se dan las instrucciones de juego
    #creación de la clase para la nueva pantalla a partir de la clase madre pilas.escena.Base
    
    def __init__(self):
        pilas.escena.Base.__init__(self)
        
    def iniciar(self):
        #instanciamos el fondo deseado y creamos métodos para mostrar los textos de ayuda
        pilas.fondos.Tarde()
        self.crear_texto_ayuda()
        self.boton.conectar(self.regresa_inicio)
        
    def crear_texto_ayuda(self):
        pilas.actores.Texto("Cómo se juega?:" , y = 100)
        pilas.actores.Texto(texto_ayuda)
        
    def regresa_inicio(self):
        #importa la escena de inicio y ejecuta el cambio de pantalla
        import menu
        pilas.cambiar_escena(escena_menu.EscenaMenu())
        
        
pilas.ejecutar()
