print('satış fiyatını giriniz')
satis_fiyati=int(input())
print('indirim oranını giriniz')
indirim_orani=int(input())
yeni_fiyat=satis_fiyati-(satis_fiyati*indirim_orani/100)
print('indirimli satış fiyatı:',yeni_fiyat)
