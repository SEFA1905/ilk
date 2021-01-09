import sqlite3
import sys
class universite_sistemi:
    def __init__(self):
        self.durum = True

    def calıs(self):
        self.menu()
        secim = self.secim_yap()
        if secim == 1:
            self.kayit_yap()
            print("Kayıt İşleminiz Başarılı")
        if secim == 2:
            print("Yakında Gelecek ")
        if secim == 3:
            self.ogrenci_bak()
        if secim == 4:
            self.cikis_yap()

    def menu(self):
        print("""
              -----------Sisteme Hosgeldiniz-----------
                            1-Kayıt Yap
                            2-Kayıt Sil
                            3-Öğrenci Bilgisi Bak
                            4-Çıkıs Yap

              """)

    def secim_yap(self):
        try:
            while True:
                secim = int(input("Yapmak İstediğiniz İşlemi Seciniz:"))
                if secim < 1 or secim > 4:
                    print("Lütfen 1-4 Arasında Bir Sayı Giriniz:")
                else:
                    return secim
                    break

        except:
            print("Sayı Giriniz")
    def kayit_düzenle(self):
        pass
    def ogrenci_bak(self):
        self.verileri_al()
    def verileri_al(self):
        with sqlite3.connect('bilgiislem.vt')as dosya:
            imlec=dosya.cursor()
            imlec.execute("select numara from ogrenciler")
            bilgiler=imlec.fetchall()

            sayi=self.sırası_ne(bilgiler)
            self.veriler_goster(sayi)
            dosya.commit()

    def sırası_ne(self,bilgiler):
        a =0
        sayi=len(bilgiler)*6
        while True:
            try:
                numara=int(input("Bakmak İstediğiniz Öğrencinin Numarasını Giriniz"))
                break

            except:
                print("Numara Giriniz")
        while  a<sayi:
            try:

                if numara in bilgiler[a]:
                     return a
                     break
                else:
                    a+=1
            except :

                print("Aradığınız Kişi Bulunmadı Yeniden Deneyiniz")
                sys.exit()


    def veriler_goster(self,sayi):

        with sqlite3.connect('bilgiislem.vt')as dosya:
            imlec = dosya.cursor()
            imlec.execute("select * from ogrenciler")
            bilgiler = imlec.fetchall()
            print(bilgiler[sayi])
            dosya.commit()
    def bilgi_düzenle(self,v1,v2):
        tr2eng = str.maketrans("ÇçĞğıİşŞÜü", "CcGgiIsSUu")
        while True:
            v3 = input(f"Öğrencinin {v1} Giriniz:")
            v4 = v3.isspace()
            v5 = v3.isdigit()
            if v4 == True or v5 == True:
                print(f"Lütfen Geçerli Bir {v2} Giriniz")
            else:
                break

        v3 = v3.translate(tr2eng)
        v3 = v3.lower()
        v3 = v3.strip()
        return v3

    def kayit_yap(self):
        ad=self.ad_gir()
        soyad=self.soyad_gir()
        fakulte=self.fakulte_gir()
        bolum=self.bolum_gir()
        numara=self.numara_gir()
        durum1=self.durum_gir()




        bilgiler=[ad,soyad,fakulte,bolum,numara,durum1]
        with sqlite3.connect('bilgiislem.vt')as dosya:
            imlec=dosya.cursor()
            imlec.execute("create table if not exists ogrenciler(ad text,soyad text,fakulte text,bolum text,numara int,durum text)")
            imlec.execute("insert into ogrenciler values(?,?,?,?,?,?)",bilgiler)
            dosya.commit()

    def ad_gir(self):

        return self.bilgi_düzenle('Adını','Adı')

    def soyad_gir(self):

        return self.bilgi_düzenle('Soyadını','Soyadı')

    def fakulte_gir(self):

        return self.bilgi_düzenle('Fakültesini','Fakülteyi')

    def bolum_gir(self):

        return self.bilgi_düzenle('Bölümünü', 'Bölümü')

    def numara_gir(self):
        while True:
            try:
                    numara=int(input("Öğrencinin Numarasını Giriniz:"))
                    return numara
                    break

            except:
                print("Lütfen Numara Giriniz")


    def durum_gir(self):
        print("""
                     1-Aktif
                     2-Pasif

                 """)

        durum1 = int(input("Öğrencinin Durumunu Seçiniz:"))
        if durum1 == 1:
            durum2 = "Aktif"

        else:
            durum2 = "Pasif"
        return durum2




    def cikis_yap(self):
        self.durum = False


sistem = universite_sistemi()
while sistem.durum:
    sistem.calıs()
