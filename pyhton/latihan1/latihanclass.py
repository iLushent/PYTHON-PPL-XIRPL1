from re import X


class cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def tambah(self):
        return self.a + self.b
     
    def tambah(self):
        return self.a - self.b

a= int(input('Masukan angka pertama : '))
b= int(input)('Masuakn angka kedua : ')

object = cal(a,b)
while True:
    def menu():
        X = ("1. Pertambahan \n2. kurang")
        print(X)

    menu()
    pilihan = int(input)('silahkan pilih : ')
    if pilihan ==1:
        print('Hasilnya : ', object.tambah())
    elif pilihan == 2:
        print('hasilnya : ', object.kurang()) 
    break