from bangundatar.bangundatar import BangunDatar
from bangundatar.persegi import Persegi
from bangundatar.segitiga import Segitiga

bangundatar = BangunDatar()

def garis():
  print("=====================")

run = True
while run:
  print("APLIKASI BANGUN DATAR")
  garis()
  print("1. PERSEGI")
  print("2. SEGITIGA")
  print("3. SELESAI")
  
  pilih = input("PILIH MENU [1/2/3]: ")

  if pilih == "1":
    print("PERSEGI")
    sisi = int(input('SISI: '))
    persegi = Persegi(sisi)
    print("Luas:",persegi.luas())
    print("Keliling:",persegi.keliling())
    garis()
  elif pilih == "2":
    print("SEGITIGA")
    alas = int(input('ALAS: '))
    tinggi = int(input('TINGGI: '))
    sisi = int(input('SISI MIRING: '))
    segitiga = Segitiga(alas, tinggi, sisi)
    print("Luas:",segitiga.luas())
    print("Keliling:",segitiga.keliling())
    garis()
  elif pilih == "3":
    run = False
  else:
    print("Tidak ada menu:",pilih)
