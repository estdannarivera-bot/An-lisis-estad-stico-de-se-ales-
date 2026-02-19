import serial
import numpy as np
import matplotlib.pyplot as plt
import time

# CONFIGURACIÓN
PORT = 'COM4'      # Puerto serial
BAUD = 115200      # Velocidad
FS = 200           # Frecuencia de muestreo (Hz)
TIEMPO = 10        # segundos
N = FS * TIEMPO    # muestras 

VREF = 3.3         # Voltaje STM32
ADC_MAX = 4095     # 12 bits


# ADQUISICIÓN
ser = serial.Serial(PORT, BAUD, timeout=1)  # Abrir puerto 
time.sleep(2) # Esperar a que el puerto se estabilice

x = [] # Almacenar muestras
print("Adquiriendo señal...")

while len(x) < N:  # Adquirir hasta N muestras
    try:
        line = ser.readline().decode('utf-8').strip() # Leer línea
        if line.isdigit():                            # Verificar que es un número
            value = int(line)                         # Convertir a entero
            x.append(value)                           
    except:
        pass

ser.close()            # Cerrar puerto
x = np.array(x)        # Convertir a numpy array

# CONVERSIÓN A VOLTAJE
v = (x / ADC_MAX) * VREF      # Voltios
v_mv = v * 1000               # mV

# GUARDAR ARCHIVOS
np.savetxt("senal.txt", v_mv)    # Indicar nombre del archivo

# EJE TEMPORAL
t = np.arange(len(x)) / FS      # Tiempo en segundos

# GRÁFICA 10s (mV)
m = int(10 * FS)                 # Muestras para 10 segundos

plt.plot(t[:m], v_mv[:m])
plt.title("Señal adquirida (10 s)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.ylim(0, 3300)
plt.grid()
plt.show()

# ESTADÍSTICA (en voltios)
mu = np.mean(v)
sigma = np.std(v)
cv = sigma / mu if mu != 0 else 0
sk = np.mean(((v - mu) / sigma) ** 3)
ku = np.mean(((v - mu) / sigma) ** 4)

stats = {
    "Media (V)": mu,              # Media en voltios
    "Desviación (V)": sigma,      # Desviación estándar en voltios
    "Coef. Variación": cv,        # Coeficiente de variación
    "Skewness": sk,               
    "Curtosis": ku
}

# HISTOGRAMA (mV)
plt.figure()
plt.hist(v_mv, bins=100)                    # Más bins para mejor resolución
plt.title("Histograma señal adquirida")
plt.xlabel("Voltaje (mV)")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()

# RESULTADOS
print("\nRESULTADOS ESTADÍSTICOS")
for k, v in stats.items():           # Imprimir resultados
    print(f"{k}: {v}")               # Formato de impresión
