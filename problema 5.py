x = [11,22,33,44,55]
y=x
print('suma primelor trei componente din x =', sum(x[0:3]))
print('suma tuturor componentelor y =', sum(y))
p=1
for i in range(0,len(x)):
    p=p*x[i]
    i=i+1
print('produsul tuturor componentelor x =', p)
print('valoarea absoluta a componentei a treia din y =', abs(x[2]))
print('suma primelor componente din x si y =', x[0]+y[0])
