import random

pilihan = ["batu", "gunting", "kertas"]

pemain = input("Pilih (batu/gunting/kertas): ").lower()
komputer = random.choice(pilihan)

print(f"Komputer memilih: {komputer}")

if pemain == komputer:
    print("Seri!")
elif (pemain == "batu" and komputer == "gunting") or \
    (pemain == "gunting" and komputer == "kertas") or \
    (pemain == "kertas" and komputer == "batu"):
    print("Kamu menang!")
else:
    print("Kamu kalah!")
