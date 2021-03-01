from .bangundatar import BangunDatar

class Persegi(BangunDatar):
  def __init__(self, sisi=0):
    self.__sisi = sisi

  def luas(self):
    return self.__sisi * self.__sisi

  def keliling(self):
    return 4 * self.__sisi