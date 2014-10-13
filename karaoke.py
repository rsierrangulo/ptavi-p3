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
        x = ''
        diccionario = linea[1]
        for atributos in diccionario.keys():
            valor = diccionario[atributos]
            if valor != '':
                if atributos == 'src' and valor[0] == 'h':
                    recurso = valor
                    nuevo_recurso = recurso.split('/')
                    valor = nuevo_recurso[-1]
                    os.system("wget -q " + recurso)
                x = x + atributos + '=' + '"' + valor + '"' + '\t'
        print x
