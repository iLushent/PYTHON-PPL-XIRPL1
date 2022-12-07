#membuat variable atau box bernama buah
buah = ["apel", "durian", "kiwi", "alpukat", "mangga"]
sayur =["pokcoy", "sledri", "kangkung", "bayem", "asem"]

#tampilkan data yang ada divariable buah
#print (buah)

#tamppilkan data berurutan dari awal hingga akhir
#for gerobak in buah:
    #print(gerobak)

#tampilkan hanya beberapa data saja
#print(buah[0], buah[2])

#cara menambah nilai didalam list


#cara menghapus yang ada didalam buah
#buah.remove(2)
#print(buah)

#cara memmotong nilai yang ada di box buah
#print(buah[1:4]) 

#dagang_Hari_Ini = buah + sayur

#for gerobak in dagang_Hari_Ini:
    #print(gerobak)

kasir = input("Mau tambah buah apa lagi : ")
buah.append(kasir)
print(buah)