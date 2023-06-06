import Calisan

class MaviYaka(Calisan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                return self.__yipranma_payi * 10
            elif self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_tecrube() / 2) + (self.__yipranma_payi * 10)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / 3) + (self.__yipranma_payi * 10)
            else:
                return 0
        except:
            print("Hata: Tecrübe veya maaş bilgisi hatalı.")

    def __str__(self):
        yeni_maas = self.get_maas() + self.zam_hakki()
        calisan_bilgileri = super().__str__()
        return f"{calisan_bilgileri}\nYıpranma Payı: {self.__yipranma_payi}\nYeni Maaş: {yeni_maas}"
