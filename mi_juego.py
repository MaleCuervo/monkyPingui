#! /usr/bin/env python
# coding: utf-8

import pilasengine

pilas = pilasengine.iniciar()

#import de modulos
import escenaInicio
import nivel1

caca = escenaInicio.PantallaBienvenida
pilas.escenas.vincular(caca)
pilas.escenas.caca("MonkyPingui\n Bienvenido")

pilas.ejecutar()
