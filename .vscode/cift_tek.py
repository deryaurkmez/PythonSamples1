#1. ekrana sayı girin yazar
#2. girilen sayı, int tipine çevirilmeli ve bir değişkene atanmalı.
#3. Bu değişken, 2'ye tam bölünüyorsa çift, bölünmüyorsa tektir.

print('Sayı giriniz:')
girilen_sayi=int(input())

if girilen_sayi % 2==0:
    print('sayı çifttir')
else:
    print('sayı tektir')