from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading

def servis_metotlarini_getir():
    return [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith("__")]

def temizle():
    system("cls||clear")

def hata_mesaji(renk, mesaj):
    temizle()
    print(renk + mesaj)
    sleep(3)

def telefon_kontrol(tel_no):
    try:
        int(tel_no)
        if len(tel_no) != 10:
            raise ValueError
        return True
    except ValueError:
        return False

def telefon_listesi_al():
    tel_liste = []
    tel_no = input(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa boş bırakınız): " + Fore.LIGHTGREEN_EX)
    
    if tel_no == "":
        temizle()
        dizin = input(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: " + Fore.LIGHTGREEN_EX)
        try:
            with open(dizin, "r", encoding="utf-8") as f:
                for i in f.read().strip().split("\n"):
                    if telefon_kontrol(i):
                        tel_liste.append(i)
        except FileNotFoundError:
            hata_mesaji(Fore.LIGHTRED_EX, "Hatalı dosya dizini. Tekrar deneyiniz.")
            return None
    else:
        if telefon_kontrol(tel_no):
            tel_liste.append(tel_no)
        else:
            hata_mesaji(Fore.LIGHTRED_EX, "Hatalı telefon numarası. Tekrar deneyiniz.")
            return None
    return tel_liste

def mail_al():
    mail = input(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız boş bırakınız): " + Fore.LIGHTGREEN_EX)
    if ("@" in mail and ".com" in mail) or mail == "":
        return mail
    else:
        hata_mesaji(Fore.LIGHTRED_EX, "Hatalı mail adresi.")
        return None

def sms_gonder_normal():
    temizle()
    tel_liste = telefon_listesi_al()
    if not tel_liste:
        return

    temizle()
    mail = mail_al()
    if mail is None:
        return

    temizle()
    try:
        kere_input = input(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun (sonsuz için boş bırak): " + Fore.LIGHTGREEN_EX)
        kere = int(kere_input) if kere_input else None
    except ValueError:
        hata_mesaji(Fore.LIGHTRED_EX, "Hatalı giriş. Sayı giriniz.")
        return

    temizle()
    try:
        aralik = int(input(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.LIGHTGREEN_EX))
    except ValueError:
        hata_mesaji(Fore.LIGHTRED_EX, "Hatalı sayı girdin.")
        return

    temizle()
    for tel in tel_liste:
        sms = SendSms(tel, mail)
        if kere is None:
            while True:
                for method in servis_metotlarini_getir():
                    getattr(sms, method)()
                    sleep(aralik)
        else:
            while sms.adet < kere:
                for method in servis_metotlarini_getir():
                    if sms.adet >= kere:
                        break
                    getattr(sms, method)()
                    sleep(aralik)

    print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
    input()

def sms_gonder_turbo():
    temizle()
    tel_no = input(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.LIGHTGREEN_EX)
    if not telefon_kontrol(tel_no):
        hata_mesaji(Fore.LIGHTRED_EX, "Hatalı numara.")
        return

    temizle()
    mail = mail_al()
    if mail is None:
        return

    temizle()
    send_sms = SendSms(tel_no, mail)
    dur = threading.Event()

    def turbo_gonder():
        while not dur.is_set():
            threadler = []
            for metot in servis_metotlarini_getir():
                t = threading.Thread(target=getattr(send_sms, metot), daemon=True)
                threadler.append(t)
                t.start()
            for t in threadler:
                t.join()

    try:
        turbo_gonder()
    except KeyboardInterrupt:
        dur.set()
        temizle()
        print(Fore.LIGHTRED_EX + "Ctrl+C algılandı. En Başa Dönülüyor...")
        sleep(2)

def menu_goster():
    temizle()
    print(Fore.LIGHTCYAN_EX + """
       ____   ________      ____       ____      ____   ________      ____   ___       ___
      6MMMMb/ `MMMMMMMb.   6MMMMb     6MMMMb/   6MMMMb  `MMMMMMMb.   6MMMMb  `MMb     dMM'
     8P    YM  MM    `Mb  8P    Y8   8P    YM  8P    Y8  MM    `Mb  8P    Y8  MMM.   ,PMM 
    6M      Y  MM     MM 6M      Mb 6M      Y 6M      Mb MM     MM 6M      Mb M`Mb   d'MM 
    MM         MM     MM MM      MM MM        MM      MM MM    .M9 MM      MM M YM. ,P MM 
    MM         MM    .M9 MM      MM MM        MM      MM MMMMMMM(  MM      MM M `Mb d' MM 
    MM         MMMMMMM9' MM      MM MM        MM      MM MM    `Mb MM      MM M  YM.P  MM 
    MM         MM  \\M\\   MM      MM MM        MM      MM MM     MM MM      MM M  `Mb'  MM 
    YM      6  MM   \\M\\  YM      M9 YM      6 YM      M9 MM     MM YM      M9 M   YP   MM 
     8b    d9  MM    \\M\\  8b    d8   8b    d9  8b    d8  MM    .M9  8b    d8  M   `'   MM 
      YMMMM9  _MM_    \\M\\_ YMMMM9     YMMMM9    YMMMM9  _MMMMMMM9'   YMMMM9  _M_      _MM_   
    """ + Style.RESET_ALL + Fore.CYAN + "\nby @raviento\n")

    print(Fore.LIGHTMAGENTA_EX + "\n 1- SMS Gönder (Normal)\n 2- SMS Gönder (Hepsi Bir Anda)\n 3- Çıkış\n")
    return input(Fore.LIGHTYELLOW_EX + " Seçim: ")

def main():
    while True:
        secim = menu_goster()
        if secim == "1":
            sms_gonder_normal()
        elif secim == "2":
            sms_gonder_turbo()
        elif secim == "3":
            temizle()
            print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
            break
        else:
            hata_mesaji(Fore.LIGHTRED_EX, "Geçersiz seçim.")

if __name__ == "__main__":
    main()
