def max(angka1, angka2):
    if angka1 > angka2:
        return angka1
    else:
        return angka2

def min(angka1, angka2):
    if angka1 < angka2:
        return angka1
    else:
        return angka2
    

def menu():
    print("Menentukan Nilai Maksimum dan Minimum dari 2 Angka")
    angka1 = int(input("Masukkan Angka Pertama : "))
    angka2 = int(input("Masukkan Angka Kedua : "))
    print("Nilai Maksimumnya adalah : ", max(angka1, angka2))
    print("Nilai Minimumnya adalah : ", min(angka1, angka2))