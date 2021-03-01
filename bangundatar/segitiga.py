from .bangundatar import BangunDatar

class Segitiga(BangunDatar):
  def __init__(self, alas=0, tinggi=0, sisi=0):
    self.__alas   = alas
    self.__tinggi = tinggi
    self.__sisi   = sisi
    
  def luas(self):
    return (self.__alas * self.__tinggi) / 2

  def keliling(self):
    return self.__alas + self.__tinggi + self.__sisi