t=[-2,4,5,6,21,13,12,22,-5,16,33,-9,19,11,25,27,34,17,20,10,1,0,29,-3]
print('a Temperatura medie este', sum(t)/24)
print('b Maximul temperaturii este', max(t)) 
print('b Minimul temperaturii este', min(t))
for i in t:
    if i==max(t):
        print('c Ora cand s-a inregistrat temperatura maxima este', t.index(i)+1)
for i in t:
    if i==min(t):
        print('c Ora cand s-a inregistrat temperatura minima este', t.index(i)+1)
n1=0
for i in t:
    if i<0:
        n1+=1
print('d Nr. de zile in care au fost inregistrate temperaturi mai jos de 0 grade este', n1)
n2=0
for i in t:
    if i>sum(t)/24:
        n2+=1
print('e Nr. de zile in care au fost inregistrate temperaturi mai mari de media saptamanala este', n2)