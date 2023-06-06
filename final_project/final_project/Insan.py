class Insan:
    def __init__(self, tcNo, ad, soyad, yas, cinsiyet, uyruk):
        self.__tcNo = tcNo
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
    
    #tc no dondürür
    def getTcNo(self):
        return self.__tcNo
    #tc no değiştirir
    def setTcNo(self, tcNo):
        self.__tcNo = tcNo

    #ad dondürür
    def getAd(self):
        return self.__ad
    #ad değiştirir
    def setAd(self, ad):
        self.__ad = ad

    #soyad dondürür
    def getSoyad(self):
        return self.__soyad
    #soyad değiştirir
    def setSoyad(self, soyad):
        self.__soyad = soyad

    #yaşı dondürür
    def getYas(self):
        return self.__yas
    #yaşı değiştirir
    def setYas(self, yas):
        self.__yas = yas
    #cinsiyet dondürür
    def getCinsiyet(self):
        return self.__cinsiyet

    #Cinsiyet değiştirir
    def setCinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    #Uyurk döndürür
    def getUyruk(self):
        return self.__uyruk
    #Uyruk döndürür
    def setUyruk(self, uyruk):
        self.__uyruk = uyruk
    
    #Kullanıcı bilgilerini ekrana yazdırır
    def __str__(self):
        return f"TC No: {self.__tcNo}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}"

