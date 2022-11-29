from fungsi import ani
from fungsi import loop
from fungsi import minmax
    
def inputUlang():
    print("===================")
    pilih = input("Apakah kamu ingin mengulang program? (y/n)")
    
    while(pilih == "y"):
        allMenu()
        break

def allMenu():
    print("===================")
    print("Rehan Kurnia Hidayat")
    print("11121089")
    print("2KA01")
    print("===================")

    print("Pilih program yang ingin dijalankan")
    print("[1] Program Ani")
    print("[2] Program Looping")
    print("[3] Program MinMax")
    print("[4] Exit Program")
    angka = int(input("Masukkan pilihan anda : "))

    if angka == 1:
        ani.menu()
        inputUlang()
    elif angka == 2:
        loop.menu()
        inputUlang()
    elif angka == 3:
        minmax.menu()
        inputUlang()
    elif angka == 4:
        exit()
    else:
        print("Pilihan tidak ditemukan")
        
allMenu()
  