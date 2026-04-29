# Documentación - Bloque 4, Parte 1

## Contenido de esta Carpeta

Materiales de referencia para clustering fundamental.

## Archivos

### GUIA_RAPIDA.md
Referencia rápida de código para:
- Carga y exploración de datos unsupervised
- StandardScaler y MinMaxScaler
- K-Means clustering
- Método del codo
- Silhouette Score
- PCA para visualización 2D/3D
- Interpretación de clusters
- Perfilado de datos

### environment.yml y requirements.txt
Archivos de configuración del entorno

## Temas de Referencia

### Escalado
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: media=0, std=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# MinMaxScaler: rango [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

### K-Means
```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)
```

### Silhouette Score
```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X_scaled, labels)
# Rango: [-1, 1]
# > 0.7: Excelente
# > 0.5: Bueno
# < 0.3: Débil
```

### PCA
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Varianza explicada
print(pca.explained_variance_ratio_.sum())
```

## Método Recomendado

```
1. ESCALAR
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)

2. PROBAR MÚLTIPLES K
   for k in range(2, 10):
       kmeans = KMeans(n_clusters=k, ...)
       score = silhouette_score(X_scaled, kmeans.fit_predict(X_scaled))

3. ELEGIR K
   best_k = k_con_máximo_silhouette

4. ENTRENAR FINAL
   kmeans = KMeans(n_clusters=best_k, ...)
   labels = kmeans.fit_predict(X_scaled)

5. VISUALIZAR
   pca = PCA(n_components=2)
   X_pca = pca.fit_transform(X_scaled)
   plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)

6. PERFILAR
   df_profiles = df.groupby(labels).mean()
```

## Interpretación Rápida

### Silhouette Score
- **0.8-1.0**: Excelente, clusters bien definidos
- **0.5-0.8**: Bueno, clusters aceptables
- **0.3-0.5**: Débil, clusters ambiguos
- **<0.3**: Pobre, los datos no tienen estructura clara

### PCA Varianza
- **>85%**: Visualización 2D confiable
- **70-85%**: Aceptable, verifica relaciones
- **<70%**: Consideracuidadosamente, puede perderse info

### Método del Codo
```
El "codo" es donde la curva cambia de pendiente pronunciada a plana
Suele ser la mejor elección de K
```

## Recursos Externos

- [Scikit-learn KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Scikit-learn Silhouette](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
- [Scikit-learn PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

## Template Completo

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv('data.csv')
X = df.drop('id', axis=1)

# 2. Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Probar múltiples K
silhouettes = []
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    silhouettes.append(score)

# 4. Elegir K
best_k = np.argmax(silhouettes) + 2
print(f"Best K: {best_k}")

# 5. Entrenar
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 6. Visualizar con PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 6))
for c in range(best_k):
    mask = df['cluster'] == c
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], label=f'Cluster {c}', alpha=0.6)
plt.legend()
plt.title('Clustering with PCA Visualization')
plt.show()

# 7. Perfilar
print(df.groupby('cluster')[X.columns].mean())
```

---

**Nivel**: Beginner to Intermediate  
**Duración estimada**: Referencia rápida
