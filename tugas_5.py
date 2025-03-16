tahun = int(input("Masukkan tahun yang ingin diperiksa: "))

if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")