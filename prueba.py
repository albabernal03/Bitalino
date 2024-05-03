import h5py
import matplotlib.pyplot as plt

# Abrir el archivo HDF5
file_path = 'Opensignals2/bitalino_Sound_video_without_light.h5'
with h5py.File(file_path, 'r') as file:
    # Leer datos, por ejemplo, EEG
    eeg_data = file['EEG'][:]
    
    # Graficar los datos de EEG
    plt.figure(figsize=(10, 4))
    plt.plot(eeg_data)
    plt.title('Datos de EEG')
    plt.xlabel('Muestra')
    plt.ylabel('Amplitud')
    plt.show()

metadata = {
    "device": "bitalino_rev",
    "device name": "84:BA:20:5E:FF:58",
    "position": 0,
    "device connection": "BTH84:BA:20:5E:FF:58",
    "sampling rate": 100,
    "resolution": [4, 1, 1, 1, 1, 10],
    "firmware version": 1282,
    "comments": "",
    "keywords": "",
    "mode": 0,
    "sync interval": 2, 
    "date": "2024-3-1", 
    "time": "18:30:27.147",
    "channels": [1],
    "sensor": ["EMGBITREV"], 
    "label": ["A1"],
    "column": ["nSeq", "I1", "I2", "O1", "O2", "A1"],
    "special": [{}],
    "digital IO": [0, 0, 1, 1],
    "convertedValues": 0
}

# Formatear los metadatos como texto
metadata_str = '\n'.join(f"# {key}: {value}" for key, value in metadata.items())

# Guardar en un archivo .txt
txt_file_path = 'egg2.txt'
with open(txt_file_path, 'w') as txt_file:
    txt_file.write(metadata_str)
