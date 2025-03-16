berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

bmi = berat / (tinggi ** 2)

if bmi < 18.5:
    kategori = "Kurus (Underweight)"
elif bmi < 25.0:
    kategori = "Normal"
elif bmi < 30.0:
    kategori = "Gemuk (Overweight)"
else:
    kategori = "Obesitas (Obese)"

print(f"BMI Anda: {bmi:.2f}")
print(f"Kategori: {kategori}")
