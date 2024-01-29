#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import subprocess

def obtener_librerias_instaladas():
    """Obtiene las librerías instaladas y las devuelve como un conjunto de nombres."""
    output = subprocess.check_output(['pip', 'list']).decode('utf-8')
    librerias = set()
    for linea in output.split('\n')[5:]:  # Ignorar los encabezados
        if linea.strip():
            nombre = linea.split()[0]
            librerias.add(nombre)
    return librerias

# Obtener las librerías actualmente instaladas
librerias_actuales = obtener_librerias_instaladas()

# Leer el archivo con la lista de librerías a instalar
with open('librerias_instaladas.txt', 'r') as file:
    librerias_a_instalar = file.readlines()

for libreria in librerias_a_instalar[5:]:
    if libreria.strip() == "":
        continue
    libreria_nombre = libreria.split()[0]
    if libreria_nombre in librerias_actuales:
        print(f"{libreria_nombre} ya está instalada, se omite.")
        continue
    print(f"Intentando instalar {libreria_nombre}...")
    try:
        subprocess.check_call(['pip', 'install', libreria_nombre])
        print(f"{libreria_nombre} instalada con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar {libreria_nombre}: {e}")


# AÑADIR PRINT POR NOMBRE, EXTRA, HACER UN ARCHIVO CON LAS LIBRERIAS QUE YA SE TIENEN Y NO DESCARGAR ESAS 
