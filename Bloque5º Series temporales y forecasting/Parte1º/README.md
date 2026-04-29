# Bloque 5 - Parte 1: Series Temporales y Forecasting

## 📚 Introducción

Bienvenidos al Bloque 5, Parte 1: **Series Temporales y Forecasting**. En esta unidad, haremos la transición desde el análisis estático de datos hacia el análisis **dinámico y secuencial**.

### ¿Por Qué es Importante el Análisis de Series Temporales?

Las series temporales son omnipresentes en los negocios modernos:
- **Ventas y demanda diarias** en retail y e-commerce
- **Tráfico web y usuarios activos** en plataformas digitales
- **Precios de activos** en mercados financieros
- **Consumo energético** en utilities
- **Métricas de salud** en dispositivos wearables

La clave fundamental: **el orden de los datos importa**. Predecir mañana basándote en ayer no es lo mismo que usar cualquier día aleatorio del pasado.

### Objetivos de Aprendizaje

Al finalizar esta parte, serás capaz de:

1. **Comprender la anatomía de una serie temporal**
   - Tendencia (trend)
   - Estacionalidad (seasonality)
   - Ruido e irregularidades
   - Componentes y descomposición

2. **Transformar tiempo en características predictoras**
   - Variables rezagadas (lags)
   - Medias móviles (rolling windows)
   - Características temporales (día, mes, dow)
   - Variables externas

3. **Construir baselines simples pero efectivos**
   - Predicción ingenua (naive forecast)
   - Medias móviles
   - Métodos de referencia para comparación

4. **Aplicar Machine Learning a series temporales**
   - Random Forest para forecasting
   - Separación temporal correcta de train/test
   - Evaluación apropiada

## 📋 Estructura del Dataset

**Archivo**: `demanda_diaria_mayo_2026.csv` (90 registros diarios)

### Variables:
- `fecha`: Fecha calendario
- `demanda`: Variable objetivo (demanda diaria)
- `promocion`: Indicador de promoción activa
- `festivo`: Indicador de día festivo/fin de semana
- `temperatura`: Temperatura ambiental
- `stock_disponible`: Stock en almacén

## 🚀 Quickstart

```bash
# 1. Preparar entorno
conda env create -f environment.yml
conda activate bloque5

# 2. Abrir notebook
jupyter notebook notebooks/05_Bloque_V_Series_Temporales_Forecasting_Entregable.ipynb
```

## 🎯 Contenido del Notebook

1. Carga e indexación temporal
2. Visualización de la serie
3. Descomposición de componentes
4. Ingeniería de features
5. Baselines (Naive + Media Móvil)
6. Modelo Random Forest
7. Evaluación y métricas
8. Análisis de importancia

## 💡 Conceptos Clave

### Lags y Medias Móviles

```python
# Lag: el valor de hace n períodos
df['lag_1'] = df['demanda'].shift(1)    # ayer
df['lag_7'] = df['demanda'].shift(7)    # hace 7 días

# Media móvil: promedio de últimos n períodos
df['ma_7'] = df['demanda'].rolling(7).mean()  # promedio últimos 7 días
```

### Split Temporal Correcto

```python
# ❌ INCORRECTO: random split
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# ✓ CORRECTO: temporal split
n = len(df)
train_size = int(n * 0.8)
X_train = X[:train_size]
X_test = X[train_size:]
```

## 📊 Métricas de Evaluación

- **MAE** (Mean Absolute Error): Error promedio en unidades originales
- **RMSE** (Root Mean Squared Error): Penaliza errores grandes
- **MAPE** (Mean Absolute Percentage Error): Error porcentual

## 🚀 Cómo Empezar

### Opción 1: Usando pip (recomendado para Windows)
```bash
cd Parte1º
pip install -r requirements.txt
jupyter lab
```

### Opción 2: Usando Conda
```bash
cd Parte1º
conda env create -f environment.yml
conda activate big_data_bloque5_parte1
jupyter lab
```

## 📚 Contenido del Notebook Entregable

1. **Indexación Temporal**: Conversión a DateTime y establecimiento de índice
2. **Visualización**: Gráficos de evolución de la serie
3. **Descomposición**: Tendencia, estacionalidad, componentes
4. **Feature Engineering**: Creación de variables predictoras
5. **Baselines**: Comparación con métodos simples
6. **Random Forest**: Modelo de forecasting avanzado
7. **Evaluación**: MAE, RMSE, gráficos de comparación
8. **Importancia**: Características más influyentes

## 🔗 Enlaces Útiles

- [Pandas Time Series Documentation](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Scikit-Learn Time Series](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
- [Forecasting Best Practices](https://otexts.com/fpp2/)

## 📝 Notas Importantes

1. **Cuidado con el data leakage**: No uses información futura para predecir el pasado
2. **Validación temporal**: Siempre usa los datos más recientes como test
3. **Features estacionarias**: Muchos modelos requieren series estacionarias
4. **Múltiples pasos adelante**: El error crece al predecir múltiples períodos
5. **Recuerda diferenciar**: Si la serie no es estacionaria, diferencia antes de modelar
- Nomenclatura significativa

## 💡 Principios Clave de Clustering

### 1. Escalado es Obligatorio
```python
# ❌ Malo: K-Means con escala inconsistente
kmeans.fit(X)

# ✅ Bien: Primero escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans.fit(X_scaled)
```

### 2. K Nunca es Obvio
```python
# ❌ Malo: Asumir K=3 sin validación
kmeans = KMeans(n_clusters=3)

# ✅ Bien: Probar múltiples K y elegir por Silhouette
silhouette_scores = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k)
    score = silhouette_score(X_scaled, kmeans.fit_predict(X_scaled))
    silhouette_scores.append(score)
best_k = np.argmax(silhouette_scores) + 2
```

### 3. PCA Pierde Información
```python
# Siempre verifica varianza explicada
print(f"Varianza: {pca.explained_variance_ratio_.sum():.2%}")
# Si es < 80%, considera más componentes o verifica datos
```

### 4. Clusters Necesitan Interpretación
No es suficiente obtener 3 clusters. Debes:
- Describir cada cluster
- Asignar un nombre significativo
- Identificar acciones de negocio

## 🏆 Criterios de Éxito

Al completar esta parte, podrás:

- [ ] Explicar por qué clustering es diferente a clasificación
- [ ] Entrenar K-Means con diferentes valores de K
- [ ] Calcular e interpretar Silhouette Score
- [ ] Usar PCA para visualización
- [ ] Nombrar clusters significativamente
- [ ] Proponer acciones para cada segmento

## 📊 Flujo Típico de Clustering

```
1. CARGA y EXPLORACIÓN
   ↓
2. PREPROCESAMIENTO: Limpieza, imputación, escalado
   ↓
3. SELECCIÓN DE K: Método del codo, Silhouette
   ↓
4. ENTRENAMIENTO: K-Means con K óptimo
   ↓
5. VISUALIZACIÓN: PCA en 2D
   ↓
6. PERFILADO: Estadísticas por cluster
   ↓
7. NOMENCLATURA: Nombres significativos
   ↓
8. ACCIONES: Estrategias por segmento
```

## 🎨 Métrica de Selección de K: Elbow + Silhouette

**Método del Codo (Elbow)**:
```
Inercia (suma distancias dentro clusters)
    ^
    |      ___
    |    /
    |  /      ← "Codo" aquí = K óptimo
    |/
    |________> K
```

**Silhouette Score**:
```
Silhouette
    ^
  1 |     o
    |    o o o
0.7 |   o     o  ← Busca máximo aquí
    |  o       o
    | o
  0 |
    |________> K
```

**Recomendación**: Usa ambas métricas. Si concuerdan en K, excelente. Si discrepan, usa dominio empresarial.

## 📖 Materiales de Referencia

Consulta la carpeta `docs/` para obtener:
- Guía rápida de scikit-learn clustering
- Código template para Silhouette
- Interpretación de PCA
- Casos prácticos resueltos

---

**Profesor**: Unidad de Ciencia de Datos  
**Nivel**: Intermediate  
**Duración estimada**: 4-5 horas  
**Requisitos**: Completar Bloques 1-3
