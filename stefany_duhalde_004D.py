recorridos = {
'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True]
}

venta = {
'R001': [7990, 20],
'R002': [25990, 0],
'R003': [1990, 35],
'R004': [12990, 8],
'R005': [18990, 3],
'R006': [4990, 12]
}


def menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Asientos por ciudad de origen
2. Búsqueda de recorridos por rango de precio
3. Actualizar precio de recorrido
4. Agregar recorrido
5. Eliminar recorrido
6. Salir
=====================================""")

def leer_opcion():
    while True:
        try:
            opcion = int(input('Ingrese opción [1-2-3-4-5-6]: '))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opción válida")
            else:
                return opcion
        except:
            print('ERROR: opción debe ser un número entero.')


while True:
    menu()
