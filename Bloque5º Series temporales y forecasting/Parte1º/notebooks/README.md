# Notebooks - Bloque 4, Parte 1

## Descripción

Notebooks introductorios a clustering con K-Means, Silhouette y PCA.

## Notebooks Disponibles

### 04_Bloque_IV_Clustering_Fundamentals_ENUNCIADO.ipynb
**Propósito**: Ejercicios prácticos de clustering básico

Contiene:
1. Carga y exploración del dataset
2. Preprocesamiento y escalado
3. Experimentos con diferentes K
4. Cálculo de Silhouette Score
5. Visualización con PCA
6. Interpretación de clusters

**Recomendación**: Intenta resolver por tu cuenta antes de ver soluciones.

### 04_Bloque_IV_Clustering_Fundamentals_RESUELTO.ipynb
**Propósito**: Soluciones profesionales

Incluye:
1. Pipeline correcto de preprocesamiento
2. Método del codo + Silhouette
3. Visualización profesional con PCA
4. Perfilado de clusters
5. Nomenclatura significativa
6. Interpretación empresarial

**Recomendación**: Consulta para comparar enfoques.

## Flujo de Trabajo Recomendado

```
1. Lee el notebook del enunciado
   ↓
2. Ejecuta celdas exploratorias
   ↓
3. Intenta resolver cada pregunta
   ↓
4. Consulta GUIA_RAPIDA.md si necesitas ayuda de código
   ↓
5. Compara con soluciones
   ↓
6. Experimenta con variaciones
```

## Temas Cubiertos

- ✅ Carga de datos unsupervised
- ✅ Escalado (StandardScaler, MinMaxScaler)
- ✅ K-Means clustering
- ✅ Método del codo
- ✅ Silhouette Score
- ✅ PCA para visualización 2D
- ✅ Interpretación de clusters

## Consejos para Aprender

1. **Entiende la pregunta**: ¿Qué queremos descubrir?
2. **Explora primero**: EDA antes de modelar
3. **Experimenta**: Prueba diferentes K
4. **Visualiza**: Los gráficos revelan patrones
5. **Interpreta**: ¿Qué significa cada cluster?

## Errores Comunes

❌ **No escalar**
```python
# ❌ Malo
kmeans.fit(X)

# ✅ Bien
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans.fit(X_scaled)
```

❌ **No verificar varianza de PCA**
```python
# ✅ Siempre verifica
print(f"Varianza explicada: {pca.explained_variance_ratio_.sum():.2%}")
```

❌ **Asumir K sin validación**
```python
# ❌ Malo
kmeans = KMeans(n_clusters=3)

# ✅ Bien
# Probar múltiples K y elegir por Silhouette
```

## Dificultad Progresiva

### Nivel 1: Básico
- Cargar datos
- Escalar
- K-Means simple
- Visualizar

### Nivel 2: Intermedio
- Probar múltiples K
- Calcular Silhouette
- Comparar resultados
- Elegir K óptimo

### Nivel 3: Avanzado
- PCA interpretation
- Feature analysis
- Cluster profiling
- Business insights

---

**Duración estimada**: 3-4 horas  
**Nivel**: Beginner to Intermediate  
**Requisitos**: Bloques 1-3 completados
