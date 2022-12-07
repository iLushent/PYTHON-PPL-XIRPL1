#latihan atribut
#class siswa
class siswa:
    nama = None
    mantan = None

    def perkenalkan(self):
        print("Perrkenalkan saya {self.nama} dan nama mantan saya adalah {self.mantan}")
dhea = siswa()
dhea.nama = "Dhea Aisya Andini"
dhea.mantan = "Firgi"
dhea.perkenalan()