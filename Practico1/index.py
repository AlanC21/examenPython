# Lista de Alumnos de 7'4
alumnos = ['Cordoba', 'Cataldo', 'Alsina', 'Di Gialleonardo', 'Stuffano', 'Oromendia', 'Almiron', 'Barbe']

# Notas de los Alumnos de 7'4
notas = {
  'Cordoba': [10, 7, 4, 8, 7, 10],
  'Cataldo': [9, 6, 6, 7, 8, 10],
  'Alsina': [8, 4, 7, 7, 2, 8],
  'Di Gialleonardo': [7, 4, 4, 9, 8, 7],
  'Stuffano': [6, 2, 4, 10, 10, 7],
  'Oromendia': [2, 2, 2, 4, 4, 4],
  'Almiron': [7, 4, 7, 2, 2, 1],
  'Barbe': [10, 10, 10, 10, 9, 10],
}


# Funcion para calcular el promedio de los alumnos
def calcularPromedioNotas(notas):
  return sum(notas) / len(notas)

# Funcion para mostrar el promedio de los alumnos
def mostrarPromedioNotas(notasAlumnos):
  for alumno, notas in notasAlumnos.items():
    promedioNota = calcularPromedioNotas(notas)
    print(f'El alumno: {alumno}, tuvo un promedio de notas de: {promedioNota}')

# Llamamos a la funcion para mostrar los promedios
mostrarPromedioNotas(notas)