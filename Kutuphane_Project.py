#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:07:53 2021

@author: mertsamast
"""

# =============================================================================
# Kütüphane Projei
# 2 tane sınıf olacak. Kütüphane ve Kitap sınıfı
# Kitaplar, kütüphane veri tabanında olacak. 
# =============================================================================


import sqlite3
import time

class Kitap():
    def __init__(self, isim, yazar, yayinEvi,tur,baski):    #ekleyebilmek ve içine metod olustumak icin yazıldı.
        self.isim = isim
        self.yazar = yazar
        self.yayinEvi = yayinEvi
        self.tur = tur
        self.baski = baski
        
    def __str__(self):  #yazdırmak için
        return "Kitap İsmi: {}\nYazar = {}\nYayin Evi: {}\nTur: {}\nBaski: {}\n".format(self.isim, self.yazar, self.yayinEvi, self.tur, self.baski)
    
######## Kitap Class'ı bitti. #######



class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kutuphane.db")     #database dosyası oluşturuldu.
        self.cursor = self.baglanti.cursor()                #Cursor ayarlandı, cursor ile database'de dolaşılacak ve işlemler yapılacak.       
        
        sorgu  ="Create Table If Not Exists kitaplar(isim TEXT, yazar TEXT, yayinEvi TEXT, tur TEXT, baski INT)"
        self.cursor.execute(sorgu)      #Sorgu çalışacak ve tablo olusacak.
        self.baglanti.commit()
    
    def baglantiyi_kes(self):
        self.baglanti.close()
    
    def kitaplari_goster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        
        if(len(kitaplar) == 0):
            print("there is no book. \n")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])     #kitap objesini olşturduk, sıra ile tek tek yazdırdık.
                print(kitap)
    
    def kitap_sorgula(self, isim):
        sorgu = "Select * From kitaplar Where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall() ##eğer içerisinde varsa tek elemanlı demetler olusturucak.
        if(len(kitaplar) == 0):
            print("there is no book. \n")
        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4])
            print(kitap)
    
    def kitap_ekle(self, kitap):
        sorgu = "Insert into kitaplar Values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim, kitap.yazar, kitap.yayinEvi, kitap.tur, kitap.baski))
        self.baglanti.commit()
        
        
    def kitap_sil(self, isim):
        sorgu = "Delete from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    
    def baski_yukselt(self, isim):
        sorgu = "Select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("there is no book. \n")
        else:
            baski = kitaplar[0][4]  #baskı sayısını aldık, günceledik.
            baski += 1
            
            sorgu2 = "Update kitaplar set baski = ? where isim = ?"
            self.cursor.execute(sorgu2,(baski, isim))
            self.baglanti.commit()
        
        
        
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
