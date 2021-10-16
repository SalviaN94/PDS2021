import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import signal

def sin_signal(vmax, dc, ff, ph, nn, fs):
    ts = 1/fs           #Tiempo de muestreo

    #Grilla de sampleo temporal
    #np.linspace devuelve numeros igualmente espaciados en un intervalo
    #flaten Devuelve una copia del array en una dimensión
    tt = np.linspace(0, (nn-1)*ts, nn).flatten()
    
    x = np.array([], dtype=np.float).reshape(nn,0)
    
    aux = dc + (vmax * np.sin(2*np.pi*ff*tt + ph))
    
    x = np.hstack([x, aux.reshape(nn,1)])
    return x,tt
    
def square_signal(vmax, dc, ff, duty, nn, fs):
    ts = 1/fs           #Tiempo de muestreo

    #Grilla de sampleo temporal
    #np.linspace devuelve numeros igualmente espaciados en un intervalo
    #flaten Devuelve una copia del array en una dimensión
    tt = np.linspace(0, (nn-1)*ts, nn).flatten()
    
    x = np.array([], dtype=np.float).reshape(nn,0)
    
    aux = dc + (vmax * signal.square(2 * np.pi* ff *tt, duty));
    
    x = np.hstack([x, aux.reshape(nn,1)])
    return x,tt
    
def sawtooth_signal(vmax, dc, ff, nn, fs):
    ts = 1/fs           #Tiempo de muestreo

    #Grilla de sampleo temporal
    #np.linspace devuelve numeros igualmente espaciados en un intervalo
    #flaten Devuelve una copia del array en una dimensión
    tt = np.linspace(0, (nn-1)*ts, nn).flatten()
    
    x = np.array([], dtype=np.float).reshape(nn,0)
    
    aux = dc + (vmax * signal.sawtooth(2 * np.pi* ff *tt));
    
    x = np.hstack([x, aux.reshape(nn,1)])
    return x,tt
    

# #x,tt = sin_signal(vmax=1, dc=0, ff=10, ph=0, nn=1000, fs=1000.0)
# #x,tt = square_signal(vmax=1, dc=0, ff=5, duty=0.5, nn=1000, fs=1000.0)
# x,tt = sawtooth_signal(vmax=1, dc=0, ff=10, nn=1000, fs=1000.0)

# plt.figure(1)
# line_hdls = plt.plot(tt, x)
# plt.title('Señal: Senoidal' )
# plt.xlabel('tiempo [segundos]')
# plt.ylabel('Amplitud [V]')
# axes_hdl = plt.gca()    
# plt.show()

    
    
    
    





