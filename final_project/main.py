from Insan import Insan
from BeyazYaka import BeyazYaka
from Calisan import Calisan
from Issiz import Issiz
from MaviYaka import MaviYaka
import pandas as pd

print("\nInsan Class nesneleri")
print("**************************************************")
insan1=Insan("12345678905","ali","veli","32","Erkek","azeri")
insan2=Insan("12342678905","Aytun","yilmazerler","42","Kadin","türk")
print(insan1)
print(insan2)

print("\nIssis class nesneleri")
print("**************************************************")
issiz1=Issiz("12345678901","ahmet","Yasar","31","Erkek","türk",{"mavi yaka":3,"beyaz yaka":2,"yonetici":1})
issiz2=Issiz("12345678902","pelin","Ak","41","Kadin","türk",{"mavi yaka":5,"beyaz yaka":7,"yonetici":13})
issiz3=Issiz("12345678903","Burak","git","51","Erkek","türk",{"mavi yaka":8,"beyaz yaka":18,"yonetici":5})
print(issiz1)
print(issiz2)
print(issiz3)

print("\nCalisan class nesneleri")
print("**************************************************")
calisan1=Calisan("12345678911","ahmet","Yasar","31","Erkek","türk","teknoloji",2,12000)
calisan2=Calisan("12345678921","mehmet","yilmaz","41","Erkek","türk","muhasebe",3,13000)
calisan3=Calisan("12345678931","berke","garaip","51","Erkek","türk","insaat",5,23000)
print(calisan1)
print(calisan2)
print(calisan3)

print("\nMavi Yaka nesneleri")
print("**************************************************")
MYaka1=MaviYaka("12345678811","alis","Yasar","33","Kadin","ingiliz","teknoloji",2,9000,0.3)
MYaka2=MaviYaka("12345678721","galip","yilmaz","44","Erkek","türk","muhasebe",4,15000,0.4)
MYaka3=MaviYaka("12345678631","geldi","garaip","55","Erkek","türk","insaat",6,18000,0.5)
print(MYaka1)
print(MYaka2)
print(MYaka3)

print("\nBeyaz Yaka Nesneleri")
print("**************************************************")
BYaka1=BeyazYaka("22345678911","garip","Yasar","35","Erkek","türk","teknoloji",1,16000,0.5)
BYaka2=BeyazYaka("32345678921","kont","yilmaz","46","Erkek","türk","muhasebe",6,14000,0.2)
BYaka3=BeyazYaka("42345678931","gitti","garaip","48","Erkek","türk","insaat",3,22000,0.6)
print(BYaka1)
print(BYaka2)
print(BYaka3)

# data frame içeren dictionary oluşturldu
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

try:
        
    # daataframe oluşturldu
    df = pd.DataFrame(data)
    # data frama yazdırıldı
    print(df)

    print("\n==== TASK a ====\n")
    # data frame içerisindeki boş değerler 0 ile değiştirldi
    df["nesne_degeri"].replace("",0, inplace=True)
    df["tc_no"].replace("",0, inplace=True)
    df["ad"].replace("",0, inplace=True)
    df["soyad"].replace("",0, inplace=True)
    df["yas"].replace("",0, inplace=True)
    df["cinsiyet"].replace("",0, inplace=True)
    df["uyruk"].replace("",0, inplace=True)
    df["sektor"].replace("",0, inplace=True)
    df["tecrube"].replace("",0, inplace=True)
    df["maas"].replace("",0, inplace=True)
    df["yipranma_payi"].replace("",0, inplace=True)
    df["tesvik_primi"].replace("",0, inplace=True)
    df["yeni_maas"].replace("",0, inplace=True)

    # oluşan data frame ekrana bastırıldı
    print(df)
    print("===============")


    print("\n==== TASK B ====\n")
    # çalışan i mavi yaka ve bayaz yakalı insanları şndex numaralarına göre data framedan çektik
    selected_data = df[(df['nesne_degeri'].index >= 5) & (df['nesne_degeri'].index <= 13)]

    # seçilenlerin tecrübe ortalamalırın aldık
    tecrube_ortalama = selected_data['tecrube'].mean()
    # seçilenlerin maas ortlamarını aldık
    maas_ortalama = selected_data['maas'].mean()

    # Ortalamaları yazdırma
    print("Seçilen verilere göre Tecrübe Ortalaması:", tecrube_ortalama)
    print("Seçilen verilere göre Maaş Ortalaması:", maas_ortalama)
    print("=========")
    print("\n==== TASK C ====\n")

    # maası 15.000 den fazla olan çalışan sayısı lis olarak döndürüldü
    maas_ust_limit_ustu = df[df['maas'] > 15000]
    # list eleman sayısı maaşı 15000den fazla olan çalışan sayısını verecektir
    toplam_sayi = len(maas_ust_limit_ustu)

    print("Maaşı 15000TL üzerinde olanların toplam sayısı:", toplam_sayi)

    print("\n==== TASK D ====\n")

    # panda frame içerisinde sort fonksiyonunu kullanrak yeni maasa göre insanalrı sıraladık
    df_sorted = df.sort_values(by='yeni_maas')
    print(df_sorted)

    print("\n==== TASK E ====\n")

    # panda frame içerisindeki beyaz yakalıların tecrübesi 3 seneden fazla olanları bulduk
    beyaz_yaka_filtered = df[(df['nesne_degeri'].index >= 11) & (df['nesne_degeri'].index <= 13) & (df['tecrube'] > 3)]
    print(beyaz_yaka_filtered)

    print("\n==== TASK F ====\n")
    # panda frame içerisindeki maaşı 10000den fazka olanların tc_no ve yeni maaş bilgilerini aldık
    filtered_data = df[(df['yeni_maas'] > 10000)].iloc[2:6][['tc_no', 'yeni_maas']]
    print(filtered_data)

    print("\n==== TASK G ====\n")
    # panda frame den ad soyad sektor ve yeni maas bilgilari kullanarak yeni bir data frama oluşturduk
    new_df = df[['ad', 'soyad', 'sektor', 'yeni_maas']]

    print(new_df)
except:
    print("Data frame oluşurken veya işlemler esnasında bir hata oluştu")