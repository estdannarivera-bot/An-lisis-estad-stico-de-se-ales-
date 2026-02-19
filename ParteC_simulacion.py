import numpy as np
import matplotlib.pyplot as plt

# CONFIGURACIÓN GENERAL
FS = 200                 # Frecuencia de muestreo 
TIEMPO = 10              # segundos
N = FS * TIEMPO          # muestras

# Archivos
ARCHIVO_SENAL = "senal.txt"     # señal desde Parte B

# CARGAR SEÑAL REAL
senal_real = np.loadtxt(ARCHIVO_SENAL)

# Convercion a voltios
senal_real_v = senal_real / 1000.0

# Eje temporal
t = np.arange(len(senal_real_v)) / FS


# GENERACIÓN DE RUIDOS

# 1. Ruido gaussiano (blanco)
media_ruido = 0
std_ruido = 0.05   # desviación estándar en voltios
ruido_gauss = np.random.normal(media_ruido, std_ruido, N)

# 2. Ruido impulsivo (picos aleatorios)
ruido_impulsivo = np.zeros(N)
num_impulsos = int(0.01 * N)  # 1% de muestras con impulsos
indices = np.random.randint(0, N, num_impulsos)
ruido_impulsivo[indices] = np.random.uniform(-1, 1, num_impulsos)

# 3. Ruido tipo artefacto muscular (alta frecuencia)
frecuencia_muscular = 50  # Hz
ruido_muscular = 0.02 * np.sin(2*np.pi*frecuencia_muscular*t)


# CONTAMINACIÓN DE LA SEÑAL
senal_gauss = senal_real_v + ruido_gauss
senal_impulsiva = senal_real_v + ruido_impulsivo
senal_muscular = senal_real_v + ruido_muscular


# FUNCIÓN SNR
def calcular_snr(senal, ruido):
    """
    SNR = 10 * log10( Potencia señal / Potencia ruido ) 
    """
    potencia_senal = np.mean(senal**2)
    potencia_ruido = np.mean(ruido**2)
    return 10 * np.log10(potencia_senal / potencia_ruido)

snr_gauss = calcular_snr(senal_real_v, ruido_gauss)
snr_imp = calcular_snr(senal_real_v, ruido_impulsivo)
snr_musc = calcular_snr(senal_real_v, ruido_muscular)


# GUARDAR RESULTADOS
np.savetxt("senal_gauss.txt", senal_gauss)
np.savetxt("senal_impulsiva.txt", senal_impulsiva)
np.savetxt("senal_muscular.txt", senal_muscular)

with open("resultados_snr.txt", "w") as f:
    f.write("RESULTADOS SNR\n")
    f.write(f"SNR Ruido Gaussiano: {snr_gauss:.2f} dB\n")
    f.write(f"SNR Ruido Impulsivo: {snr_imp:.2f} dB\n")
    f.write(f"SNR Ruido Muscular: {snr_musc:.2f} dB\n")


# GRÁFICAS

m = int(10 * FS)  # 10 segundos

# Señal original
plt.figure()
plt.plot(t[:m], senal_real_v[:m])
plt.title("Señal real")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()

# Ruido gaussiano
plt.figure()
plt.plot(t[:m], senal_gauss[:m])
plt.title(f"Señal con ruido gaussiano | SNR = {snr_gauss:.2f} dB")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()

# Ruido impulsivo
plt.figure()
plt.plot(t[:m], senal_impulsiva[:m])
plt.title(f"Señal con ruido impulsivo | SNR = {snr_imp:.2f} dB")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()

# Ruido muscular
plt.figure()
plt.plot(t[:m], senal_muscular[:m])
plt.title(f"Señal con artefacto muscular | SNR = {snr_musc:.2f} dB")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()

# HISTOGRAMAS
plt.figure()
plt.hist(senal_real_v, bins=100)
plt.title("Histograma señal real")
plt.grid()
plt.show()

plt.figure()
plt.hist(senal_gauss, bins=100)
plt.title("Histograma señal con ruido gaussiano")
plt.grid()
plt.show()

plt.figure()
plt.hist(senal_impulsiva, bins=100)
plt.title("Histograma señal con ruido impulsivo")
plt.grid()
plt.show()

plt.figure()
plt.hist(senal_muscular, bins=100)
plt.title("Histograma señal con ruido muscular")
plt.grid()
plt.show()

# RESULTADOS EN CONSOLA
print("RESULTADOS PARTE C - ANÁLISIS DE RUIDO")
print(f"SNR Gaussiano   : {snr_gauss:.2f} dB")
print(f"SNR Impulsivo   : {snr_imp:.2f} dB")
print(f"SNR Muscular    : {snr_musc:.2f} dB")
