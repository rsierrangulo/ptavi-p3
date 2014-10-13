#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler
import os


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self):
        comandos = sys.argv
        fichero = comandos[1]
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.lista = cHandler.get_tags()

    def __str__(self):
        lista_str = ''
        for linea in self.lista:
            etiquetas = linea[0] + '\t'
            elementos = ''
            diccionario = linea[1]
            for atributos in diccionario.keys():
                valor = diccionario[atributos]
                if valor != '':
                    elementos = elementos + atributos
                    elementos += '=' + '"' + valor + '"' + '\t'
            lista_str += etiquetas + elementos + "\n"
        return lista_str

    def do_local(self):
        for linea in self.lista:
            etiquetas = linea[0] + '\t'
            elementos = ''
            diccionario = linea[1]
            for atributos in diccionario.keys():
                valor = diccionario[atributos]
                if valor != '':
                    nuevo_recurso = valor.split('/')
                    if nuevo_recurso[0] == 'http:':
                        os.system("wget -q " + valor)
                        diccionario[atributos] = nuevo_recurso[-1]

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit('Usage: python karaoke.py file.smil')

    karaoke = KaraokeLocal()
    print karaoke.__str__()
    karaoke.do_local()
    print karaoke.__str__()
