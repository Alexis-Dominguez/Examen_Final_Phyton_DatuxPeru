n = int(input('Introduce un número entero entre 1 y 10: '))
nombre = 'tabla-' + str(n) + '.txt'
f = open(nombre, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()