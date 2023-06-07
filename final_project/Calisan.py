from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc,ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc,ad, soyad, yas, cinsiyet, uyruk)
        # Insan sınıfının __init__() metodunu çağırarak temel özellikleri tanımlıyoruz.
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
                # Eğer çalışanın tecrübesi 2 yıldan azsa, zam hakkı 0 olarak döner.
                return 0
            elif self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
                # Eğer çalışanın tecrübesi 2 ile 4 yıl arasında ve maaşı 15000'den düşükse,
                # maaşına tecrübe yüzdesiyle birlikte zam yapılır.
                return self.__maas * self.__tecrube / 100
            elif self.__tecrube > 4 and self.__maas < 25000:
                # Eğer çalışanın tecrübesi 4 yıldan fazla ve maaşı 25000'den düşükse,
                # maaşına tecrübenin 1/200'i kadar zam yapılır.
                return (self.__maas * self.__tecrube) / 200
            else:
                return 0
        except:
            print("Hata: Tecrübe veya maaş bilgisi hatali.")

    def __str__(self):
        yeni_maas = self.__maas + self.zam_hakki()
        # Zam hakkı hesaplanarak yeni maaş belirlenir.
        insan_bilgileri = super().__str__()
        # Üst sınıftaki __str__() metoduyla elde edilen insan bilgilerini alıyoruz.
        # Ardından tecrübe ve yeni maaş bilgilerini ekleyerek bir metin döndürüyoruz.
        return f"{insan_bilgileri}\nTecrübe: {self.__tecrube} ay\nYeni Maaş: {yeni_maas}"


