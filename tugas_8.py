a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))

if a + b > c and a + c > b and b + c > a:  # Syarat segitiga
    if a == b == c:
        jenis = "Segitiga Sama Sisi"
    elif a == b or a == c or b == c:
        jenis = "Segitiga Sama Kaki"
    else:
        jenis = "Segitiga Sembarang"
    print(f"Ini adalah {jenis}")
else:
    print("Tiga angka ini tidak dapat membentuk segitiga")
