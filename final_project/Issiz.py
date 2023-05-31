import Insan
class Issiz(Insan):
    def __init__(self, ad, soyad, tecrube):
        super().__init__(ad, soyad, None, None, None)
        self.__tecrube = tecrube
        self.__statu = ""

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        try:
            mavi_yaka_etkisi = self.__tecrube.get("mavi yaka", 0) * 0.20
            beyaz_yaka_etkisi = self.__tecrube.get("beyaz yaka", 0) * 0.35
            yonetici_etkisi = self.__tecrube.get("yonetici", 0) * 0.45

            if mavi_yaka_etkisi >= beyaz_yaka_etkisi and mavi_yaka_etkisi >= yonetici_etkisi:
                self.__statu = "mavi yaka"
            elif beyaz_yaka_etkisi >= mavi_yaka_etkisi and beyaz_yaka_etkisi >= yonetici_etkisi:
                self.__statu = "beyaz yaka"
            else:
                self.__statu = "yonetici"
        except:
            print("Hata: Geçmiş tecrube bilgisi hatalı veya eksik.")

    def __str__(self):
        self.statu_bul()
        insan_bilgileri = super().__str__()
        return f"{insan_bilgileri}\nStatü: {self.__statu}"
