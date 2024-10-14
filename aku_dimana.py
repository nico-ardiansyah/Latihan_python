""" Permainan Tebak Aku DImana """
import random

print("***********************************************")
print("*** Selamat Datang di Game Tebak Aku Dimana ***")
print("***********************************************")


while True:
    bentuk = "|_|"  
    kotak = [bentuk] * 4
    daftar_kotak = kotak.copy()   
    random_nilai = random.randint(1,4)
    daftar_kotak[random_nilai - 1]= "|^v^|"
    kotak = ' '.join(kotak)
    daftar_kotak = ' '.join(daftar_kotak)
    
    print ("\nPerhatikan Keempat Kotak Dibawah Ini ")
    print (f'''\n{kotak}\n''')
    tebak = int(input("\nTebak aku dimana [1,2,3,4] : "))
    if tebak == random_nilai:
        print (f"\nSelamat Kamu Berhasil Menemukan Ku {daftar_kotak} :")
        lanjut = input("\nApakah kamu mau lanjut bermain [y/n] : ")
        if lanjut == "y":
            continue
        else:
            print ("\nGame Berhenti")
            break
    else:
        print("\nKamu kalah")
        print(f"\nTernyata aku ada di sini {daftar_kotak}")
        lanjut = input("\nApakah kamu mau lanjut bermain [y/n] : ")
        if lanjut == "y":
            continue
        else:
            print ("\nGame Berhenti")
            break
