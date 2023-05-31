import Insan

class Calisan(Insan):
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        try:
            if self.__tecrube < 2:
                return 0
            elif self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
                return self.__maas * self.__tecrube / 100
            elif self.__tecrube > 4 and self.__maas < 25000:
                return (self.__maas * self.__tecrube) / 200
            else:
                return 0
        except:
            print("Hata: Tecrübe veya maaş bilgisi hatali.")

    def __str__(self):
        yeni_maas = self.__maas + self.zam_hakki()
        insan_bilgileri = super().__str__()
        return f"{insan_bilgileri}\nTecrübe: {self.__tecrube} ay\nYeni Maaş: {yeni_maas}"


