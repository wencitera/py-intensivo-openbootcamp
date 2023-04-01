import os, sys

def main():
    #listar_ficheros('C:\\Users\\wenci\\Downloads')
    listar_directorios_y_ficheros('C:\\Users\\wenci')

""" def listar_ficheros(path):
    files = os.listdir(path)
    
    for file in files:
        full_path = os.path.join(path, file) 
        if(os.path.isfile(full_path)):
            file_weight = convertir_tamano(os.stat(full_path).st_size)
            print(f'{file} PESO: {file_weight}') """


def mostrar_fichero(full_path):
    path, archivo = os.path.split(full_path)
    file_weight = convertir_tamano(os.stat(path).st_size)
    print(f'    L__ {archivo} :: {file_weight}')

def listar_directorios_y_ficheros(path_inicial):
    try:
        dirs = os.listdir(path_inicial)
    except:
        print(f"No se puede acceder al directorio {path_inicial}")
        return
    
    for dir in dirs:
        full_path = os.path.join(path_inicial, dir)
        if(os.path.isdir(full_path)):
            print(path_inicial)
            listar_directorios_y_ficheros(full_path)
        else:
            mostrar_fichero(full_path)


def convertir_tamano(bytes):
    unidades = ['B', 'KB', 'MB', 'GB', 'TB']
    size = bytes
    unidad_idx = 0
    while size >= 1024 and unidad_idx < len(unidades) - 1:
        size /= 1024
        unidad_idx += 1
    if size > 1:
        return f"{size:.2f} {unidades[unidad_idx]}"
    else:
        return f"{bytes} bytes"

if __name__ == '__main__':
    main()