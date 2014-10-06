#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler (ContentHandler):

    def __init__(self):
        self.rootlayout = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.tagslist = []

    def startElement(self, tag, attrs):
        if tag == 'root-layout':
            self.rootlayout['width'] = attrs.get('width', "")
            self.rootlayout['height'] = attrs.get('height', "")
            self.rootlayout['background-color'] = attrs.get('height', "")
            self.tagslist.append([tag, self.rootlayout])
        elif tag == 'region':
            self.region['id'] = attrs.get('id', "")
            self.region['top'] = attrs.get('top', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('left', "")
            self.region['right'] = attrs.get('right', "")
            self.tagslist.append([tag, self.region])
        elif tag == 'img':
            self.img['src'] = attrs.get('src', "")
            self.img['region'] = attrs.get('region', "")
            self.img['begin'] = attrs.get('begin', "")
            self.img['dur'] = attrs.get('dur', "")
            self.tagslist.append([tag, self.img])
        elif tag == 'audio':
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['dur'] = attrs.get('dur', "")
            self.tagslist.append([tag, self.audio])
        elif tag == 'textstream':
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            self.tagslist.append([tag, self.textstream])

    def get_tags(self):
        return self.tagslist

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print cHandler.get_tags()
