import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas import DataFrame
from IPython.display import HTML
import scipy.signal as scpySig
import spectrum as sp

#######################################################################################
m = 200
N = 1000   
fs = 1000 # Hz
ts = 1/fs
df = fs/N
mean = 0  # Media
a1 = 1
SNR = np.array([3, 10])
noise_power = np.zeros_like(SNR)
noise = np.zeros_like(SNR)
noise_p = a1/(10**(SNR/10))

########################### Ejemplo para 3 db de ruido ########################
tt = np.linspace(0, (N-1), N) * ts 
ff = np.linspace(0, (N-1)*df, N).flatten()
fr = np.random.uniform(low = -1/2, high= 1/2, size = m)
noise = np.random.normal(mean, noise_p[0], size=(N, m))

freq_1 = ((np.pi/2)*fs)/(2*np.pi)
freq_2 = ((np.pi/2) + (fr * ((2*np.pi)/N)))*fs/(2*np.pi)
a_sign = np.sqrt(a1*2)

signal = a_sign * np.sin(2*np.pi * np.outer(tt, freq_2)) + noise
#ff, periodgram = scpySig.welch(signal, fs, window='hann', axis=0, nfft = N)

#plt.close("all")

#plt.semilogy(ff, periodgram)
#plt.ylim([0.5e-3, 1])
#plt.xlabel('frequency [Hz]')
#plt.ylabel('PSD [V**2/Hz]')
#plt.show()

#peaks_welch = np.argmax(periodgram, axis = 0)
#mean_welch = np.mean(peaks_welch)
#sesgo_welch = mean_welch - freq_1
#var_welch = np.var(peaks_welch)

psd_arma = []
psd_arma_peaks = []
plt.close("all")
for k in range (m):
    psd_arma.append(sp.parma(signal[:,0], 8, 8, 30, NFFT = N, sampling=fs))
    plt.semilogy(ff[0:int(N/2+1)], psd_arma[k].psd)    
    psd_arma_peaks.append(np.argmax(psd_arma[k].psd))

#plt.ylim([0.5e-3, 1])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

mean = np.mean(psd_arma_peaks)
sesgo = mean - freq_1
var = np.var(psd_arma_peaks)
    





