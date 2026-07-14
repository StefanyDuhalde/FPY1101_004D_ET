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
    
# --> VERIFICAR SI EN LA PARTE DE ERROR DEBO ESCRIBIR LO MISMP Q EN EL PRITN
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

def validador_string(mensaje):
    "Sirve para validar origen y destino. Devuelve string en minúscula"
    while True:
        valor = input(mensaje).strip().lower()
        if len(valor) == 0:
            print('Valor no puede estar vacío ni contener solo espacios en blanco')
        else:
            return valor

def validador_entero_positivo(mensaje):
    'Sirve para validar distancia_km o precio. Devuelve valor entero positivo.'
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print('Valor debe ser mayor que cero.')  
            else:
                return valor
        except:
            print('ERROR:VALOR DEBE SER UN NÚMERO ENTERO.')      

# OPCION 1: --> dicc en argumento

def asientos_origen(origen, dicc_recorrido):
    asientos_disponibles = 0
    for codigo, detalles_recorrido in dicc_recorrido.items():
        if detalles_recorrido[0].capitalize() == ciudad_origen:
            asientos_disponibles += venta[codigo][1]
    print(f'El total de asientos disponible es: {asientos_disponibles}')

# OPCION 2: --> poner dicc en argumento

def busqueda_precio(p_min, p_max, dicc_recorrido):
    lista_por_rango_de_precio = []
    for codigo, detalles_venta in venta.items():
        if (p_min <= detalles_venta[0] <= p_max) and (detalles_venta[1] != 0):
            origen = dicc_recorrido[codigo][0]
            destino = dicc_recorrido[codigo][1]
            lista_por_rango_de_precio.append(f'{origen}-{destino}--{codigo}')
    
    if len(lista_por_rango_de_precio) == 0:
        print("No hay recorridos en ese rango de precios.")
    else:
        print(sorted(lista_por_rango_de_precio))

# OPCIÓN 3:

def actualizar_precio(codigo, nuevo_precio):
    "Devuelve True si se pudo actulizar precio, False si no existe el código"
    if codigo in venta:
        venta[codigo][0] = nuevo_precio
        return True
    else:
        return False
    
#OPCION 4:
def validador_codigo(codigo):
    "True si código no está vacío o solo con espacios en blanco, False si no cumple con validación."
    return len(codigo.strip()) > 0

def validador_origen(origen):
    "True si origen no está vacío o solo con espacios en blanco, False si no cumple con validación."
    return len(origen.strip()) > 0

def validador_destino(destino):
    "True si destino no está vacío o solo con espacios en blanco, False si no cumple con validación."
    return len(destino.strip()) > 0

def validador_distancia_km(distancia_km):
    "True si distancia es entero mayor que 0, False si no cunmple alguna de las condiciones"
    try:
        valor = int(distancia_km)
        return valor > 0
    except:
        return False

def validador_tipo_bus(tipo_bus):
    "True si tipo de bus es 'normal', 'semi-cama' o 'cama', False si no cumple con validación."
    return tipo_bus == 'normal' or tipo_bus == 'semi-cama' or tipo_bus == 'cama'

def validador_servicio(servicio):
    "True si servicio es 'dia' o 'noche', False si no cumple con validación."
    return servicio == 'dia' or servicio == 'noche' 

def validador_tiene_wifi(tiene_wifi:str) -> True | False :
    'True si es "s" o "n"'
    if tiene_wifi == 's' or tiene_wifi == 'n':
        return True
    else:
        return False 
    
def validador_precio(precio):
    "True si precio es entero mayor que 0, False si no cunmple alguna de las condiciones"
    try:
        valor = int(precio)
        return valor > 0
    except:
        return False

def validador_asientos(asientos):
    "True si asientos es entero mayor o igual que 0, False si no cunmple alguna de las condiciones"
    try:
        valor = int(asientos)
        return valor >= 0
    except:
        return False
#--> agregar dicc recorrido
def agregar_recorrido(codigo, origen, destino, distancia, tipo_bus, servicio, tiene_wifi, precio, asientos, dicc_recorridos):
    "False si el código ya se encontraba registrado, True si se logra agregar"
    if codigo in dicc_recorridos or codigo in venta:
        return False
    
    if tiene_wifi == 'n':
        tiene_wifi = False
    elif tiene_wifi == 's':
        tiene_wifi = True
    
    dicc_recorridos[codigo] = [origen, destino, distancia, tipo_bus, servicio, tiene_wifi]
    venta[codigo] = [precio, asientos]
    return True
    
#OPCION 5: --> poner diccionario reco

def eliminar_codigo(codigo, dicc_recorridos):
    "True si elimina el código de los diccionarios, False si el código no existe."
    if codigo in dicc_recorridos:
        del dicc_recorridos[codigo]
        if codigo in venta:
            del venta[codigo]
        return True
    return False
    
while True:
    menu()
    opcion = leer_opcion()

    if opcion == 1:
        ciudad_origen = validador_string('Ingrese ciudad de origen: ').capitalize()
        asientos_origen(ciudad_origen, recorridos)
    
    #VERIFICAR LA VALIDACIÓN DE LOS PRECIOS MIN/MAXIMO
    elif opcion == 2:
        """    while True:
            try:
                precio_minimo = int(input('Ingrese precio mínimo: '))
                if precio_minimo < 0 :
                    print('Precio mínimo debe ser mayor o igual a 0.')
                else:
                    break
            except:
                print('Debe ingresar valores enteros.')
        while True:
            try:
                precio_maximo = int(input('Ingrese precio maximo: '))
                if precio_maximo < 0 :
                    print('Precio maximo debe ser mayor o igual a 0.')
                elif precio_maximo < precio_minimo:
                    print('Precio máximo debe ser mayor o igual a precio mínimo.')
                else:
                    break
            except:
                print('Debe ingresar valores enteros.')"""

        while True:
            try:
                precio_minimo = int(input('Ingrese precio mínimo: '))
                precio_maximo = int(input('Ingrese precio maximo: '))
                if precio_minimo < 0 :
                    print('Precio mínimo debe ser mayor o igual a 0.')
                    continue
                if precio_maximo < 0 :
                    print('Precio maximo debe ser mayor o igual a 0.')
                    continue
                if precio_maximo < precio_minimo:
                    print('Precio máximo debe ser mayor o igual a precio mínimo.')
                else:
                    break
            except:
                print('Debe ingresar valores enteros.')
                
                
        
        busqueda_precio(precio_minimo, precio_maximo, recorridos)
    
    elif opcion == 3:
        while True:
            codigo_a_modificar = validador_string('Ingrese Código a modificar: ').upper()
            precio_nuevo = validador_entero_positivo('Ingrese nuevo precio: ')

            if actualizar_precio(codigo_a_modificar, precio_nuevo) == False:
                print('El código no existe')
            else:
                print('Precio actualizado')

            while True:
                respuesta = validador_string('¿Desea actualizar otro precio (s/n)?: ')
                if respuesta == 'n' or respuesta == 's':
                    break
                elif respuesta != 's' and respuesta != 'n':
                    print('Respuesta debe ser "n", "N", "s" o "S".')
            if respuesta == 'n':
                break    
            

    elif opcion == 4:
        while True:
            codigo = input('Ingrese código: ').strip().upper()
            if validador_codigo(codigo) == False:
                print('Código inválido: no debe estar vacío ni contener solo espacios en blanco.')
            else:
                break
        
        while True:
            origen = input('Ingrese origen: ').strip().capitalize()
            if validador_origen(origen) == False:
                print('Origen inválido: no debe estar vacío ni contener solo espacios en blanco.')
            else:
                break

        while True:
            destino = input('Ingrese destino: ').strip().capitalize()
            if validador_destino(destino) == False:
                print('Destino inválido: no debe estar vacío ni contener solo espacios en blanco.')
            else:
                break
        
        while True:
            distancia_km = input('Ingrese distancia en km: ').strip()
            if validador_distancia_km(distancia_km) == False:
                print('Distancia inválida: Debe ser un entero mayor que 0.')
            else:
                distancia_km = int(distancia_km)
                break
        
        while True:
            tipo_bus = input('Ingrese tipo de bus [normal, semi-cama o cama]: ').lower().strip()
            if validador_tipo_bus(tipo_bus) == False:
                print('Tipo de bus inválido: tipo de bus debe ser: normal, semi-cama o cama.')
            else:
                break
        
        while True:
            servicio = input('Ingrese servicio [dia o noche]: ').lower().strip()
            if validador_servicio(servicio) == False:
                print('Servicio inválido: servicio debe ser: dia o noche, sin tildes.')
            else:
                break

        while True:
                tiene_wifi = input('Ingrese si tiene wifi (s/n): ').lower().strip()
                if validador_tiene_wifi(tiene_wifi) == False:
                    print('ERROR: Respuesta debe ser s, S, n o N.')
                elif validador_tiene_wifi(tiene_wifi) == True:
                    break
        
        while True:
            precio = input('Ingrese precio en pesos: ').strip()
            if validador_precio(precio) == False:
                print('Precio inválido: Debe ser un entero mayor que 0.')
            else:
                precio = int(precio)
                break
        
        while True:
            asientos = input('Ingrese asientos disponibles: ').strip()
            if validador_asientos(asientos) == False:
                print('Asientos disponibles inválido: Debe ser un entero mayor o igual que 0.')
            else:
                asientos = int(asientos)
                break
        
        if agregar_recorrido(codigo, origen, destino, distancia_km, tipo_bus, servicio, tiene_wifi, precio, asientos, recorridos) == False:
            print('El código ya existe')
        else:
            print('Recorrido agregado')

    elif opcion == 5:
        codigo_a_eliminar = validador_string('Ingrese Código a modificar: ').upper()
        if eliminar_codigo(codigo_a_eliminar, recorridos) == False:
            print('El código no existe')
        else:
            print("Recorrido eliminado")
    elif opcion == 6:
        print('Programa finalizado.')
        break
