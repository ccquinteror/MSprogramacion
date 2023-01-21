import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import lagrange


ruta="C:\\Users\\Asus\\OneDrive - AGUAS DE MANIZALES SA ESP\\CCQuinteroR\\UniversidadAM\\Programacion\\ejercicio1\\data.xlsx"
data=pd.read_excel(ruta)

print(data.head(3))

col_data=data.columns[1:]

xi=np.array(data['beta'])

v_beta=55

res=[v_beta]


for i in col_data:
    #print(i)
    fi=np.array(data[i])
    poly=lagrange(xi,fi)
    #print(poly(v_beta))
    res.append(round(poly(v_beta),5))
    fig, axes=plt.subplots(1,1)
    axes.plot(xi,fi, 'o')
    axes.set_title(i)
    muestras = 100 # Numero cualquiera
    a = np.min(xi)
    b = np.max(xi)
    p_xi = np.linspace(a,b,muestras)
    pfi = poly(p_xi)
    plt.plot(p_xi,pfi)

    

res_t=np.transpose(res)
col_t=data.columns

g_res=pd.DataFrame()

g_res['variables']=col_t
g_res['valores']=res_t

print(g_res)
print('\n')


delta_x=20

pos1=list(g_res['variables'].values).index('s_deltax_l2')
pos2=list(g_res['variables'].values).index('s_l1_l2')
pos3=list(g_res['variables'].values).index('s_l3_l2')


l2_s=round(g_res['valores'][pos1]*delta_x,3)
l1_s=round(g_res['valores'][pos2]*l2_s,3)
l3_s=round(g_res['valores'][pos3]*l2_s,3)


pos1=list(g_res['variables'].values).index('v_deltax_l2')
pos2=list(g_res['variables'].values).index('v_l1_l2')
pos3=list(g_res['variables'].values).index('v_l3_l2')


l2_v=round(g_res['valores'][pos1]*delta_x,3)
l1_v=round(g_res['valores'][pos2]*l2_v,3)
l3_v=round(g_res['valores'][pos3]*l2_v,3)

print('Las dimensiones de L1,L2 y L3 son: \n')

print('el valor de L2, para el criterio de rectitud es: {}'.format(l2_s))
print('el valor de L1, para el criterio de rectitud es: {}'.format(l1_s))
print('el valor de L3, para el criterio de rectitud es: {} \n'.format(l3_s))

print('el valor de L2, para el criterio de velocidad es: {}'.format(l2_v))
print('el valor de L1, para el criterio de velocidad es: {}'.format(l1_v))
print('el valor de L3, para el criterio de velocidad es: {}'.format(l3_v))