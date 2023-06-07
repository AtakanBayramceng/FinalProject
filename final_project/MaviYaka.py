from Calisan import Calisan


class MaviYaka(Calisan):
    def __init__(self, tc,ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc,ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        # Calisan sınıfının __init__() metodunu çağırarak temel özellikleri tanımlıyoruz.
        self.__yipranma_payi = yipranma_payi
        self.__yeni_maas__=0

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            deger=0
            if self.get_tecrube() < 2:
                deger =self.__yipranma_payi * 10
                # Tecrübe 2 yıldan az ise yıpranma payını 10 ile çarparak değeri hesaplıyoruz.
            elif self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
                deger= (self.get_maas() * self.get_tecrube() / 2) + (self.__yipranma_payi * 10)
                # Tecrübe 2-4 yıl arasında ve maaş 15000'den düşükse, yeni maaş hesaplamasında tecrübe ve yıpranma payını kullanıyoruz.
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                # Tecrübe 4 yıldan fazla ve maaş 25000'den düşükse, yeni maaş hesaplamasında tecrübe ve yıpranma payını kullanıyoruz.
                deger =(self.get_maas() * self.get_tecrube() / 3) + (self.__yipranma_payi * 10)
            
            self.__yeni_maas__ = self.get_maas() + deger
            return self.__yeni_maas__
        except:
            print("Hata: Tecrübe veya maaş bilgisi hatalı.")

    def __str__(self):
        
        calisan_bilgileri = super().__str__()
        # Üst sınıftaki __str__() metoduyla elde edilen çalışan bilgilerini alıyoruz.
       # Ardından yıpranma payı ve yeni maaş bilgilerini ekleyerek bir metin döndürüyoruz.
        return f"{calisan_bilgileri}\nYıpranma Payı: {self.__yipranma_payi}\nYeni Maaş: {self.zam_hakki()}"
