print('1.Vize notunuz:')
vize_1=int(input())
print('2.Vize notunuz:')
vize_2=int(input())
print('Final notunuz:')
final=int(input())
ortalama=(vize_1 * 0.25) + (vize_2 * 0.35) + (final * 0.40)
print('Ortalamanız:' , ortalama)

if ortalama>=80:
    print('NOTUNUZ: A')
elif ortalama>=70 and ortalama<80:                                                                                                                                                                             
    print('NOTUNUZ: B')
elif ortalama>=60 and ortalama<70:
    print('NOTUNUZ: C')
elif ortalama>=50 and ortalama<60:
    print('NOTUNUZ: D')
else:
    print('NOTUNUZ: F KALDINIZ')