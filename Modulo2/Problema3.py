def promedio(alumno):
    prom = 0
    promediofinal = 0
    promedio = []
    k ={}
    for i in range(0,3):
        prom = (alumno[i]['Nota1']+alumno[i]['Nota2']+alumno[i]['Nota3'])/3
        name = alumno[i]['Nombre']
        if prom >= 4:
            k ={'Nombre':name,'promedio': prom, 'Estado': 'Aprobado'}
            promedio.append(k)
        else:
            k ={'Nombre':name,'promedio': prom, 'Estado': 'Desaprobado'}
            promedio.append(k) 
    for i in range(len(alumno)):
        promediofinal = promediofinal + promedio[i]['promedio']
    promediofinal2 = promediofinal/len(alumno)
    return promediofinal2
alumno = [{'Nombre': 'Gonzalo', 'Nota1': 14.0, 'Nota2': 12.0, 'Nota3': 15.0},
 {'Nombre': 'Juan', 'Nota1': 2.0, 'Nota2': 8.0, 'Nota3': 9.0},
 {'Nombre': 'Maria', 'Nota1': 14.0, 'Nota2': 11.0, 'Nota3': 10.0}]
problema = promedio(alumno)
print(problema)
