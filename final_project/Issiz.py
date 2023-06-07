from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc,ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc,ad, soyad, yas, cinsiyet, uyruk)
        # Insan sınıfının __init__() metodunu çağırarak temel özellikleri tanımlanır.
        self.__tecrube = tecrube
        self.__statu = ""

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        try:
            # Farklı tecrube kategorilerinin etkisini hesaplanır.
            # Mavi yaka tecrübesi %20, beyaz yaka tecrübesi %35, yönetici tecrübesi %45 etkili oluyor.
            mavi_yaka_etkisi = self.__tecrube.get("mavi yaka", 0) * 0.20
            beyaz_yaka_etkisi = self.__tecrube.get("beyaz yaka", 0) * 0.35
            yonetici_etkisi = self.__tecrube.get("yonetici", 0) * 0.45

            if mavi_yaka_etkisi >= beyaz_yaka_etkisi and mavi_yaka_etkisi >= yonetici_etkisi:
                # Mavi yaka tecrübesi diğerlerine göre en büyükse, statü "mavi yaka" olarak belirlenir.
                self.__statu = "mavi yaka"
            elif beyaz_yaka_etkisi >= mavi_yaka_etkisi and beyaz_yaka_etkisi >= yonetici_etkisi:
                # Beyaz yaka tecrübesi diğerlerine göre en büyükse, statü "beyaz yaka" olarak belirlenir.
                self.__statu = "beyaz yaka"
            else:
                # Yukarıdaki koşullar sağlanmazsa, statü "yonetici" olarak belirlenir.
                self.__statu = "yonetici"
        except:
            print("Hata: Geçmiş tecrube bilgisi hatali veya eksik.")

    def __str__(self):
        self.statu_bul()
        # Statüyü belirlemek için statu_bul() metodunu çağırıyoruz.
        insan_bilgileri = super().__str__()
        # Üst sınıftaki __str__() metoduyla elde edilen insan bilgilerini alıyoruz.
        # Ardından statü bilgisini ekleyerek bir metin döndürüyoruz.
        return f"{insan_bilgileri}\nStatü: {self.__statu}"
