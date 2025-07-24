import time

dersler = []
notlar = []

while True:
    print("\n Not Menüsü")
    print("-1- Ders Ekle")
    print("-2- Ders Sil")
    print("-3- Dersleri Listele")
    print("-4- Derse Not Ekle")
    print("-5- Ders Notunu Sil")
    print("-6- Ders Notlarını Listele")
    print("-7- Çıkış")

    secim = input("Seçiminizi yapınız (1-7): ")

    if secim == '1':
        ders_ekle = input("Ders adını giriniz: ")
        dersler.append(ders_ekle)
        print("Ders eklendi:", ders_ekle)
        time.sleep(1)

    elif secim == '2':
        ders_sil = input("Silinecek dersi giriniz: ")
        if ders_sil in dersler:
            dersler.remove(ders_sil)
            print("Ders silindi:", ders_sil)
        else:
            print("Böyle bir ders bulunamadı.")
        time.sleep(1)

    elif secim == '3':
        print("\nDers Listesi:")
        print(dersler)
        time.sleep(2)

    elif secim == '4':
        not_ekleme_dersi = input("Not eklemek istediğiniz dersi giriniz: ")
        if not_ekleme_dersi in dersler:
            not_ekle = input("Notu giriniz: ")
            not_kaydi = f"{not_ekleme_dersi} - {not_ekle}"
            notlar.append(not_kaydi)
            print("Not eklendi:", not_kaydi)
        else:
            print("Bu ders bulunamadı, önce dersi ekleyiniz.")
        time.sleep(1)

    elif secim == '5':
        not_silme_dersi = input("Not silmek istediğiniz dersi giriniz: ")
        not_sil = input("Silinecek notu giriniz: ")
        not_kaydi = f"{not_silme_dersi} - {not_sil}"
        if not_kaydi in notlar:
            notlar.remove(not_kaydi)
            print("Not silindi:", not_kaydi)
        else:
            print("Böyle bir not bulunamadı.")
        time.sleep(1)

    elif secim == '6':
        print("\nNot Listesi:")
        print(notlar)
        time.sleep(2)

    elif secim == '7':
        print("Çıkılıyor...")
        time.sleep(0.5)
        break

    else:
        print("Geçersiz seçim, lütfen 1-7 arasında bir değer giriniz.")
        time.sleep(1)
