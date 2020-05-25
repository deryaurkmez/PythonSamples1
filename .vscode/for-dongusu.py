isim='İstanbul'
for harf in isim:
    print(harf)

for sayi in range(1,11):
    print(sayi)

for sayi in range(0,11,2):
    print(sayi)

# Çarpım tablosu 2 * 1   2*2    2*3    ..... 2*9  3*1  3*2   3*3
# iç içe döngü
#

for a in  range(1,10):
    for b in range(1,10):
       carpim=a * b
       print(a, 'x' , b, '=',carpim)

       
