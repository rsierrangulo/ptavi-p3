#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import smallsmilhandler
import os 

comandos = sys.argv

if __name__ == "__main__":
    try:
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
                elementos = elementos + atributos + '=' + '"' + linea[1][atributos] + '"' + '\t'
            print elementos
    except:
        print 'Usage: python karaoke.py file.smil'