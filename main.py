from grafica import explorar_estructura_h5, trazar_datos_especificos_h5

def main():
    # Lista ruta de archivos .h5 y rutas de los datos a graficar
    datos = [['OpenSignals/ECG/ECG_imagen2.h5', '84:BA:20:5E:FF:58/raw/channel_2']
            ]

    # Iterar sobre los datos y graficarlos
    for dato in datos:
        ruta_archivo = dato[0] # Ruta del archivo .h5
        ruta_datos = dato[1] # Ruta de los datos a graficar

        # Explorar la estructura del archivo .h5
        explorar_estructura_h5(ruta_archivo)

        # Graficar un conjunto de datos específico
        trazar_datos_especificos_h5(ruta_archivo, ruta_datos)