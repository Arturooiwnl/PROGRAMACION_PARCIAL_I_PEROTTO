# Arturo Benicio Perotto - 113

from funciones import *

if __name__ == "__main__":
    datos = leer_csv("bicicletas.csv")

    imprimir_lista_bicicletas(datos)

    datos_con_tiempos = asignar_tiempo_aleatorio_bicicletas(datos)

    imprimir_lista_bicicletas(datos_con_tiempos)