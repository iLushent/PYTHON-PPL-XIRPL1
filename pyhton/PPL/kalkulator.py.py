print("Kalkulator luas bidang datar")
pilihan = input("Masukan pilihan 1 sampai 4 = ")

if pilihan == "1":
    print("Rumus luas segitiga")
    a = int(input("Masukan alas = "))
    t = int(input("Masukan tinggi = "))
    print("Hasilnya = ", 0.5 * a * t)
elif  pilihan == "2":
    print("Rumus luas lingkaran")
    r = int(input("Masukan r = "))
    print("Hasilnya = ", 3.14 * r * r)
elif  pilihan == "3":
    print("Rumus luas persegi panjang")
    p = int(input("Masukan panjang = "))
    l = int(input("Masukan lebar = "))
    print("Hasilnya = ", p * l)
elif  pilihan == "4":
    print("Rumus luas jajar genjang")
    a = int(input("Masukan alas = "))
    t = int(input("Masukan tinggi = "))
    print("Hasilnya = ", a * t )
else: print("Error")