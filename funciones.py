#Arturo Benicio Perotto - 113
import json
import os
import random

def get_path_actual(nombre_archivo):
    """
    Obtiene la ruta completa de un archivo dado su nombre.

    Args:
        nombre_archivo (str): El nombre del archivo.

    Returns:
        str: La ruta completa del archivo.
    """
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def leer_csv(archivo_entrada):
    """
    Lee un archivo csv y devuelve una lista de diccionarios.

    Args:
        archivo_entrada: El nombre del archivo csv de entrad.

    Returns:
        list: Una lista de diccionarios con los datos del archivo csv.
    """
    with open(get_path_actual(archivo_entrada), 'r', encoding='utf-8') as archivo:
        lista = []
        encabezado = archivo.readline().strip('\n').split(',')

        for linea in archivo.readlines():
            bici = {}
            linea = linea.strip('\n').split(',')
            id_bike, nombre, tipo, tiempo = linea

            bici['id_bike'] = int(id_bike)
            bici['nombre'] = nombre
            bici['tipo'] = tipo
            bici['tiempo'] = int(tiempo)  # Convertir tiempo a entero
            lista.append(bici)
    
    return lista  # Retornar la lista de bicicletas

def guardar_posiciones_en_json(archivo, nombre_archivo_salida):
    """
    Guarda el listado de bicicletas ordenadas por tipo y tiempo en un archivo jsonn

    Args:
        archivo: Lista de diccionarios representando las bicicletas ordenadas.
        nombre_archivo_salida (str): Nombre del archivo json de salida.
    """
    if not archivo:
        print("No hay bicicletas para guardar.")
        return

    with open(get_path_actual(nombre_archivo_salida), "w", encoding="utf-8") as file:
        json.dump(archivo, file, indent=4)

def escribir_csv(lista, archivo_salida):
    if not lista:
        print("La lista está vacía, no se puede escribir en el archivo.")
        return
    with open(get_path_actual(archivo_salida), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for bici in lista:
            values = [str(value) for value in bici.values()]
            linea = ",".join(values) + "\n"
            archivo.write(linea)

def asignar_tiempo_aleatorio_bicicletas(lista_bicicletas):
    """
    Asigna un tiempo aleatorio entre 50 y 120 minutos a cada bicicleta en la lista dada.

    Args:
        lista_bicicletas (list): Una lista de diccionarios representando cada bicicleta.

    Returns:
        list: La lista de bicicletas con los tiempos asignados.
    """
    for bicicleta in lista_bicicletas:
        bicicleta["tiempo"] = random.randint(50, 120)
    return lista_bicicletas

def imprimir_lista_bicicletas(lista_bicicletas):
    """
    Imprime la lista de bicicletas con los tiempos asignados.

    Args:
        lista_bicicletas (list): Una lista de diccionarios representando cada bicileta.
    """
    for bicicleta in lista_bicicletas:
        print("id_bike:", bicicleta["id_bike"])
        print("nombre:", bicicleta["nombre"])
        print("tipo:", bicicleta["tipo"])
        print("tiempo:", bicicleta["tiempo"])
        print("-----------------------------")

def informar_ganador(bicicletas):
    """
    Informa el nombre del dueño de la bicicleta que llegó primero y el tiempo que tardó.
    Si hubiera empate, informa todos los nombres de las bicicletas que empataron.

    Parámetros:
    bicicletas (list): Una lista de diccionarios donde cada diccionario representa una bicicleta.

    Retorna:
    tuple: Una lista con los nombres de los ganadores y el tiempo mínimo.
    """
    if not bicicletas:
        print("No hay bicicletas en la lista.")
        return [], 0

    min_tiempo = bicicletas[0]['tiempo']
    ganadores = [bicicletas[0]['nombre']]
    for bicicleta in bicicletas[1:]:
        if bicicleta['tiempo'] < min_tiempo:
            min_tiempo = bicicleta['tiempo']
            ganadores = [bicicleta['nombre']]
        elif bicicleta['tiempo'] == min_tiempo:
            ganadores.append(bicicleta['nombre'])
    
    return ganadores, min_tiempo

def filtrar_lista(funcion, lista:list)->list:
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

def filtrar_por_tipo(bicicleta, tipo):
    """
    Verifica si el tipo de bicicleta coincide con el tipo dado.

    Args:
        bicicleta (dict): Diccionario.
        tipo (str): El tipo de bicicleta a comparar.

    Returns:
        bool: True si el tipo de bicicleta coincide, False en caso contrario.
    """
    return bicicleta["tipo"].lower() == tipo.lower()

def menu_filtrar_por_tipo(bicicletas):
    tipo_bicicleta = input("Ingrese el tipo de bicicleta a filtrar (BMX, PLAYERA, MTB, PASEO): ").upper()
    bicicletas_filtradas = filtrar_lista(lambda bici: filtrar_por_tipo(bici, tipo_bicicleta), bicicletas)
    nombre_archivo_salida = tipo_bicicleta.lower() + ".csv"
    escribir_csv(bicicletas_filtradas, nombre_archivo_salida)
    print(f"Se ha creado el archivo '{nombre_archivo_salida}' con las bicicletas de tipo '{tipo_bicicleta}'.")

def informar_promedio_por_tipo(bicicletas):
    """
    Calcula y muestra el promedio de tiempo por cada tipo de bicicleta.

    Args:
        bicicletas (list): Una lista de diccionarios donde cada diccionario representa una bicicleta.
    """
    promedio_por_tipo = {}
    contador_por_tipo = {}

    for bicicleta in bicicletas:
        tipo = bicicleta["tipo"]
        tiempo = bicicleta["tiempo"]
        if tipo not in promedio_por_tipo:
            promedio_por_tipo[tipo] = tiempo
            contador_por_tipo[tipo] = 1
        else:
            promedio_por_tipo[tipo] += tiempo
            contador_por_tipo[tipo] += 1

    for tipo, total_tiempo in promedio_por_tipo.items():
        cantidad_bicicletas = contador_por_tipo[tipo]
        promedio_por_tipo[tipo] = total_tiempo / cantidad_bicicletas
    print("\nPromedio de tiempo por tipo de bicicleta:")
    for tipo, promedio in promedio_por_tipo.items():
        print(f"{tipo}: {promedio:.2f} minutos")

def ordenar_bicicletas_por_tipo_y_tiempo(bicicletas):
    bicicletas_ordenadas = []

    tipos_unicos = []
    for bici in bicicletas:
        tipo = bici['tipo']
        if tipo not in tipos_unicos:
            tipos_unicos.append(tipo)

    for tipo in tipos_unicos:
        for bici in bicicletas:
            if bici['tipo'] == tipo:
                bicicletas_ordenadas.append(bici)

    return bicicletas_ordenadas

def ordenar_bicicletas(bicicletas):
    bicicletas_por_tipo = {}

    for bici in bicicletas:
        tipo = bici['tipo']
        if tipo not in bicicletas_por_tipo:
            bicicletas_por_tipo[tipo] = []
        bicicletas_por_tipo[tipo].append(bici)
    for tipo in bicicletas_por_tipo:
        bicicletas_por_tipo[tipo].sort(key=lambda x: x['tiempo'])

    return bicicletas_por_tipo

def guardar_posiciones_en_json(bicicletas_por_tipo, archivo_salida):
    """
    Guarda las bicicletas ordenadas por tipo y tiempo en un archivo JSON.

    Args:
        bicicletas_por_tipo (dict): Diccionario con las bicicletas ordenadas por tipo.
        archivo_salida (str): Nombre del archivo JSON de salida.
    """
    with open(get_path_actual(archivo_salida), "w", encoding="utf-8") as archivo:
        json.dump(bicicletas_por_tipo, archivo, indent=4)

def mostrar_posiciones(archivo):
    """
    Muestra por pantalla un listado de bicicletas ordenadas por tipo y tiempo.
    """
    if not archivo:
        print("No hay bicicletas para mostrar.")
        return

    archivo_ordenado = ordenar_bicicletas_por_tipo_y_tiempo(archivo)

    print("Posiciones de las bicicletas:")
    for bici in archivo_ordenado:
        print(f"id_bike: {bici['id_bike']}, nombre: {bici['nombre']}, tipo: {bici['tipo']}, tiempo: {bici['tiempo']} minutos")

#-------------------- MENU ------------------
def pause():
    os.system("pause")

def clean_screen():
    os.system("cls") 

def menu_principal():
    bicicletas = []
    archivo = None

    while True:
        clean_screen()
        print("\nMenú Principal | BiciFast")
        print("[1] Cargar Archivo")
        print("[2] Imprimir archivo")
        print("[3] Agregar tiempo")
        print("[4] Informar ganador")
        print("[5] Filtrar por tipo")
        print("[6] Informar promedio por tipo")
        print("[7] Mostrar posiciones")
        print("[8] Guardar posiciones")
        print("[9] Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_archivo = str(input("Introduzca el nombre de un archivo: "))
            archivo = leer_csv(nombre_archivo)
        elif opcion == "2":
            if archivo:
                imprimir_lista_bicicletas(archivo)
            else:
                print("Primero debe cargar el archivo.")
        elif opcion == '3':
            if archivo:
                archivo = asignar_tiempo_aleatorio_bicicletas(archivo)
                print("Tiempos asignados aleatoriamente.")
            else:
                print("Primero debe cargar el archivo.")
        elif opcion == '4':
            if archivo:
                ganadores, tiempo = informar_ganador(archivo)
                if ganadores:
                    if len(ganadores) == 1:
                        print(f"El ganador es: {ganadores[0]}, con un tiempo de {tiempo} minutos.")
                    else:
                        print("Hubo un empate entre los siguientes participantes:")
                        for ganador in ganadores:
                            print(f"- {ganador}")
                        print(f"Todos con un tiempo de {tiempo} minutos.")
                else:
                    print("No hay ganadores, la lista de bicicletas está vacía.")
            else:
                print("Primero debe cargar el archivo.")
        elif opcion == '5':
            menu_filtrar_por_tipo(bicicletas)
        elif opcion == '6':
            informar_promedio_por_tipo(archivo)
        elif opcion == '7':
            mostrar_posiciones(archivo)
        elif opcion == '8':
            bicicletas_por_tipo = ordenar_bicicletas(bicicletas)
            guardar_posiciones_en_json(bicicletas_por_tipo, "bicicletas_ordenadas.json")
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        pause()

menu_principal()

