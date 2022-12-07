#jenis enkapsulasi  : public, protected, private

#membuat public class 

class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;

#instanstasi
segitiga_besar= segitiga(100, 80)

#
print('ini adalah publi class')
print(f'Alas : {segitiga_besar.alas}')
print(f'Tinggi : {segitiga_besar.tinggi}')
print(f'Luas : {segitiga_besar.luas}\n')

#membuat proctected class

class mobil: #class induk
    def __init__(self,merk):
        self._merk = merk #proctected class declaration

class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk) #panggil merk dibagian sini
        self._total_gear = total_gear

    def pamer(self):
        #hak akses _merk dari subclass
        print(f'ini adalah mobil {self._merk} dengan total gearnya {self._total_gear}\n')

#instansiansi
ferrari = mobilefwan('Ferrrari', 8)
ferrari.pamer()

#membuat private class
class motor:
    def __init__(self, merk):
        self.__merk = merk #private class declaration


    def tampilkan_merk(self):
        print(f'merk motornya : {self.__merk}')
        #panggil private disini


#intansiasi
print('ini adalah private class')
moge = motor('Harley')
moge.tampilkan_merk()