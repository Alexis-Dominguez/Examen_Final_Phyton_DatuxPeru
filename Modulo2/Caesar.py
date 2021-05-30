abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista = []
lista2= []
final =[]
x = int(input("Ingrese el número de desplazamientos "))
if x>26:
    le = int(x/26)
    x = x-(26*le)
for i in range(x,len(abc)):
    #print(abc[i])
    lista.append(abc[i])
#print(lista)    
for i in range(0,x):
    lista.append(abc[i])
for i in range(x,len(mayus)):
    lista2.append(mayus[i])
#print(lista2)    
for i in range(0,x):
    lista2.append(mayus[i])
for i in range(len(mayus)):
    abc.append(mayus[i])
for i in range(len(lista2)):
    lista.append(lista2[i])
abc.append(" ")
abc.append(",")
lista.append(" ")
lista.append(",")       
#print(abc)
#print(lista)

y = input("Ingrese texto ")
for i in range(len(y)):
    z= abc.index(y[i])
    #print(z)
    final.append(lista[z])
fin = "".join(final)
print(fin)