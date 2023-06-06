import Calisan

class BeyazYaka(Calisan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                return self.__tesvik_primi
            elif self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_tecrube() / 100) + self.__tesvik_primi
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / 25) + self.__tesvik_primi
            else:
                return 0
        except:
            print("Hata: Tecrübe veya maaş bilgisi hatalı.")

    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        calisan_bilgileri = super().__str__()
        return f"{calisan_bilgileri}\nTeşvik Prim: {self.__tesvik_primi}\nYeni Maaş: {yeni_maas}"
