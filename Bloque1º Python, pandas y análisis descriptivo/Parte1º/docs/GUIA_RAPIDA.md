# Guía Rápida - Bloque 1 Parte 1

## 🎯 Objetivo General

Al finalizar esta parte, serás capaz de **cargar, limpiar, transformar y analizar un dataset tabular con Python y pandas**, generando conclusiones iniciales útiles para un proyecto de análisis de datos.

## 📚 Contenidos Específicos

### 1. Fundamentos de Python (0:20–0:50)
- Variables, tipos de datos y asignación
- Listas y diccionarios
- Condicionales (if/else)
- Bucles (for, while)
- Funciones básicas con argumentos y retornos
- Aplicación en contexto de análisis de negocios

### 2. NumPy y Operaciones Vectorizadas (0:50–1:25)
- Creación y manipulación de arrays
- Operaciones elemento a elemento
- Funciones estadísticas: `mean()`, `median()`, `std()`, `min()`, `max()`
- Ventajas de vectorización vs. bucles
- Generación de datos sintéticos reproducibles

### 3. Carga y Exploración de Datos (1:35–2:15)
- Lectura de archivos CSV con `pd.read_csv()`
- Inspección: `shape`, `info()`, `head()`, `tail()`
- Detección de: tipos de datos incorrectos, valores nulos, duplicados
- Análisis inicial descriptivo con `describe()`
- Documentación de hallazgos

### 4. Limpieza de Datos
- Eliminación de duplicados
- Conversión de tipos (fechas, numéricos, categóricos)
- Imputación de valores faltantes (mediana para numéricos, etiquetas para categóricos)
- Creación de variables derivadas (extractores de fechas, ratios, transformaciones)
- Control de calidad post-limpieza

### 5. Análisis Descriptivo (2:15–2:45)
- Estadísticos univariantes: media, mediana, rango, desviación típica
- Agregaciones: `groupby()`, `sum()`, `mean()`, `agg()`
- Análisis por categorías y regiones
- Identificación de valores extremos
- Interpretación comercial

### 6. Visualización Básica
- Histogramas: distribuciones de variables continuas
- Boxplots: comparación por grupos
- Gráficos de barras: sumas/promedios por categoría
- Gráficos de línea: series temporales
- Títulos, etiquetas y leyendas

### 7. Redacción de Conclusiones
- Conversión de números en interpretación comercial
- Estructura de un mini-informe automático
- Buenas prácticas en documentación de hallazgos

## ⏱️ Agenda de la Sesión

| Duración | Actividad |
|:---:|---|
| 0:00–0:20 | Ecosistema Python para análisis de datos |
| 0:20–0:50 | Repaso aplicado de Python |
| 0:50–1:25 | NumPy y pandas introducción |
| 1:25–1:35 | **Pausa** |
| 1:35–2:15 | Carga, exploración y limpieza de datos |
| 2:15–2:45 | Análisis descriptivo y visualización |
| 2:45–3:00 | Ejercicio integrador y conclusiones |

## 💻 Dataset Utilizado

**`ventas_mayo_2026.csv`**: Dataset sintético con registros de transacciones de ventas incluyendo:
- Identificadores de cliente y transacción
- Fecha y hora de la operación
- Categoría y canal de venta
- Región geográfica
- Cantidad de unidades y precio unitario
- Importe total de la venta

## 📋 Tareas Prácticas

### Ejercicio Integrador

Realiza las siguientes tareas sobre el dataset de ventas:

1. ✅ Calcula las ventas totales por canal
2. ✅ Calcula el ticket medio por región
3. ✅ Identifica la categoría con mayor número de unidades vendidas
4. ✅ Genera un gráfico de barras con ventas por canal
5. ✅ Redacta tres conclusiones de negocio basadas en el análisis

### Entregable Esperado

Un notebook llamado `01_Bloque_I_Python_Pandas_Analisis_Descriptivo_ENTREGABLE.ipynb` que incluya:
- Código ejecutable y comentado
- Visualizaciones claras
- Sección final de **Conclusiones** con interpretación comercial

## ✅ Criterios de Éxito

Al finalizar, podrás:

- [ ] Escribir código Python limpio aplicado a datos
- [ ] Cargar y explorar datasets tabulares
- [ ] Limpiar y transformar datos de forma documentada
- [ ] Calcular estadísticas descriptivas univariantes y multivariantes
- [ ] Crear visualizaciones que comuniquen hallazgos
- [ ] Redactar conclusiones de negocio fundamentadas en datos

## 🔗 Referencias Rápidas

```python
# Carga
df = pd.read_csv("archivo.csv")

# Exploración
df.shape, df.info(), df.head(), df.describe()

# Limpieza
df.drop_duplicates(), df.fillna(valor), pd.to_datetime()

# Análisis
df.groupby("columna").agg({"otra": "sum"})

# Visualización
plt.hist(), plt.boxplot(), plt.bar()
```
