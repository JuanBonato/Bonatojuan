# -*- coding: utf-8 -*-

class Url():
    def __init__(self, center, recorrido, zoom):
        self.__url = "http://maps.google.com/maps/api/staticmap?"
        self.__center = "center="+center
        self.__zoom = "&zoom="+zoom
        self.__size = "&size=640x640"
        self.__markers = "&markers="+recorrido
        self.__path = "&path="+recorrido
        self.__imgformat = "&format=png"
        self.__maptype="&maptype=roadmap"        
        self.__sensor = "&sensor=false"
        self.__urlfinal = self.__url + self.__center + self.__zoom + self.__size + self.__markers + self.__path + self.__imgformat + self.__maptype + self.__sensor

    def set_Url(self,url):
        self.__urlfinal = url
        
    def set_Zoom(self,zoom):
        self.__zoom = "&zoom="+zoom
        self.__urlfinal = self.__url + self.__center + self.__zoom + self.__size + self.__markers + self.__path + self.__imgformat + self.__maptype + self.__sensor
        
    def get_Url(self):
        return self.__urlfinal