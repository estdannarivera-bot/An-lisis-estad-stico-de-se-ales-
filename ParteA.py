# LABORATORIO 1 - ANALISIS ESTADISTICO DE SEÑALES

# IMPORTAR LIBRERIAS


import wfdb
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


# CARGAR SEÑAL


record = wfdb.rdrecord('100')   # No poner .dat
signal = record.p_signal[:, 0] # Canal 0
fs = record.fs                 # Frecuencia de muestreo

# Vector de tiempo
t = np.arange(len(signal)) / fs


#  GRAFICAR SEÑAL


#plt.figure()
#plt.plot(t, signal)
#plt.title("Señal ECG - Registro 100")
#plt.xlabel("Tiempo (s)")
#plt.ylabel("Amplitud (mV)")
#plt.grid()
#plt.show()


# CALCULOS MANUALES


N = len(signal)

# ---- MEDIA ----
media = sum(signal) / N

# ---- VARIANZA ----
var = sum((signal - media)**2) / N

# ---- DESVIACION ESTANDAR ----
std = np.sqrt(var)

# ---- COEFICIENTE DE VARIACION ----
cv = std / media

# ---- SKEWNESS MANUAL ----
skew_manual = sum(((signal - media)/std)**3) / N

# ---- CURTOSIS MANUAL ----
kurt = sum(((signal - media)/std)**4) / N


# FUNCIONES DE PYTHON


media_np = np.mean(signal)
std_np = np.std(signal)
cv_np = std_np / media_np
skew_np = skew(signal)
kurt_np = kurtosis(signal)



#  MOSTRAR RESULTADOS


print("============== RESULTADOS MANUALES ==============")
print("Media:", media)
print("Desviación estándar:", std)
print("Coeficiente de variación:", cv)
print("Skewness:", skew_manual)
print("Curtosis:", kurt)

print("\n============== RESULTADOS NUMPY/SCIPY ==============")
print("Media:", media_np)
print("Desviación estándar:", std_np)
print("Coeficiente de variación:", cv_np)
print("Skewness:", skew_np)
print("Curtosis:", kurt_np)


# 8. DIFERENCIA ENTRE METODOS


print("\n============== DIFERENCIAS ==============")
print("Diferencia Media:", abs(media - media_np))
print("Diferencia STD:", abs(std - std_np))
print("Diferencia Skew:", abs(skew_manual - skew_np))
print("Diferencia Kurt:", abs(kurt - kurt_np))

# Mostrar solo 10 segundos
segundos = 10
muestras = int(segundos * fs)

plt.figure()
plt.plot(t[:muestras], signal[:muestras])
plt.title("Señal ECG - 10 segundos")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.grid()
plt.show()

#  HISTOGRAMA


plt.figure()
plt.hist(signal[:muestras], bins=50)
plt.title("Histograma ECG - 10 segundos")
plt.xlabel("Amplitud (mV)")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()

