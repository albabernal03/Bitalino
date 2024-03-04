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