def busca_alumno(alumno):
    prom = 0
    promediofinal = 0
    promedio = []
    comparar = []
    k ={}
    x=input("Ingrese el nombre del alumno a buscar")
    for i in range(len(alumno)):
        if alumno[i]['Nombre'] == x:
            print(alumno[i])
    
    
alumno = [{'Nombre': 'Gonzalo', 'Nota1': 14.0, 'Nota2': 12.0, 'Nota3': 15.0,'promedio':13.666},
 {'Nombre': 'Juan', 'Nota1': 2.0, 'Nota2': 8.0, 'Nota3': 9.0,'promedio':6.333},
 {'Nombre': 'Maria', 'Nota1': 14.0, 'Nota2': 11.0, 'Nota3': 10.0,'promedio':11.666}]
problema = busca_alumno(alumno)
