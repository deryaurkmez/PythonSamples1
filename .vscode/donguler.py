#Başlangıç
#Bitiş Koşulu
#Kullanılacak Yapı
#Örnek: Amaç= 1 den 10 a kadar olan sayıları ekrana yazdır.
# 1. Bir değişkenim olsun, 1 den başlasın
#2. Bu değişken 10 dan küçük olduğu sürece ekrana yazılsın. 
#3. Değişkenin değeri 1 artsın.

sayac=1
while sayac<=10:
    print(sayac)
    sayac +=1        #sayac=sayac+1
print('Döngü bitti.')

#Sonsuz Döngü
#sayac2=1
#while sayac2<20:
    #print('sayac2')

#klavyeden girilen sayının kaç basamaklı olduğunu gösteren uygulama
# Bir sayıyı 0 dan büyük olduğu sürece 10'a bölerseniz, bölüm sayısı basamak sayısına eşittir.

print('Bir sayı girin:')
girilen_sayi=int(input())
bolme_sayisi=0
while girilen_sayi>0:
    girilen_sayi //= 10
    bolme_sayisi+=1
print('Girdiğiniz Sayı',bolme_sayisi, 'Basamaklıdır')



