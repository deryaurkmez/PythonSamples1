#Asal Sayı: kendinden ve 1'den başka sayıya kalansız bölünemiyorsa sayı asaldır.
#Girilen sayının asal olupup olmadığını bulan uygulama
#sayıyı al
#Bölen sayi, girilen sayının bir küçüğü olana kadar 
#girilen sayı bölen sayıya kalansız bölmeye bakılır

print('Bir sayı giriniz')
girilen_sayi=int(input())
bolen_sayi=2
asal_mi=True

while bolen_sayi<girilen_sayi:
    if girilen_sayi % bolen_sayi == 0:
        asal_mi = False
        break
    bolen_sayi +=1
if asal_mi==True:
    print(girilen_sayi, 'asaldır.')
else:
    print(girilen_sayi,'asal değildir.')


