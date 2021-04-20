#1
def LuasPersegi():
    print("Program menghitung luas Persegi")
    sisi = int(input("Masukkan sisi = >? "))
    luas = sisi**2
    return "Luas persegi = sisi x sisi. Maka Luasnya = "+str(luas)+" satuan luas"
def LuasLingkaran():
    from math import pi
    print("Program menghitung luas Lingakaran")
    r = int(input("Masukkan jari-jari = >? "))
    luas = (pi*r*r)
    return "Luas Lingkaran = phi x r x r. Maka Luasnya = "+'{:.2f}'.format(luas)+" satuan luas"
def LuasSegitigaSamaSisi():
    print("Program menghitung luas Segitiga Sama Sisi")
    sisi = int(input("Masukkan sisi = >? "))
    luas = (sisi**2)/2
    return "Luas Segitiga = 1/2 x sisi x sisi. Maka Luasnya = "+str(luas)+" satuan luas"
def LuasBelahKetupat():    
    print("Program menghitung luas Belah Ketupat")
    d1 = int(input("Masukkan d1 = >? "))
    d2 = int(input("Masukkan d2 = >? "))
    luas = (d1*d2)/2
    return "Luas Belah Ketupat = 1/2 x d1 x d2. Maka Luasnya = "+str(luas)+" satuan luas"

##print(LuasPersegi())
##print("----------------------")
##print(LuasLingkaran())
##print("----------------------")
##print(LuasSegitigaSamaSisi())
##print("----------------------")
##print(LuasBelahKetupat())
##print("----------------------")

#2
#2a
matrik1 = [2,3]
matrik2 = [[3,4,5],[2,3,4]]
def kalikanMatrik(matrik1, matrik2):
    hasil = []
    jumlah = 0
    for indek in range(len(matrik2[0])):
        for i in range(len(matrik1)):
            jumlah += matrik1[i]*matrik2[i][indek]
        hasil.append(jumlah)
        jumlah = 0
    return hasil
##print("2a")
##print(matrik1, "1x2")
##print(matrik2, "2x3")
##print("Kalikan")
##print(kalikanMatrik(matrik1, matrik2), "1x3")
##print("----------------------")
#2b
def buatIdentitas7():
    matrik = [[1 if y==x else 0 for y in range(7)] for x in range(7)]
    return matrik
##print("2b")
##print("Buat Matrik identitas 7x7")
##print(buatIdentitas7())

#3
class Orang():
    def __init__(self, nama, umur, kulit):
        self.nama = nama
        self.umur = umur
        self.kulit = kulit
    def __str__(self):
        return str(self.nama)+" "+str(self.umur)+" "+str(self.kulit)

data1 = Orang("Jarot",20,"Sawo Matang")
data2 = Orang("Budi",22,"Kuning Langsat")
data3 = Orang("Tito",21,"Putih")
data4 = Orang("Riski",18,"Sawo Matang")
data5 = Orang("Akbar",17,"Kuning Langsat")
data6 = Orang("Doni",23,"Putih")
data7 = Orang("Dapa",16,"Kuning Langsat")
data8 = Orang("Adit",24,"Sawo Matang")
data9 = Orang("Agil",15,"Kuning Langsat")
data10 = Orang("Guntur",16,"Putih")

data = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]

##for i in data:
##    print(i)

#4
def cetakKulit(data, warna):
    for i in data:
        if i.kulit == warna:
            print(i.nama, "warna", i.kulit)
    return True

#cetakKulit(data, "Sawo Matang")

#5
def urutkanUmur(data):
    for tujuan in range(len(data)-1,0,-1):
        maks = 0
        for x in range(1,tujuan+1):
            maks_sem = data[maks].umur
            if maks_sem < data[x].umur:
                maks = x
            data[maks],data[tujuan] = data[tujuan],data[maks]
    return data

##for i in data:
##    print(i.umur, i.nama)
##print("--------Sebelum----------")
##urutkanUmur(data)
##print("--------Sesudah----------")
##for i in data:
##    print(i.umur, i.nama)
