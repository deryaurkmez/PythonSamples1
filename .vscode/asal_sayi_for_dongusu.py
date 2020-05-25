print('bir sayı giriniz')
girilen_sayi=int(input())
asal_mi=False
for sayi in range(2 , girilen_sayi):
    if girilen_sayi % sayi==0:
        asal_mi=True
if asal_mi==True:
    print(girilen_sayi,'sayısı asal değildir.')
else:
    print(girilen_sayi, 'sayısı asaldır.')
   