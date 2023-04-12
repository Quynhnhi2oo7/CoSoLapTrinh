a=int(input('Tieu thu='))
gia1=550
gia2=750
gia3=950
gia4=1350
if 1<=a<=100:
    b=a*gia1
elif 101<=a<=150:
    b=100*gia1+(a-100)*gia2
elif 151<=a<=200:
    b=100*gia1+50*gia2+(a-150)*gia3
elif a>=201:
    b=100*gia1+50*gia2+50*gia3+(a-200)*gia4
VAT=10/100
TT=b+b*VAT 
print('Phai tra=',TT)