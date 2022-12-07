#buat 3 objek orang, pelajar, pekerja
#Orang = kelas induk
#pelajar, pekerja = kelas turunan

class orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("Halo nama saya", self.nama,"dari",self.asal)

class pelajar(orang):
    def __init__(self, nama, asal, sekolah):
         orang.__init__(self, nama, asal)
         self.sekolah = sekolah

class pekerja(orang):
    def __init__(self, nama, asal, kantor):
         super().__init__(nama, asal)
         self.kantor = kantor

andi = orang('Andi','Jakarta\n')
andi.perkenalan()

tito = pelajar('Tito','Subang','SMK JP1')
tito.perkenalan()
print(f'saya sekolah di {tito.sekolah}\n')

cahyo = pekerja('Cahyo','Bandung','SMK JP1')
cahyo.perkenalan()
print(f'saya bekerja di{cahyo.kantor}')