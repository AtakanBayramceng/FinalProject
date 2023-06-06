from Insan import Insan
from BeyazYaka import BeyazYaka
from Calisan import Calisan
from Issiz import Issiz
from MaviYaka import MaviYaka
import pandas as pd

print("Insan Class nesneleri")
insan1=Insan("12345678905","ali","veli","32","Erkek","azeri")
insan2=Insan("12342678905","Aytun","yilmazerler","42","Kadin","türk")
print(insan1)
print(insan2)

print("Issis class nesneleri")
issiz1=Issiz("12345678901","ahmet","Yasar","31","Erkek","türk",{"mavi yaka":3,"beyaz yaka":2,"yonetici":1})
issiz2=Issiz("12345678902","pelin","Ak","41","Kadin","türk",{"mavi yaka":5,"beyaz yaka":7,"yonetici":13})
issiz3=Issiz("12345678903","Burak","git","51","Erkek","türk",{"mavi yaka":8,"beyaz yaka":18,"yonetici":5})
print(issiz1)
print(issiz2)
print(issiz3)

print("Calisan class nesneleri")
calisan1=Calisan("12345678911","ahmet","Yasar","31","Erkek","türk","teknoloji",2,12000)
calisan2=Calisan("12345678921","mehmet","yilmaz","41","Erkek","türk","muhasebe",3,13000)
calisan3=Calisan("12345678931","berke","garaip","51","Erkek","türk","insaat",5,23000)
print(calisan1)
print(calisan2)
print(calisan3)

print("Mavi Yaka nesneleri")
MYaka1=MaviYaka("12345678811","alis","Yasar","33","Kadin","ingiliz","teknoloji",2,9000,0.3)
MYaka2=MaviYaka("12345678721","galip","yilmaz","44","Erkek","türk","muhasebe",4,15000,0.4)
MYaka3=MaviYaka("12345678631","geldi","garaip","55","Erkek","türk","insaat",6,18000,0.5)
print(MYaka1)
print(MYaka2)
print(MYaka3)

print("Beyaz Yaka Nesneleri")
BYaka1=BeyazYaka("22345678911","garip","Yasar","35","Erkek","türk","teknoloji",1,16000,0.5)
BYaka2=BeyazYaka("32345678921","kont","yilmaz","46","Erkek","türk","muhasebe",6,14000,0.2)
BYaka3=BeyazYaka("42345678931","gitti","garaip","48","Erkek","türk","insaat",3,22000,0.6)
print(BYaka1)
print(BYaka2)
print(BYaka3)

data = {
    "nesne_degeri": ["İnsan 1", "İnsan 2", "İşsiz 1", "İşsiz 2", "İşsiz 3", "Çalışan 1", "Çalışan 2", "Çalışan 3", "Mavi Yaka 1", "Mavi Yaka 2", "Mavi Yaka 3", "Beyaz Yaka 1", "Beyaz Yaka 2", "Beyaz Yaka 3"],
    "tc_no": [insan1.getTcNo(), insan2.getTcNo(), issiz1.getTcNo(), issiz2.getTcNo(), issiz3.getTcNo(), calisan1.getTcNo(), calisan2.getTcNo(), calisan3.getTcNo(), MYaka1.getTcNo(), MYaka2.getTcNo(), MYaka3.getTcNo(),BYaka1.getTcNo(), BYaka2.getTcNo(), BYaka3.getTcNo()],
    "ad": [insan1.getAd(), insan2.getAd(), issiz1.getAd(), issiz2.getAd(), issiz3.getAd(), calisan1.getAd(), calisan2.getAd(), calisan3.getAd(), MYaka1.getAd(), MYaka2.getAd(), MYaka3.getAd(),BYaka1.getAd(), BYaka2.getAd(), BYaka3.getAd()],
    "soyad": [insan1.getSoyad(), insan2.getSoyad(),issiz1.getSoyad(), issiz2.getSoyad(), issiz3.getSoyad(), calisan1.getSoyad(), calisan2.getSoyad(), calisan3.getSoyad(), MYaka1.getSoyad(), MYaka2.getSoyad(), MYaka3.getSoyad(),BYaka1.getSoyad(), BYaka2.getSoyad(), BYaka3.getSoyad()],
    "yas": [insan1.getYas(), insan2.getYas(),issiz1.getYas(), issiz2.getYas(), issiz3.getYas(), calisan1.getYas(), calisan2.getYas(), calisan3.getYas(), MYaka1.getYas(), MYaka2.getYas(), MYaka3.getYas(),BYaka1.getYas(), BYaka2.getYas(), BYaka3.getYas()],
    "cinsiyet": [insan1.getCinsiyet(), insan2.getCinsiyet(),issiz1.getCinsiyet(), issiz2.getCinsiyet(), issiz3.getCinsiyet(), calisan1.getCinsiyet(), calisan2.getCinsiyet(), calisan3.getCinsiyet(), MYaka1.getCinsiyet(), MYaka2.getCinsiyet(), MYaka3.getCinsiyet(),BYaka1.getCinsiyet(), BYaka2.getCinsiyet(), BYaka3.getCinsiyet()],
    "uyruk": [insan1.getUyruk(), insan2.getUyruk(),issiz1.getUyruk(), issiz2.getUyruk(), issiz3.getUyruk(), calisan1.getUyruk(), calisan2.getUyruk(), calisan3.getUyruk(), MYaka1.getUyruk(), MYaka2.getUyruk(), MYaka3.getUyruk(),BYaka1.getUyruk(), BYaka2.getUyruk(), BYaka3.getUyruk()],
    "sektor": ["", "", "", "", "", calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), MYaka1.get_sektor(), MYaka2.get_sektor(), MYaka3.get_sektor(),BYaka1.get_sektor(), BYaka2.get_sektor(), BYaka3.get_sektor()],
    "tecrube": ["", "", "", "", "", calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), MYaka1.get_tecrube(), MYaka2.get_tecrube(), MYaka3.get_tecrube(),BYaka1.get_tecrube(), BYaka2.get_tecrube(), BYaka3.get_tecrube()],
    "maas": ["", "", "", "", "", calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), MYaka1.get_maas(), MYaka2.get_maas(), MYaka3.get_maas(),BYaka1.get_maas(), BYaka2.get_maas(), BYaka3.get_maas()],
    "yipranma_payi": ["", "", "", "", "", "", "", "", MYaka1.get_yipranma_payi(), MYaka2.get_yipranma_payi(), MYaka3.get_yipranma_payi(), "", "", ""],
    "tesvik_primi": ["", "", "", "", "", "", "", "", "", "", "", BYaka1.get_tesvik_primi(), BYaka2.get_tesvik_primi(), BYaka3.get_tesvik_primi()],
    "yeni_maas": ["", "", "", "", "", calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki(), MYaka1.zam_hakki(), MYaka2.zam_hakki(), MYaka3.zam_hakki(), BYaka1.zam_hakki(), BYaka2.zam_hakki(), BYaka3.zam_hakki()]
}

df = pd.DataFrame(data)
print(df)
