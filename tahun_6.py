x = float(input("Masukkan angka pertama: "))
y = float(input("Masukkan angka kedua: "))
op = input("Masukkan operator (+, -, *, /): ")

if op == "+":
    hasil = x + y
elif op == "-":
    hasil = x - y
elif op == "*":
    hasil = x * y
elif op == "/":
    if y != 0:
        hasil = x / y
    else:
        hasil = "error"
else:
    hasil = "Error: Operator tidak valid"

print("Hasil:", hasil)
