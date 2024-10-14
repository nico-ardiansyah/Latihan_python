import random

print("**********************************")
print("***  Selamat Datang Di Casino  ***")
print("***   Pasang Taruhan & Menang  ***")
print("**********************************")

bank = []
admin = []
while True:
    angka = random.randint(1,5)
    bank.append(int(input("\nPasang Taruhan Kamu :")))
    upah = bank[-1]
    menang = upah * 2
    admin.append(menang)
    untung = sum(bank) - sum(admin)
    print ("\nSilahkan Pilih Angka 1 Sampai 5")
    pilahan_user = int(input("Masukkan Angka : "))
    if (pilahan_user) == angka :
        print (f"\nSelamat Kamu Menang {menang}")
        print ("\n**********************************************")
        print ("**** Terima kasih sudah bermain di Casino ****")
        print (f'''      Keuntungan Admin : {untung}           ''') 
        print ("**********************************************")
        berhenti = input("\nApakah mau mencoba lagi ? pilih [y/n] : ")
        if berhenti == 'y':
            continue
        elif berhenti == 'n':
            print ("\n**********************************************")
            print ("**** Terima kasih sudah bermain di Casino ****")
            print (f'''       Keuntungan Admin : {untung}           ''') 
            print ("**********************************************")
            break
        else:
            print("\nWarning !!! Salah Input")
        break
    elif (pilahan_user) != angka :
        print ("\n*********************")
        print ("*** Kamu Kalah !! ***")
        print ("*********************")
        berhenti = input("\nApakah mau mencoba lagi ? pilih [y/n] : ")
        if berhenti == 'y':
            continue
        if berhenti == 'n':
            print ("\n**********************************************")
            print ("**** Terima kasih sudah bermain di Casino ****")
            print (f'''       Keuntungan Admin : {sum(bank)}           ''') 
            print ("**********************************************")
        else:
            print ("warning !! Salah Input")
            break
