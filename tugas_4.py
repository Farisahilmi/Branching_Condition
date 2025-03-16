nilai_1 = int(input("nilai 1: "))
nilai_2 = int(input("nilai 2: "))
nilai_3 = int(input("nilai 3: "))


if nilai_1 > nilai_2 and nilai_1 > nilai_3 :
    print("nilai 1 lebih besar, nilainya: ", nilai_1)
elif nilai_2 > nilai_1 and nilai_2 > nilai_3 :
    print("nilai 2 lebih besar, nilainya: ", nilai_2)
else:
    print("nilai 3 lebih besar, nilainya: ", nilai_3)