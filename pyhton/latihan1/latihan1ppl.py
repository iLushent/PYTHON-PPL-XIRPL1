#belajar object dan class

class kocheng:
    warna = None
    usia = None

class icikiwir:
    merk = None
    kecepatan = None



#membuat instance/variable sebagai "objek nyata"
#kocheng hitam menaiki icikiwir honda karbu dengan kecepatan 100km

pembalap_handal1 = kocheng()
pembalap_handal1 = icikiwir()
pembalap_handal1.warna = "hitam"
pembalap_handal1.merk = "honda karbu"
pembalap_handal1.kecepatan = "100km"

kocheng1 = kocheng()
kocheng1.warna = "grey"
kocheng1.usia = "4 bulan"

kocheng2 = kocheng()
kocheng2.warna = "putih"
kocheng2.usia = "3bulan"

print(kocheng1.warna, kocheng1.usia)
print(kocheng2.warna, kocheng2.usia)

