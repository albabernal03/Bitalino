# Bitalino

El link a nuestro repositorio es: [GitHub](https://github.com/albabernal03/Bitalino)

En esta práctica, hemos aplicado técnicas de Inteligencia Artificial y Análisis de Datos para explorar, procesar, y analizar datos fisiológicos recopilados a través del dispositivo Bitalino. El objetivo es identificar patrones, realizar predicciones, y extraer conclusiones significativas de los datos de electrocardiograma (ECG), electromiograma (EMG), y actividad electrodermal (EDA) bajo diferentes condiciones experimentales. En este primer tramo nuestro objetivo ha sido aprender a recoger datos y visualizarlos para en un futuro aplicarlo a gran escala.

## Documento de autorización BITalino

La gestión ética de datos biomédicos, dada su naturaleza sensible, requiere medidas rigurosas para proteger la privacidad y asegurar el consentimiento informado. Por ello, elaboramos un documento de autorización, reflejando nuestro compromiso con la ética y la transparencia. Este documento garantiza que los participantes estén bien informados sobre la investigación, sus riesgos y beneficios, y cómo se protegerán sus datos. Además, subraya la importancia de su consentimiento voluntario y la protección de sus derechos, alineándose con las normativas éticas y legales. En esencia, este documento es esencial para asegurar un manejo responsable de los datos biomédicos y fortalecer la confianza entre investigadores y participantes.

## requirements.txt

Para descargar las dependencias usadas en este proyecto, ejecutar en la terminal el siguiente comando:
```
pip install -r requirements.txt
```

## OpenSignals

En esta carpeta están recogidos los datos vitales de diferentes tipos los cuales vamos a analizar:

- EMG (Electromiografía): La señal EMG registra la actividad eléctrica producida por los músculos.
  
- ACC (Acelerometría): Los datos de acelerometría registran la aceleración en una o más direcciones. 

- LUX (Luminosidad): Los datos de luminosidad representan la intensidad de la luz.

- ECG (Electrocardiografía): Los datos de ECG registran la actividad eléctrica del corazón. 

- EEG (Electroencefalografía): Los datos de EEG registran la actividad eléctrica del cerebro. 

- EDA (Actividad Electrodermal): Los datos registran los cambios de estado en la piel. No recogimos datos de esta sección ya que en el estado en el que estaba la persona no había ningún cambio.

## img

En esta carpeta hemos guardado las gráficas de las constantes vitales analizadas.
- acc.png
  ![image](https://github.com/albabernal03/Bitalino/assets/91721875/035e344d-e8f5-43a4-8e30-205deb509e5e)

- ecg.png
  ![image](https://github.com/albabernal03/Bitalino/assets/91721875/bbafeb35-5f39-462f-bcc7-e8778eae6e4f)

- eeg.png
  ![image](https://github.com/albabernal03/Bitalino/assets/91721875/743200dd-7ed2-4b8d-bcde-f09524c6adfb)

- emg.png
  ![image](https://github.com/albabernal03/Bitalino/assets/91721875/c3a3d247-5b81-4d6e-b767-d6d97eb7c17c)

- lux.png
  ![image](https://github.com/albabernal03/Bitalino/assets/91721875/107068dd-6923-481c-a5b5-5057c37474f3)


## grafica.py

Los archivos `.h5` son capaces de almacenar datos de forma estructurada y compleja, lo que incluye múltiples grupos y subgrupos. Esta organización detallada permite una gestión precisa de los datos, pero también requiere comprender la estructura del archivo para acceder a los datos de manera correcta. Antes de realizar análisis o visualizaciones, es fundamental explorar la estructura de los archivos de datos para comprender cómo están organizados. Esto facilita la selección adecuada de los conjuntos de datos a analizar y garantiza una interpretación precisa de los resultados. La visualización de datos es una herramienta poderosa para el análisis preliminar, ya que permite identificar patrones, tendencias, anomalías y comportamientos específicos de las señales capturadas.

Con el siguiente código dibujamos las gráficas que representan los datos y exploramos la estructura del archivo `.h5`.

```
import h5py
import matplotlib.pyplot as plt

# Función para explorar la estructura de un archivo .h5
def explorar_estructura_h5(ruta_archivo):
    with h5py.File(ruta_archivo, 'r') as f:
        # Explorar la estructura del archivo imprimiendo las claves y subclaves
        def print_keys(name, obj):
            print(name)
            if isinstance(obj, h5py.Dataset):
                print(f"Forma del conjunto de datos: {obj.shape}")
            elif isinstance(obj, h5py.Group):
                print(f"Grupo")

        f.visititems(print_keys)

# Función para graficar un conjunto de datos específico de un archivo .h5
def trazar_datos_especificos_h5(ruta_archivo, ruta_datos):
    with h5py.File(ruta_archivo, 'r') as f:
        data = f[ruta_datos][()]
        
        # Graficar los datos
        plt.figure(figsize=(10, 4))
        plt.plot(data)
        plt.title(f"{ruta_datos} from {ruta_archivo.split('/')[-1]}")
        plt.xlabel('Muestra')
        plt.ylabel('Valor')
        plt.savefig(f"img/{ruta_archivo.split('/')[-1].split('.')[0]}.png")
```

## main.py

```
from grafica import explorar_estructura_h5, trazar_datos_especificos_h5

def main():
    # Lista ruta de archivos .h5 y rutas de los datos a graficar
    datos = [['OpenSignals/EMG/emg.h5', '84:BA:20:5E:FF:58/raw/channel_1'],
            ['OpenSignals/ECG/ecg.h5', '84:BA:20:5E:FF:58/raw/channel_2'],
            ['OpenSignals/EEG/eeg.h5', '84:BA:20:5E:FF:58/raw/channel_4'],
            ['OpenSignals/ACC/acc.h5', '84:BA:20:5E:FF:58/raw/channel_5'],
            ['OpenSignals/LUX/lux.h5', '84:BA:20:5E:FF:58/raw/channel_6']]

    # Iterar sobre los datos y graficarlos
    for dato in datos:
        ruta_archivo = dato[0] # Ruta del archivo .h5
        ruta_datos = dato[1] # Ruta de los datos a graficar

        # Explorar la estructura del archivo .h5
        explorar_estructura_h5(ruta_archivo)

        # Graficar un conjunto de datos específico
        trazar_datos_especificos_h5(ruta_archivo, ruta_datos)
```

## run.py

```
from main import main

if __name__ == "__main__":
    main()
```
