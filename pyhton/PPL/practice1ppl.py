class siswa:
    def __init__(self, nama):
        self.nama = nama

perkenalan = siswa('Euroski')

print(f'siswa kami bernama {perkenalan.nama} Ganteng')


class guru:
    def __init__(self, nama):
        self._nama = nama

class guruotkp(guru):
    def __init__(self, nama, cantik):
        super().__init__(nama)
        self._cantik = cantik

    def pamer(self):
        print(f'Guru kami bernama {self._nama} yang {self._cantik}')
        
BuAnita = guruotkp('Bu anita', 'Cantik')
BuAnita.pamer()


class kepsek:
    def __init__(self, nama):
        self.__nama = nama

    def lilik(self):
        print(f'kepsek kami bernama {self.__nama}')

l = kepsek('lilik')
l.lilik()
