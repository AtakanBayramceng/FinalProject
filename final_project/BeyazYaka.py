from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self,tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc,ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
        self.__yeni_maas__=0
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            deger=0
            if self.get_tecrube() < 2:
                # Eğer çalışanın tecrübesi 2 yıldan azsa,
                # teşvik primi değerini geri döndürür.
                deger= self.__tesvik_primi
            elif self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
                # Eğer çalışanın tecrübesi 2 ile 4 yıl arasında ve maaşı 15000'den düşükse,
               # maaşına tecrübe yüzdesiyle birlikte teşvik primini ekler.
                deger= (self.get_maas() * self.get_tecrube() / 100) + self.__tesvik_primi
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                # Eğer çalışanın tecrübesi 4 yıldan fazla ve maaşı 25000'den düşükse,
                # maaşına tecrübe yüzdesinin 1/25'i kadarını ekler.
                deger= (self.get_maas() * self.get_tecrube() / 25) + self.__tesvik_primi
            
            self.__yeni_maas__ = self.get_maas() + deger
            return self.__yeni_maas__
            
        except:
            print("Hata: Tecrübe veya maaş bilgisi hatalı.")

    def __str__(self):
        calisan_bilgileri = super().__str__()
        # Üst sınıftaki __str__() metoduyla elde edilen çalışan bilgilerini alır.
        # Ardından teşvik primi ve yeni maaş bilgilerini ekleyerek bir metin döndürür.
        return f"{calisan_bilgileri}\nTeşvik Prim: {self.__tesvik_primi}\nYeni Maaş: {self.zam_hakki()}"
