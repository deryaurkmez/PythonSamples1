for sayi in range(1,4):
    n=2
    asal_mi=False
    while sayi<n:
        sayi % n==0
        asal_mi=True
        n +=1
        if asal_mi==False:
            print(sayi)