asal_mi=False
for sayi in range(1,10000):
    asal_mi=False
    for sayi2 in range(2, sayi):
        if sayi % sayi2==0:
            asal_mi=True
            break
    if asal_mi==False:
        print(sayi)


