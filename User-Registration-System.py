veriler={}

def numara_rakam_kontrol(numara):
    return numara.isdigit()

def numara_kontrol(numara):
    return(
        len(numara)==11 and numara.startswith("05") and numara_rakam_kontrol(numara)
    )

def dogum_yeri_kontrol(dogum_yeri):
    return dogum_yeri.isalpha()

def veri_giris():
    i=1
    while i <= 25:
        print(f"\n{i}Bilgilerinizi giriniz.")
        ad=input("Ad: ").strip()
        soyad=input("Soyad: ").strip()

        while True:
            numara=input("Telefon numaranızı giriniz, format(05xxxxxxxxx):").strip()
            if numara_kontrol(numara):
                break
            else:
                print("Telefon numarası geçersiz, tekrar deneyiniz.")

        while True:
            dogum_yeri=input("Doğum yerinizi giriniz.").strip()
            if dogum_yeri_kontrol(dogum_yeri):
                break
            else:
                print("Doğum yeri geçersiz, tekrar deneyiniz.")

        veriler[i]={
            "ad":ad,
            "soyad":soyad,
            "telefon numarası":numara,
            "doğum yeri":dogum_yeri
        }
        i+=1
        print("\nVeri girişi bitti.")

veri_giris()

def verileri_kaydet(veriler, dosya_adi="kisiler.txt"):
    try:
        with open(dosya_adi,"a") as f:
            for kisi in veriler.values():
                f.write(f"{kisi['ad']},{kisi['soyad']},{kisi['numara']},{kisi['dogum_yeri']}\n")
            return "Veriler başarıyla eklendi."
    except Exception as e:
        return f"Hata oluştu {str(e)}"
sonuc=verileri_kaydet(veriler)
print(sonuc)