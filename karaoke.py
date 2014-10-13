#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler
import os

comandos = sys.argv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Usage: python karaoke.py file.smil')

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(comandos[1]))
    lista = cHandler.get_tags()
    for linea in lista:
        etiqueta = linea[0]
        print etiqueta + '\t',
        elementos = ''
        diccionario = linea[1]
        for atributos in diccionario.keys():
            if diccionario[atributos] != '':  
                if atributos == 'src' and diccionario[atributos][0] == 'h':
                    recurso = diccionario[atributos]
                    nuevo_recurso = recurso.split('/')
                    diccionario[atributos] = nuevo_recurso[-1]
                    os.system("wget -q " + recurso)
                elementos = elementos + atributos + '=' + '"' + diccionario[atributos] + '"' + '\t'
        print elementos
