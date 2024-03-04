# Bitalino
El link a nuestro repositorio es: [GitHub](https://github.com/albabernal03/Bitalino)
En esta práctica, hemos aplicado técnicas de Inteligencia Artificial y Análisis de Datos para explorar, procesar, y analizar datos fisiológicos recopilados a través del dispositivo Bitalino. El objetivo es identificar patrones, realizar predicciones, y extraer conclusiones significativas de los datos de electrocardiograma (ECG), electromiograma (EMG), y actividad electrodermal (EDA) bajo diferentes condiciones experimentales. En este primer tramo nuestro objetivo ha sido aprender a recoger datos y visualizarlos para en un futuro aplicarlo a gran escala.

## OpenSignals
En esta carpeta están recogidos los datos vitales de diferentes tipos los cuales vamos a analizar:

- EMG (Electromiografía): La señal EMG registra la actividad eléctrica producida por los músculos. Dependiendo de la aplicación específica, podrías usar SARIMA o ARIMA para modelar y predecir la actividad muscular a lo largo del tiempo.

- ACC (Acelerometría): Los datos de acelerometría registran la aceleración en una o más direcciones. Podrías aplicar técnicas de series temporales para modelar patrones de movimiento o vibraciones a lo largo del tiempo.

- LUX (Luminosidad): Los datos de luminosidad representan la intensidad de la luz. Para este tipo de datos, puede que no tenga sentido aplicar SARIMA o ARIMA, ya que la luminosidad puede estar influenciada por factores externos como la hora del día o el clima, que no son necesariamente modelados bien por estos modelos.

- ECG (Electrocardiografía): Los datos de ECG registran la actividad eléctrica del corazón. SARIMA o ARIMA podrían usarse para modelar y predecir patrones de ritmo cardíaco a lo largo del tiempo.

- EEG (Electroencefalografía): Los datos de EEG registran la actividad eléctrica del cerebro. Al igual que con ECG, SARIMA o ARIMA podrían usarse para modelar y predecir patrones de actividad cerebral.

- EDA: Los datos registran los cambios de estado en la piel.

## img
En esta carpeta hemos guardado las gráficas de las constantes vitales analizadas.
- acc.png
- ecg.png
- eeg.png
- emg.png
- lux.png

## grafica.py
Con este codigo dibujamos las gráficas que representan los datos y exploramos la estructura del archivo .h5.
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
