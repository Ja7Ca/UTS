#1
def fib(n):
    fib_num = [0,1]
    for i in range(2,n):
        fib_num.append(fib_num[i-1]+fib_num[i-2])
    return fib_num

#print(fib(6))

#Yang dihasilkan [0,1,1,2,3,5]
#Penjelasan : ketika fungsi fib dipanggil akan membuat variable list fib_num yang
#memiliki value 0, dan 1. Kemudian fungsi ini akan melakukan perulangan untuk
#menambahkan hasil penjumlahan angka terakhir dengan depannya. Perulangan dimulai
#dari 2 dan akan berhenti apabila banyak perulangan mencapai sebelum input
#paramater dari user
#------------------------------------------------------------
#2
class Buku():
    def __init__(self,jumlah,judul):
        self.jumlah = jumlah
        self.judul = judul

    def __str__(self):
        return "Buku berjudul : "+str(self.judul)+"berjumlah" + str(self.jumlah)

#buku1 = Buku(2,"Aku Anak Hebat")
#print(buku1)

#2a
##Class Buku diatas memiliki parameter jumlah, dan buku
##hasil dari parameter dimasukkan kemasing-masing variable self
##Kemudian terdapat method __str__ method ini digunakan ketikan mencetak objeck
##klas ini akan mencetak string dan juga variable judul, dan jumlah

#2b
##Kelas ini memiliki method __str__, maka akan mencetak yang didalam method ini
##berupa return "Buku berjudul: "+str(self.judul)+"berjumlah"+str(self.jumlah)
##Contoh : Buku berjudul : Aku Anak Hebatberjumlah 2

#2c
#Mengubah isi mehtode __str__
    def __str__(self):
        return "Buku Berjudul : "+str(self.judul)


#------------------------------------------------------------
#3
class Array():
    def __init__(self):
        array = []

    def buatArray(self, panjang):
        array = [None for i in range(panjang)]
        return array
    def gantiElement(self):
        for i in len(array):
            array[i] = "Jarot"
        return array
#Ketika class Array dipanggil, akan membuat array kosong, kemudian method buatArray akan membuat panjang array tergantung input dari user, kemudian method gantiElement akan mengubah element pada array menjadi string
#------------------------------------------------------------
#4
#4a            
class DNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

nim = 247
head = DNode(nim)
x = head
for i in range(1, 9):
    baru = DNode(nim+i)
    x.next = baru
    baru.prev = x
    x = baru

#class DNode sebagai menyimpan node, kemudia membuat 9 node dari nim 247-255

class Doubly(object):
    def __init__(self, head):
        self.head = head
    def cetakAll(self):
        x = self.head
        while x != None:
            print(x.data)
            x = x.next
#4b
    def hapus7(self):
        x = self.head
        posisi = 1
        while posisi != 6:
            x = x.next
            posisi += 1
        x.next = x.next.next
        x.next.next.prev = x
# methode ini menggunakan node ke-6 untuk melanjutkan node ke-8, dan node ke-8
#melakukan pengembalian node ke-6

#------------------------------------------------------------
# class no 4
class Doubly(object):
    def __init__(self, head):
        self.head = head
    def cetakAll(self):
        x = self.head
        while x != None:
            print(x.data)
            x = x.next
    def hapus7(self):
        x = self.head
        posisi = 1
        while posisi != 6:
            x = x.next
            posisi += 1
        x.next = x.next.next
        x.next.next.prev = x
#5
#Melakukan pengecekan setiap node, apabila pencarian berada di node tersebut maka
#akan mengembalikan nilai string, apabila tidak, maka akan melanjutkan ke node
#setelahnya

    def cari(self, data):
        posisi = 1
        x = self.head
        while x != None:
            if str(data) in str(x.data):
                return "Di-posisi "+str(posisi)
            x = x.next
            posisi += 1
        return "Tidak ditemukan"

#Kompleksitas fungsi cari Notasi Big O
#1 perulangan O(n) dan 5 Operasi O(5)
#O(n + 5), karena Big O tidak boleh menyertai konstanta
#O(n)
