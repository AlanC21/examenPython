# Funcion donde el usuario ingresa las calificaciones
def ingresarCalificaciones():
    calificaciones = []
    while True:
        calificacion = input("Ingresa una calificación (o 'q' para salir): ")
        if calificacion.lower() == 'q':
            break
        try:
            calificaciones.append(float(calificacion))
        except ValueError:
            print("Por favor ingresa un número válido.")
    return calificaciones

# Funcion para calcular el promedio de las calificaciones
def calcularPromedio(calificaciones):
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

# Funcion para obtener la maxima calificacion
def obtenerMax(calificaciones):
    return max(calificaciones) if calificaciones else None

# Funcion para obtener la minima calificacion
def obtenerMin(calificaciones):
    return min(calificaciones) if calificaciones else None

# Funcion para mostrar la pantalla del usuario
def mostrarPantalla():
    calificaciones = ingresarCalificaciones()
    if calificaciones:
        print(f"Calificación más alta: {obtenerMax(calificaciones)}")
        print(f"Calificación más baja: {obtenerMin(calificaciones)}")
        print(f"Promedio de calificaciones: {calcularPromedio(calificaciones):.2f}")
    else:
        print("No se ingresaron calificaciones.")

# Llamamos a la funcion mostrarPantalla() para que el usuario pueda utilizarla
mostrarPantalla()
