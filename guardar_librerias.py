#!/usr/bin/env python
# coding: utf-8

# In[4]:


import subprocess

# Obtener la lista de librerías instaladas
output = subprocess.check_output(['pip', 'list']).decode('utf-8')

# Guardar la lista en un archivo de texto
with open('librerias_instaladas.txt', 'w') as file:
    file.write(output)

