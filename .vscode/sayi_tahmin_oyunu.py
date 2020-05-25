#sayı tutucak, bu sayıyı tahmin etmeye çalışacak. Bulunca buldun yazsın.
#algoritma;
#1. Oyun 1-100 arasında random bir sayı tutar. 
#2. kullanıcı sayıyı tahmin eder.
#3. girilen sayı tutulan sayıdan büyükse ekrana aşağı yazar.
#4. girirlen sayı tutulandan küçükse ykarı yazarak yönlendirir.
#5. sayı bulununca sayı bulundu yazar.

import random
rastgele_sayi=random.randint(1,100)
sayac=1
print(rastgele_sayi)
    
oyun_bittimi = False
while oyun_bittimi == False:
    print('Lütfen tahmin yapın.')

    girilen_sayi=int(input())
    if girilen_sayi < rastgele_sayi:
        sayac=sayac + 1
        print('YUKARI')
    elif girilen_sayi > rastgele_sayi:
        print('AŞAĞI')
        sayac=sayac + 1
    else:
        print('Sayıyı buldunuz!' + str(sayac) , 'bildiniz')
        print(sayac, 'kerede buldunuz.')
        oyun_bittimi = True