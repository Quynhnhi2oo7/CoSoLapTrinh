import math
print('Nhap hai canh ke cua tam giac vuong:')
ckt1=int(input())
ckt2=int(input())
x=math.sqrt((ckt1*ckt1)+(ckt2*ckt2))
print('Canh ke thu nhat la: '+ str(ckt1)+',',end=" ")
print('canh ke thu hai: '+str(ckt2)+',', end=" ")
print('co canh huyen =',x)
#print('Canh ke thu nhat la:',ckt1,' , ' 'canh ke thu hai: ', ckt2,' , ' 'co canh huyen = ',x, sep="")