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



