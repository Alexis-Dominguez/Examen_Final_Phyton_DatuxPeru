abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
clave = ['n','q','x','p','o','m','a','f','t','r','h','l','z','g','e','c','y','j','i','u','w','s','k','d','v','b','N','Q','X','P','O','M','A','F','T','R','H','L','Z','G','E','C','Y','J','I','U','W','S','K','D','V','B']
lista =[]
x = input("Ingrese texto")
for i in range(len(x)):
    y= abc.index(x[i])
    #print(y)
    lista.append(clave[y])
final = "".join(lista)
print(final)
