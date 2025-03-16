username = input("masukan username: ")
password = input("masukan password: ")

if username == "admin" and password == "admin123":
    print("akses admin")
elif username == "user" and password == "user123":
    print("akses terbatas")
elif username == "guest":
    print("akses minimal")
else:
    print("kombinasi lain ditolak")