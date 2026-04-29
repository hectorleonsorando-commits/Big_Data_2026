# GUIA_RAPIDA.md - Bloque 5, Parte 1: Series Temporales y Forecasting

## Referencia Rápida de Código

### 1. Carga e Indexación Temporal

```python
import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv('../data/demanda_diaria_mayo_2026.csv')

# Convertir a datetime y usar como índice
df['fecha'] = pd.to_datetime(df['fecha'])
df = df.sort_values('fecha').set_index('fecha')

# Visualizar
print(f"Rango: {df.index.min()} a {df.index.max()}")
print(f"Frecuencia: {df.index.inferred_freq}")
```

### 2. Crear Variables Rezagadas (Lags)

```python
# Lag_1: valor de hace 1 período
df['lag_1'] = df['demanda'].shift(1)

# Múltiples lags
for lag in [1, 7, 14, 30]:
    df[f'lag_{lag}'] = df['demanda'].shift(lag)

# ⚠️ Importante: Los primeros N valores serán NaN
df = df.dropna()
```

### 3. Medias Móviles (Rolling Windows)

```python
# Media móvil de 7 días
df['ma_7'] = df['demanda'].rolling(window=7).mean()

# Otras funciones rolling
df['std_7'] = df['demanda'].rolling(7).std()      # Desv. Típica
df['min_7'] = df['demanda'].rolling(7).min()      # Mínimo
df['max_7'] = df['demanda'].rolling(7).max()      # Máximo

# Shift + rolling (evita lookahead bias)
df['ma_7_prev'] = df['demanda'].shift(1).rolling(7).mean()
```

### 4. Features Temporales

```python
# Extraer componentes de fecha
df['dia_semana'] = df.index.dayofweek      # 0=Lunes, 6=Domingo
df['mes'] = df.index.month                  # 1-12
df['trimestre'] = df.index.quarter          # 1-4
df['semana'] = df.index.isocalendar().week  # 1-52
df['dia_mes'] = df.index.day                # 1-31

# Indicadores
df['es_fin_semana'] = df['dia_semana'].isin([5, 6]).astype(int)
```

### 5. Split Temporal (CORRECTO)

```python
# ❌ INCORRECTO: Random split (data leakage en series temporales)
# X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# ✓ CORRECTO: Split temporal
n = len(df)
train_size = int(n * 0.8)

train = df.iloc[:train_size]
test = df.iloc[train_size:]

X_train = train[features]
y_train = train['demanda']

X_test = test[features]
y_test = test['demanda']

print(f"Train: {train.index.min()} a {train.index.max()}")
print(f"Test: {test.index.min()} a {test.index.max()}")
```

### 6. Baseline Ingenuo (Naive Forecast)

```python
from sklearn.metrics import mean_absolute_error

# Predicción: el valor anterior
baseline_pred = test['lag_1']

# Evaluar
mae_baseline = mean_absolute_error(y_test, baseline_pred)
print(f"Baseline MAE: {mae_baseline:.2f}")
```

### 7. Random Forest para Forecasting

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Preparar features
features = ['dia_semana', 'mes', 'lag_1', 'lag_7', 'lag_14', 'ma_7']
X_train = train[features]
X_test = test[features]

# Entrenar
modelo = RandomForestRegressor(n_estimators=200, random_state=42)
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Evaluar
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")
```

### 8. Importancia de Features

```python
import matplotlib.pyplot as plt

# Extraer importancias
importancias = pd.DataFrame({
    'feature': features,
    'importancia': modelo.feature_importances_
}).sort_values('importancia', ascending=False)

# Visualizar top 10
plt.barh(importancias['feature'][:10], importancias['importancia'][:10])
plt.title('Top 10 Features Más Importantes')
plt.xlabel('Importancia')
plt.show()
```

## ⚠️ Errores Comunes

1. **Data Leakage**: Usar información futura
   ```python
   # ❌ MAL: Rolling sin shift
   df['ma_7'] = df['demanda'].rolling(7).mean()  # Incluye valor actual
   
   # ✓ BIEN: Shift primero
   df['ma_7'] = df['demanda'].shift(1).rolling(7).mean()
   ```

2. **Random Split en Series Temporales**
   ```python
   # ❌ MAL
   X_train, X_test = train_test_split(X, test_size=0.2)
   
   # ✓ BIEN
   train = X[:int(len(X)*0.8)]
   test = X[int(len(X)*0.8):]
   ```

3. **NaN en Features**
   ```python
   # Los lags y rolling crean NaN al inicio
   df = df.dropna()  # Fundamental
   ```
    silhouettes.append(silhouette_score(X_scaled, labels))

# Visualizar
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Elbow plot
axes[0].plot(k_values, inertias, 'bo-')
axes[0].set_xlabel('K')
axes[0].set_ylabel('Inercia')
axes[0].set_title('Método del Codo')

# Silhouette plot
axes[1].plot(k_values, silhouettes, 'ro-')
axes[1].set_xlabel('K')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Score por K')

plt.tight_layout()
plt.show()

# 4. ELEGIR K ÓPTIMO
best_k = k_values[np.argmax(silhouettes)]
print(f"K óptimo: {best_k}")
print(f"Silhouette Score: {max(silhouettes):.3f}")

# 5. ENTRENAR MODELO FINAL
kmeans_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df['cluster'] = kmeans_final.fit_predict(X_scaled)

# 6. VISUALIZAR CON PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Varianza explicada: {pca.explained_variance_ratio_.sum():.2%}")

plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], 
                     cmap='viridis', alpha=0.6, s=50)
plt.colorbar(scatter, label='Cluster')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
plt.title('Clusters visualizados con PCA')
plt.show()

# Añadir componentes para referencia
df['PC1'] = X_pca[:, 0]
df['PC2'] = X_pca[:, 1]

# 7. PERFILAR CLUSTERS
print("\n=== PERFIL DE CLUSTERS ===\n")
profiles = df.groupby('cluster')[X.columns].mean()
print(profiles)

# 8. TAMAÑO Y COMPOSICIÓN
print("\n=== COMPOSICIÓN ===\n")
print(df['cluster'].value_counts().sort_index())
print("\nPorcentajes:")
print(df['cluster'].value_counts(normalize=True).sort_index() * 100)
```

## Escalado - ¿Cuándo y Por Qué?

```python
# ❌ MALO: Sin escalar
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
# Problema: Variables con rango 0-100,000 dominan sobre 0-1

# ✅ BIEN: StandardScaler (media=0, std=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scaled)

# ALTERNATIVA: MinMaxScaler (rango 0-1)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

## Silhouette Score - Interpretación

```python
from sklearn.metrics import silhouette_score, silhouette_samples

# Score global
overall_silhouette = silhouette_score(X_scaled, labels)
print(f"Silhouette Score Global: {overall_silhouette:.3f}")

# Scores individuales
silhouette_vals = silhouette_samples(X_scaled, labels)

# Por cluster
for i in range(best_k):
    cluster_silhouette = silhouette_vals[labels == i].mean()
    print(f"Cluster {i}: {cluster_silhouette:.3f}")

# Visualizar silhouette plot
plt.figure(figsize=(8, 6))
y_lower = 10

for i in range(best_k):
    cluster_silhouette_vals = silhouette_vals[labels == i]
    cluster_silhouette_vals.sort()
    
    size_cluster_i = cluster_silhouette_vals.shape[0]
    y_upper = y_lower + size_cluster_i
    
    plt.fill_betweenx(np.arange(y_lower, y_upper),
                      0, cluster_silhouette_vals,
                      label=f'Cluster {i}')
    y_lower = y_upper + 10

plt.xlabel("Silhouette Coefficient")
plt.ylabel("Cluster")
plt.axvline(x=overall_silhouette, color="red", linestyle="--", label='Average')
plt.legend()
plt.title("Silhouette Plot")
plt.show()
```

## PCA - Entender la Varianza

```python
from sklearn.decomposition import PCA

# 2 componentes
pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)

print(f"Varianza PC1: {pca_2d.explained_variance_ratio_[0]:.2%}")
print(f"Varianza PC2: {pca_2d.explained_variance_ratio_[1]:.2%}")
print(f"Total: {pca_2d.explained_variance_ratio_.sum():.2%}")

# 3 componentes si quieres más detalle
pca_3d = PCA(n_components=3)
pca_3d.fit(X_scaled)
cumsum = np.cumsum(pca_3d.explained_variance_ratio_)
print(f"Varianza acumulada (3D): {cumsum[-1]:.2%}")

# Graficar varianza acumulada
plt.figure()
plt.plot(range(1, len(cumsum) + 1), cumsum, 'bo-')
plt.xlabel('Número de componentes')
plt.ylabel('Varianza acumulada')
plt.title('Varianza explicada por PCA')
plt.axhline(y=0.8, color='r', linestyle='--', label='80% varianza')
plt.legend()
plt.show()
```

## Cluster Profiling - Estadísticas Descriptivas

```python
# Perfiles medios
profiles_mean = df.groupby('cluster')[X.columns].mean()

# Perfiles con desv. est.
profiles_std = df.groupby('cluster')[X.columns].std()

# Combinado
for col in X.columns:
    print(f"\n{col}:")
    for cluster in range(best_k):
        mean = profiles_mean.loc[cluster, col]
        std = profiles_std.loc[cluster, col]
        print(f"  Cluster {cluster}: {mean:.2f} ± {std:.2f}")

# Visualizar con heatmap
import seaborn as sns

# Normalizar para mejor visualización
profiles_normalized = (profiles_mean - profiles_mean.min()) / \
                      (profiles_mean.max() - profiles_mean.min())

plt.figure(figsize=(12, 4))
sns.heatmap(profiles_normalized.T, annot=profiles_mean.T.round(0), 
            fmt='g', cmap='RdYlGn', cbar_kws={'label': 'Intensidad'})
plt.title('Perfiles de Clusters (Normalizado)')
plt.xlabel('Cluster')
plt.show()
```

## Nomenclatura de Clusters - Asignar Nombres Significativos

```python
def name_clusters(profiles):
    """Asigna nombres basados en características"""
    names = {}
    
    for cluster_id in profiles.index:
        profile = profiles.loc[cluster_id]
        
        # Lógica para asignar nombres
        if profile['compras_12m'] > profiles['compras_12m'].mean():
            if profile['ticket_medio'] > profiles['ticket_medio'].mean():
                names[cluster_id] = "Premium / VIP"
            else:
                names[cluster_id] = "Frecuente / Regular"
        else:
            if profile['dias_desde_ultima_compra'] > profiles['dias_desde_ultima_compra'].mean():
                names[cluster_id] = "Inactivo / En Riesgo"
            else:
                names[cluster_id] = "Ocasional"
    
    return names

# Aplicar
cluster_names = name_clusters(profiles_mean)
print(cluster_names)

# Agregar al dataframe
df['cluster_name'] = df['cluster'].map(cluster_names)
```

## Errores Comunes

### ❌ No Escalar
```python
# RESULTADO: Variables con mayor escala dominan
kmeans.fit(X)  # MALO

# CORRECCIÓN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans.fit(X_scaled)  # BIEN
```

### ❌ No Validar K
```python
# RESULTADO: K elegido arbitrariamente
kmeans = KMeans(n_clusters=5)

# CORRECCIÓN
# Probar múltiples K y elegir por Silhouette
for k in range(2, 10):
    score = silhouette_score(X_scaled, KMeans(n_clusters=k).fit_predict(X_scaled))
```

### ❌ Ignorar Varianza de PCA
```python
# RESULTADO: Información perdida en visualización
pca = PCA(n_components=2)
pca.fit(X_scaled)

# VERIFICAR SIEMPRE
print(f"Varianza: {pca.explained_variance_ratio_.sum():.2%}")
# Si < 75%, considera 3 componentes o verifica datos
```

## Ejemplo Real - Segmentación de Clientes

```python
# Dataset: 1000 clientes con compras, recencia, frecuencia

df = pd.read_csv('clientes.csv')

# Features para clustering
features = ['compras_12m', 'ticket_medio', 'visitas_web', 
            'dias_desde_ultima_compra', 'antigüedad']

X = df[features].copy()

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elegir K
best_silhouette = 0
best_k = 2
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    score = silhouette_score(X_scaled, kmeans.fit_predict(X_scaled))
    if score > best_silhouette:
        best_silhouette = score
        best_k = k

print(f"K óptimo: {best_k}, Silhouette: {best_silhouette:.3f}")

# Clustering final
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Visualizar
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], cmap='viridis')
plt.title(f'Clustering de Clientes (K={best_k})')
plt.show()

# Perfilar
print(df.groupby('cluster')[features].mean())
```

---

**Uso**: Copia y adapta los templates a tu dataset  
**Nivel**: Beginner to Intermediate
