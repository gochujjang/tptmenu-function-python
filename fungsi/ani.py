def ani():
    jeruk = int(input("Jumlah jeruk : "))
    teman = int(input("Jumlah teman : "))

    hasil = int(jeruk / teman)

    print("Maka jeruk yang dibagikan sebanyak : ", hasil)    

def aniDtg():
    waktu = input("Kapan Ani datang? ")

    if waktu.upper() == "PAGI":
        jeruk = int(input("Masukkan banyaknya jeruk : "))
        teman = int(input("Masukkan banyaknya teman : "))
        hasil = int(jeruk/teman)
        print("Banyaknya jeruk yang diterima teman adalah ", hasil)
    else:
        apel = int(input("Masukkan banyaknya apel : "))
        teman = int(input("Masukkan banyaknya teman : "))
        hasil = int(apel/teman)
        print("Banyaknya apel yang diterima teman adalah ", hasil)


def menu():
    print("========== Program Ani ==========")
    print("[1] Program Ani")
    print("[2] Program Ani Kedatangan")
    print("[3] Exit Program")
    
    angka = int(input("Masukkan pilihan anda : "))

    if angka == 1:
        ani()
    elif angka == 2:
        aniDtg()
    elif angka == 3:
        exit()
    else:
        print("Pilihan tidak ditemukan")
        
    