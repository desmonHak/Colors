#! /usr/bin/python3
# -*- coding: utf-8 -*-

__description__ = 'este modulo se usa para imprimir colores'
__license__ = 'Apache 2.0'
__title__ = 'Color'
cryptography_version = '1.0.0'
__copyright__ = 'Desmon'


class Color:

    class Colors:

        def __init__(self):

            self.Red = ';31m'
            self.Yellow = ';33m'
            self.Green = ';32m'
            self.LightBlue = ';36m'
            self.DarkBlue = ';34m'
            self.Putple = ';35m'
            self.Black = ';30m'
            self.White = ';37m'

    class Shades:

        def __init__(self):

            self.Light = '\033[1'
            self.Dark = '\033[2'
            self.Italics = '\033[3'
            self.Underlined = '\033[4'
            self.Flicker = '\033[5'
            self.UnderlineMarking = '\033[6'
            self.hidden = '\033[8'
            self.strikethrough = '\033[9'


def PrintColor(text, shades='\033[1', colors=';37m'):

    print(str(shades) + str(colors) + str(text))


Colores = Color()
shades = Colores.Shades()
tipo = Colores.Colors()
PrintColor('hola', shades.Italics, tipo.Red)
