n = int(input('Introduce un número entero entre 1 y 10: '))
nombre = 'tabla-' + str(n) + '.txt'
try: 
    f = open(nombre, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())