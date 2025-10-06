def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def kali(a,b):
    return a*b

def bagi(a,b):
    return a/b

def buletin(a,b):
    return a//b

def pangkat(a,b):
    return a**b


print("===WELCOME TO SIMPLE CALCULATOR BY RAPIE===\n")

while True:
    angka1 = float(input("MASUKKAN ANGKA PERTAMA KAMU: "))
    angka2 = float(input("MASUKKAN ANGKA KEDUA KAMU JUGA: "))

    print("\nUDAH? OKE SEKARANG MASUKKAN OPERASI YANG MAU KAMU PAKE, PAKE SIMBOL INI KALO GA PAKE GA BISA YAK: + - * / ^")
    operasi=input("MASUKKIN DISINI ")

    if operasi == '+':
        hasil = tambah(angka1, angka2)
        print(f"HASILNYA ADALAH: {hasil}")
    elif operasi == '-' :
        hasil = kurang(angka1, angka2)
        print(f"HASILNYA ADALAH: {hasil}")
    elif operasi == '*' :
        hasil = kali(angka1, angka2)
        print(f"HASILNYA ADALAH: {hasil}")
    elif operasi == '/' :
        hasil_biasa = bagi(angka1, angka2)
        hasil_buletin = buletin(angka1, angka2)
        print(f"HASIL PEMBAGIAN ADALAH: {hasil_biasa}")
        print(f"HASIL PEMBAGIAN YANG TELAH DIBULATKAN ADALAH: {hasil_buletin}")
    elif operasi == '^' :
        hasil = pangkat(angka1, angka2)
        print(f"HASILNYA ADALAH: {hasil}")
    else:
        print("TETOTTT, SALAH")

    ulang=input("\nKAMU MAU NGITUNG LAGI? (IYA/GA)")
    if ulang.upper().strip() != 'IYA' :
        print("TERIMAKASIH UDAH PAKAI LAYANAN INI")
        break