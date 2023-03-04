# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:09:54 2023

@author: Asus
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#%%

caudal=pd.read_excel('Proyecto_final/dt_caudal.xlsx')

#%%

sns.lineplot(data=caudal, x='hora', y='caudal')
xlabel='tiempo'
ylabel='Caudal'

#%%
def sum_riemann(xi,xf,f,n):
    A=0
    xbar=[f['hora'].index[xi]]
    ybar=[0]
    
    while xi<=xf:
        
        di=f['hora'].index[xi]
        fi=f['caudal'][di]
        df=f['hora'].index[xi+n]
        ff=f['caudal'][df]
        
        xbar.append(di)
        ybar.append(fi)
            
        xbar.append(df)
        ybar.append(fi)        
            
        xbar.append(df)
        ybar.append(0)
        delta=(df-di)*(10*60/1000)
        
        A +=delta*(fi+ff)/2
        xi=xi+n
       
    return(A, xbar, ybar)

#%%
xi=50
xf=100
n=6

plt.plot(caudal['hora'], caudal['caudal'], label='Q. medido')
(A, xbar, ybar)=sum_riemann(xi,xf,caudal,n)
plt.plot(xbar,ybar, linestyle='--', color='r', linewidth=1, label='Aprox. Riemann')
plt.legend()
plt.xlabel('x10 minutos')
plt.ylabel('Caudal (l/s)')
print(A)



