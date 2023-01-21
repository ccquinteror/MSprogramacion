# Se importan las librerías que se necesitan
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import lagrange

# Se carga la base de datos del repositorio archivo base actualizado
ruta="https://github.com/ccquinteror/MSprogramacion/blob/main/data.xlsx?raw=true"
data=pd.read_excel(ruta)

print(data.head(3))

# se define el vector xi

col_data=data.columns[1:]
xi=np.array(data['beta'])

muestras = 100 # Número cualquiera
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a,b,muestras)

# Defino el valor de xi para el que quiero encontrar los demás parámetros
v_beta=55

res=[v_beta]


# Se crean las funciones de lagrange mediante un ciclo
for i in col_data:
    fi=np.array(data[i]) # el vector fi toma los valores de cada columna
    poly=lagrange(xi,fi) # realiza la interpolación de lagrange
    res.append(round(poly(v_beta),5)) # evalúa el valor v_beta en la función
    plt.plot(xi,fi, 'o') # Crea el gráfico de los puntos
    # Dibuja una línea de la función de regresión de lagrange
    pfi = poly(p_xi)
    plt.plot(p_xi,pfi)
    plt.title(i) # Define el nombre del gráfico
    plt.show()

# Obtengo los vectores de variables y valores para el punto deseado (v_beta)
res_t=np.transpose(res)
col_t=data.columns

# Se crea un dataframe con las listas anteriores
g_res=pd.DataFrame()

g_res['variables']=col_t
g_res['valores']=res_t

print(g_res) # Ploteo el dataframe
print('\n')


delta_x=20 # Defino el valor de delta x

# Busco la posición de las variables que necesito dentro del dataframe
# de respuesta para el parámetro de rectitud

pos1=list(g_res['variables'].values).index('s_deltax_l2')
pos2=list(g_res['variables'].values).index('s_l1_l2')
pos3=list(g_res['variables'].values).index('s_l3_l2')

# Determino el valor de L2, L1 y L3
l2_s=round(g_res['valores'][pos1]*delta_x,3)
l1_s=round(g_res['valores'][pos2]*l2_s,3)
l3_s=round(g_res['valores'][pos3]*l2_s,3)



# Busco la posición de las variables que necesito dentro del dataframe
# de respuesta para el parámetro de velocidad

pos1=list(g_res['variables'].values).index('v_deltax_l2')
pos2=list(g_res['variables'].values).index('v_l1_l2')
pos3=list(g_res['variables'].values).index('v_l3_l2')

# Determino el valor de L2, L1 y L3
l2_v=round(g_res['valores'][pos1]*delta_x,3)
l1_v=round(g_res['valores'][pos2]*l2_v,3)
l3_v=round(g_res['valores'][pos3]*l2_v,3)

# Ploteo los resultados de las variables L1,L2 y L3 para cada criterio

print('Las dimensiones de L1,L2 y L3 son: \n')

print('el valor de L2, para el criterio de rectitud es: {}'.format(l2_s))
print('el valor de L1, para el criterio de rectitud es: {}'.format(l1_s))
print('el valor de L3, para el criterio de rectitud es: {} \n'.format(l3_s))

print('el valor de L2, para el criterio de velocidad es: {}'.format(l2_v))
print('el valor de L1, para el criterio de velocidad es: {}'.format(l1_v))
print('el valor de L3, para el criterio de velocidad es: {}'.format(l3_v))
# %%
