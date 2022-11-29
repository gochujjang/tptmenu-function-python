def sgt_bintang():
    tinggi = int(5)
    for i in range(tinggi):
        for j in range(i+1):
            print("* ",end='')
        print()

def sgt_angka():
    i = 5
    for i in range(1, i+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print("")
        
def sgt_pola():
    i = 1

    while(i <= 4):
        j = 1
        k = i
        while(j <= i):
            print(k, end=" ")
            k = k + 4 - j
            j+=1
        i+=1
        print()

    

def menu():
    print("========== Program Looping ==========")
    print("[1] Segitiga Bintang")
    print("[2] Segitiga Angka")
    print("[3] Segitiga Angka Pola")
    print("[4] Exit Program")
    
    angka = int(input("Masukkan pilihan anda : "))

    if angka == 1:
        sgt_bintang()
    elif angka == 2:
        sgt_angka()
    elif angka == 3:
        sgt_pola()
    elif angka == 4:
        exit()
    else:
        print("Pilihan tidak ditemukan")