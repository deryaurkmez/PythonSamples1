print('Saat Kaç?(dakika hariç)')
saat=int(input())
print('Bugün haftasonu mu?(E/H)')
cevap=input().upper()

if saat < 12 and cevap=='H':
    print('Günaydın')
elif saat >=18 and cevap=='H':
    print('iyi Akşamlar')
elif cevap=='E':
    print('Bugün kapalıyız.')
else:
    print('İyi Günler')

