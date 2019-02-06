#!/usr/bin/env python
# coding: utf-8

# <h1> Proyecto de Porgramación de Algoritmos</h1>
# 
# 
# <img src="https://www.utpl.edu.ec/manual_imagen/images/institucional/UTPL-INSTITUCIONAL-color.jpg" />
# 
# 
# <h2>Nombre:</h2> Edison Renato Gaibor Conde <br>
# <h2>Objetivo:</h2> Elaborar graficas por medio de un archivo csv mediante el uso de la libreria de Bokeh.
# <h3> Aplicacion Web </h3>
# Jupyter
# <h3>Bibliotecas utilizadas</h3>
# Pandas
# <h3> Librerias de Graficas </h3>
# Bokeh
# <h3>Archivos CSV</h3>
# 1. instituciones_educativas_loja.csv <br>
# 2. indicadores_estudiantiles.csv <br>
# <br>
# <h3>1.Jupyter</h3>
# 
# El cuaderno Jupyter es una aplicación web de código abierto que le permite crear y compartir documentos que contienen código en vivo, ecuaciones, visualizaciones y texto narrativo. <br>
# Los usos incluyen: limpieza y transformación de datos, simulación numérica, modelado estadístico, visualización de datos, aprendizaje automático y mucho más.
# 
# <h3>2.Pandas</h3>
# 
# Pandas es una biblioteca de código abierto con licencia BSD que proporciona estructuras de datos de alto rendimiento y fáciles de usar y herramientas de análisis de datos para el lenguaje de programación Python.
# 
# <h3>3.Bokeh</h3>
# 
# Bokeh es una biblioteca de visualización interactiva que se dirige a los navegadores web modernos para la presentación. Su objetivo es proporcionar una construcción elegante y concisa de gráficos versátiles, y extender esta capacidad con interactividad de alto rendimiento en conjuntos de datos muy grandes o de transmisión por secuencias. Bokeh puede ayudar a cualquier persona que quiera crear parcelas interactivas, paneles y aplicaciones de datos de forma rápida y sencilla.
# 
# <h3>Codigo:</h3>
# 
# 
# 
# 
# 

# In[26]:


import pandas as a
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook
from bokeh.io import show
from math import pi

output_notebook()


# In[2]:


leer_archivo = a.read_csv('indicadores_estudiantiles.csv', engine = 'python', header = 0, sep = ';', decimal = ".")


# In[3]:


leer_archivo


# In[4]:


leer_archivo.iloc[0:4 , 0:3 ]


# In[5]:


datos = ColumnDataSource(leer_archivo)


# In[6]:


datos


# In[7]:


datos.column_names


# In[8]:


grafico = figure(title = "Comparacion Estudiantes Urbana - Rural")

grafico.circle(x = 'Urbana', y = 'Rural', source = datos)


# In[9]:


show(grafico)


# In[10]:


leer_archivo2 = a.read_csv('instituciones_educativas_loja.csv', engine = 'python', header = 0, sep = ';', decimal = ".")


# In[11]:


leer_archivo2


# In[12]:


datos2 = ColumnDataSource(leer_archivo2)


# In[13]:


datos2


# In[14]:


datos2.column_names


# In[15]:


grafico2 = figure(title = "Comparacion Docentes Masculino - Femenino")

grafico2.square(x = 'DocentesFemenino', y = 'DocentesMasculino', source = datos2, color="red")


# In[16]:


show(grafico2)


# In[17]:


p = figure(title = "Comparacion Docentes Masculino - Femenino de Archivo2")
p.hbar(right = 'DocentesFemenino', y = 'DocentesMasculino', source = datos2 ,height=0.5, left=0, color="navy")

show(p)


# In[18]:


p = figure(title = "Comparacion Total Docentes Masculino - Total Administrativo")
df = leer_archivo2["TotalDocentes"][:5]
df2 = leer_archivo2["TotalAdministrativos"][:5]
p.line(df, df2, line_width=1)

show(p)


# In[19]:


p = figure(title = "Subida  exponencial de Total de Docentes")
x= leer_archivo2["TotalDocentes"][:4]
y = [10**xx for xx in x]
p.line(x , y, line_width=2)
p.circle(x , y, fill_color="white", size=8)

show(p)


# In[20]:


p = figure(title = "Comparacion Total de Alumnos - Total de Docentes")
p.patch(leer_archivo2["Total_Alumnos"][:15], leer_archivo2["TotalDocentes"][:15], alpha=0.5, line_width=2)
show(p)


# In[21]:


p = figure(title = "Comparacion de EstudiantesMasculino - DocentesMasculino")
x = leer_archivo2["EstudiantesMasculino"]
y= leer_archivo2["DocentesMasculino"]
p.rect(x, y, width=10, height=20, color="green",
       angle=pi/3, height_units="screen")

show(p)


# In[22]:


p = figure(title = "Comparacion Estudiantes Femenino - Docentes Femenino")
a = leer_archivo2["EstudiantesFemenino"]
b= leer_archivo2["DocentesFemenino"]
p.square(a, b, size=20, color="pink", alpha=0.5)
show(p)


# In[23]:


p = figure(title = "Comparacion Docentes Femenino - TotalAdministrativo")
da = leer_archivo2["TotalAdministrativos"]
db = leer_archivo2["DocentesFemenino"]
p.ellipse(da, db, width= 2, height=4,
          angle=pi/3, color="blue")

show(p)


# In[24]:


p = figure(title = "Comparacion Docentes Masculino - Docentes Femenino - TotalAdministrativo")
x = leer_archivo2["TotalAdministrativos"]
y = leer_archivo2["DocentesFemenino"]
radii = leer_archivo2["DocentesMasculino"]

colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
]


TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

show(p)

