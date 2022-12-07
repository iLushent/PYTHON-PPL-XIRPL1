class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print(self.nama, "beragama", self.agama )

class islam(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat

class kristen(Agama):
    def __init__(self, nama, agama, greja):
        Agama.__init__(self, nama, agama)
        self.greja = greja

hisyam = islam('hisyam', 'islam', 'sholat')
hisyam.perkenalan()
print(f'{hisyam.nama} beribadah dengan {hisyam.sholat}')

abraham = kristen('abraham', 'kristen', 'greja')
abraham.perkenalan()
print(f'{abraham.nama} beribadah ke {abraham.greja}')
