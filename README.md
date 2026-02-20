# Laboratorio 1  
## Análisis Estadístico de Señales Biomédicas  

**Programa:** Ingeniería Biomédica  
**Asignatura:** Procesamiento Digital de Señales  
**Universidad:** Universidad Militar Nueva Granada  
**Estudiantes:** Danna Rivera, Duvan Paez

---
# Parte A
## Base de datos utilizada

Se empleó el registro **100** de la base de datos **MIT-BIH Arrhythmia Database**, disponible en:

PhysioNet  
https://physionet.org/

La señal analizada corresponde a un **Electrocardiograma (ECG)**.


## Procedimiento

### 1. Carga de la señal

Se utilizó la función `rdrecord()` de la librería `wfdb` para cargar el registro 100.  
Se extrajo el canal 0 de la señal y la frecuencia de muestreo correspondiente.

Se construyó un vector de tiempo a partir del número de muestras y la frecuencia de muestreo.

### 2. Visualización de la señal

Se graficaron los primeros 10 segundos de la señal ECG con el fin de observar de manera mas precisa y clara, la forma de la señal, permitiendo visualizar mejor sus complejos.

#### Señal ECG (10 segundos)

![Señal ECG](ECG.png)

---

### 3. Cálculo de parámetros estadísticos

Se calcularon los siguientes estadísticos descriptivos:

- Media  
- Varianza  
- Desviación estándar  
- Coeficiente de variación  
- Asimetría (Skewness)  
- Curtosis  

#### Método 1: Implementación manual

Se programaron directamente las fórmulas matemáticas para cada parámetro, utilizando operaciones básicas y estructuras de cálculo explícitas.

## 1. Media

La media representa el valor promedio de la señal.

**Fórmula:**
```python
media = sum(signal) / N
```

**Lógica del cálculo:**
- Se suman todas las muestras de la señal.
- Se divide el resultado entre el número total de datos (N).
- Esto permite obtener el valor central de la señal.

---

## 2. Varianza

La varianza mide la dispersión de los datos respecto a la media.

**Fórmula:**
```python
var = sum((signal - media)**2) / N
```

**Lógica del cálculo:**
- Se resta la media a cada muestra (centrado).
- Se eleva cada diferencia al cuadrado para evitar cancelaciones por signo.
- Se promedian esas diferencias cuadráticas.
- El resultado indica qué tan dispersa está la señal.

---

## 3. Desviación estándar

La desviación estándar es la raíz cuadrada de la varianza.

**Fórmula:**
```python
std = np.sqrt(var)
```

**Lógica del cálculo:**
- Devuelve la dispersión a las mismas unidades originales de la señal.
- Permite interpretar la variabilidad de forma más intuitiva.

## 4.Coeficiente de Variación

Mide la variabilidad relativa respecto a la media.

**Fórmula:**
```python
cv = std / media
```

## 5. Estandarización

La estandarización transforma la señal restando la media y dividiendo por la desviación estándar.
**Fórmula:**
```python
z = (signal - media) / std
```

Esta variable `z` es la que se utiliza posteriormente para calcular la asimetría y la curtosis:

```python
skew_manual = sum(z**3) / N
kurt = sum(z**4) / N
```

**Lógica del cálculo:**
- Se resta la media.
- Se divide por la desviación estándar.
- Se obtiene una variable adimensional.
- Permite analizar la forma de la distribución sin depender de la amplitud.


## 6. Asimetría y Curtosis

**Asimetría:**  
**Fórmula:**
```python
skew_manual = sum(((signal - media)/std)**3) / N
```
Evalúa si la distribución está inclinada hacia la derecha o izquierda.

Se calcula elevando al cubo los valores estandarizados.

**Curtosis:**  
**Fórmula:**
```python
kurt = sum(((signal - media)/std)**4) / N
```
Evalúa qué tan pronunciados son los picos de la distribución.

Se calcula elevando a la cuarta potencia los valores estandarizados.






#### Método 2: Funciones predefinidas

Se utilizaron funciones de Python:

- `numpy.mean()`  
- `numpy.std()`  
- `scipy.stats.skew()`  
- `scipy.stats.kurtosis()`  

Posteriormente se calcularon las diferencias absolutas entre ambos métodos para verificar la consistencia de los resultados.


### 4. Histograma

Se construyó el histograma correspondiente a los primeros 10 segundos de la señal ECG, utilizando el mismo segmento previamente graficado en el dominio del tiempo. Esto permitió analizar la distribución de frecuencias de amplitud sobre exactamente la misma muestra de datos, garantizando coherencia en el análisis estadístico.

#### Histograma ECG (10 segundos)

![Histograma ECG](HISTOGRAMA.png)


## Comparación de resultados

Las diferencias obtenidas entre los cálculos manuales y los generados por las funciones de Python fueron prácticamente nulas, lo que valida la correcta implementación de las fórmulas matemáticas.


## Archivo principal de lo mencionado (Parte A)

`ParteA.py`

---
# Configuración STM32

## Sistema de adquisición y transmisión de datos

Se utiliza una Blackpill STM32 como sistema de adquisición de datos:
### Hardware:
- Microcontrolador: STM32 Blackpill
- Entrada analógica: Pin A0
- Comunicación USB: USB CDC (Virtual COM Port)

## Funcionamiento general

El sistema realiza el siguiente proceso:
1. Lectura de la señal analógica en el pin A0
2. Conversión analógica-digital mediante el ADC interno del STM32
3. Transferencia automática del dato usando DMA
4. Envío del valor digital (en forma de texto) por USB al computador
5. Recepción de los datos en python mediante un puerto serial virtual (COM)

## Archivo principal 

`PARTEC_LAB1.rar`

Al extraer este archivo se encuentra la carpeta correspondiente al código de C, por lo que se debe buscar en MDK-ARM el archivo de keil, en este se busca: 

`main.c`

El cual contiene:

- Configuración del ADC
- Configuración del DMA
- Configuración USB-CDC
- Rutina de adquisición
- Envío de datos por USB al PC 

## Uso

1. Conectar la señal analógica al pin A0
2. Conectar la Blackpill por USB al computador
3. Cargar el firmware en el STM32
4. Abrir el script Python de adquisición
`ParteB.py`
5. Leer los datos desde el puerto COM
   
---
# Parte B
# Parte B
## Adquisición y análisis de señal fisiológica con STM32

En esta sección se generó una señal fisiológica del mismo tipo empleado en la Parte A mediante un generador biológico. La señal fue adquirida usando una tarjeta STM32, almacenada en formato .txt, procesada en Python y analizada estadísticamente.
Archivo principal:

`ParteB.py`

## Configuración de adquisición

-Puerto serial: COM5

-Baudrate: 115200

-Frecuencia de muestreo: 200 Hz

-Tiempo de adquisición: 10 s

-Resolución ADC: 12 bits (0–4095)

-Voltaje de referencia: 3.3 V

-Total de muestras:

N = 200 × 10 = 2000
```python
FS = 200           # Frecuencia de muestreo (Hz)
TIEMPO = 10        # segundos
N = FS * TIEMPO    # muestras 
```
## Procedimiento
### 1. Lectura de datos

Se estableció comunicación serial con la STM32 utilizando la librería `serial`. El programa recibe los valores digitales del ADC hasta completar las 2000 muestras, validando que cada dato sea numérico antes de almacenarlo.


###  2. Conversión a voltaje

El ADC entrega valores entre 0 y 4095. Para obtener el voltaje real se utilizó:
```python
v = (x / ADC_MAX) * VREF
v_mv = v * 1000 
```
Esta conversión es fundamental, ya que transforma los niveles digitales en una magnitud física real (voltaje).

### 3. Construcción del eje temporal y visualización

El eje de tiempo se generó mediante:
```python
t = np.arange(len(x)) / FS 
```

Se graficaron los 10 segundos adquiridos para analizar el comportamiento temporal de la señal.

### 4. Parámetros estadísticos

Se calcularon:

-Media

-Desviación estándar

-Coeficiente de variación

-Asimetría

-Curtosis

```python
mu = np.mean(v)
sigma = np.std(v)
cv = sigma / mu
sk = np.mean(((v - mu) / sigma) ** 3)
ku = np.mean(((v - mu) / sigma) ** 4)
```

### 5. Histograma

Se construyó el histograma de las muestras adquiridas para analizar la distribución de amplitudes.


### Comparación con la Parte A

En la Parte A se utilizó una señal de base de datos; en la Parte B se realizó adquisición real. Por ello, la señal puede presentar mayor variabilidad, ruido y efectos de cuantización del ADC, permitiendo un análisis más cercano a condiciones reales de medicición.}

---
# Parte C

## Análisis de ruido

En esta parte se realiza el análisis de ruido por simulación en software, a partir de una señal real previamente capturada y almacenada en un archivo de texto.
El objetivo es estudiar cómo diferentes tipos de ruido afcetan una señal biomédica y cómo se degrada su calidad.

## Funcionamiento general

El código realiza el siguiente proceso:
1. Carga una señal desde un archivo .txt
2. Genera ruido de forma digital (simulación matemática)
3. Contamina la señal sumando el ruido
4. Calcula la relación señal/ruido (SNR)
5. Analiza estadísticamente la señal
6. Genera gráficas e histogramas
7. Guarda los resultados en archivos

## Archivo principal

`ParteC_simulacion.py`

Este archivo contiene todo el procedimiento previamente visto.

## Entrada de datos

La señal se carga desde un archivo generado previamente (el de la parte B):

`senal_real = np.loadtxt(ARCHIVO_SENAL)`

## Tipos de ruidos

### Ruido gaussiano (ruido blanco)

`ruido_gauss = np.random.normal(media_ruido, std_ruido, N)`

Este ruido simula:

- Ruido térmico
- Ruido electrónico del sistema
- Interferencias aleatorias
- Ruido blanco

El parámetro mas importante para controlar la intensidad del ruido es:

`std_ruido = 0.05`

### Ruido impulsivo (picos aleatorios)

`ruido_impulsivo[indices] = np.random.uniform(-1, 1, num_impulsos)`

Este ruido simula:

- Picos eléctricos
- Interferencias
- Descargas
- Errores de transmisión

Se caracteriza por pocos valores de gran amplitud, el parámetro mas importante controla la cantidad de impulsos:

`num_impulsos = int(0.01 * N)`

### Ruido tipo artefacto (alta frecuencia)

`ruido_muscular = 0.02 * np.sin(2*np.pi*frecuencia_muscular*t)`

Este ruido simula:

- Actividad muscular
- Artefactos fisiológicos
- Ruido biológico
- Interferencia por movimiento

Es un ruido periódico de alta frecuencia por lo que este sera su parámetro mas importante:

`frecuencia_muscular = 50`

## Contaminación de la señal 

La contaminación se realiza digitalmente mediante suma directa:

`senal_contaminada = senal_real + ruido`

Esto permite simular el efecto del ruido sobre la señal sin necesidad de hardware.

## Uso

1. Verificar que el archivo de señal esté en la carpeta del proyecto
2. Ejecutar
3. Visualizar las gráficas
4. Revisar los archivos de resultados
5. Analizar valores de SNR
