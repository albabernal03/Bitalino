import h5py
import matplotlib.pyplot as plt

# Abrir el archivo HDF5
file_path = 'tu_archivo.h5'
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
