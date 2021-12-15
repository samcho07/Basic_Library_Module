#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:28:11 2021

@author: mertsamast
"""

# =============================================================================
# Kutuphaneyi modül olarak kullanmak 
# =============================================================================

import time
from Kutuphane_Project import *


kutuphane = Kutuphane()     #Modul olarak aldık. Diğer .py dosyasında sınıf olarak tanımlandı. Bu sınıfı alı burada kullanacağız.

print("*******************")
print("Kutuphanemize hoşgeldiniz.")
print("İşlemler\n1-> Kitaplari Göster\n2->Kitap Sorgulamak\n3->Kitap Eklemek\n4->Kitap Sil\n5->Baskı Yükselt\nÇıkış için 'q' basın")




while True:
    islem = input("Yapacağınız işlemi seçiniz = ")
    if(islem == "q"):
        print("Program kapatılıyor.")
        break
    elif islem == "1":
        kutuphane.kitaplari_goster()
        
    elif islem == "2":
        isim = input("Hangi kitabı istiyorsunuz?")
        print("Kitap sorgulanıyor")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
        
    elif islem == "3":
        kitap = input("Kitap ismi:")
        yazar = input("yazar ismi: ")
        yayin_evi = input("yayın Evi:")
        tur = input("Tür:")
        baski = int(input("Baski"))
        
        yeni_kitap = Kitap(kitap, yazar, yayin_evi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        
    elif islem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz?")
        cevap = input("Emin misiniz? (E/H)")
        if cevap == "e":
            print("kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap Silindi.")
        
            
        
    elif islem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?")
        kutuphane.baski_yukselt(isim)
        time.sleep(2)
        print("Baskı yükseltildi.")
        
    else:
        print("Geçersiz İşlem...")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        