# Bloque 4 - Parte 1: Introducción a Clustering - K-Means, Silhouette y PCA

## 📚 Introducción Profesional

Bienvenidos al Bloque 4, donde hacemos la transición fundamental del **aprendizaje supervisado** al **aprendizaje no supervisado**. Hasta ahora, siempre tuvimos etiquetas que nos decían: "Este cliente es churn" o "Esta transacción es fraude". 

Ahora nos enfrentamos a un nuevo escenario: **¿Y si queremos descubrir patrones sin saber qué estamos buscando?**

### El Cambio Paradigmático

**Aprendizaje Supervisado (Bloques 1-3)**:
- Tienes etiquetas (y)
- Preguntas: "¿Quién churnará?" 
- Evaluación: Métricas conocidas (AUC, F1, etc.)

**Aprendizaje No Supervisado (Bloque 4)**:
- No tienes etiquetas
- Preguntas: "¿Quiénes son mis clientes realmente?"
- Evaluación: Más subjetiva, necesita validación empresarial

### ¿Por Qué es Crucial Clustering?

**Casos de uso reales:**
1. **Segmentación de clientes**: Identificar grupos para marketing diferenciado
2. **Recomendaciones**: Netflix agrupa películas, Amazon agrupa productos
3. **Detección de anomalías**: Transacciones que no pertenecen a ningún cluster
4. **Biología**: Análisis genómico, proteómica
5. **Astronomía**: Clasificación de objetos celestes
6. **Marketing**: Crear perfiles de audiencia para campañas dirigidas

## 📋 El Problema que Resolvemos

Imagina que tienes 10,000 clientes y quieres:
- Conocer perfiles de cliente diferentes
- Ofrecer productos específicos a cada segmento
- Optimizar recursos de marketing
- Identificar clientes en riesgo vs VIP

**Sin clustering**: Tratas a todos igual (ineficiente)  
**Con clustering**: Estrategias personalizadas por segmento (ROI optimizado)

## 🎯 Conceptos Fundamentales

### 1. K-Means: El Algoritmo más Popular

**Idea Simple**:
1. Elige K (número de clusters)
2. Selecciona K puntos aleatorios como centros
3. Asigna cada punto al centro más cercano
4. Recalcula los centros
5. Repite hasta convergencia

**Ventajas:**
- Simple de entender e implementar
- Rápido (O(n*k*i), donde i es número de iteraciones)
- Funciona bien en espacios Euclidianos

**Desventajas:**
- Necesitas especificar K de antemano
- Sensible a outliers
- Asume clusters esféricos
- Puede converger a óptimo local, no global

```python
from sklearn.cluster import KMeans

# Entrenar modelo
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)
```

### 2. Silhouette Score: ¿Cuántos Clusters?

**El dilema**: ¿Cuántos clusters debo usar? ¿3? ¿5? ¿10?

**Silhouette responde**: Mide qué tan bien los puntos encajan en sus clusters.

**Matemáticamente**:
```
s(i) = (b(i) - a(i)) / max(a(i), b(i))

donde:
- a(i): Distancia promedio a otros puntos en el mismo cluster (cohesión)
- b(i): Distancia promedio al cluster más cercano (separación)
```

**Interpretación**:
- Silhouette = 1: Perfecto (punto bien asignado)
- Silhouette = 0: Ambiguo (punto en la frontera)
- Silhouette = -1: Pésimo (punto asignado al cluster equivocado)
- **Score promedio > 0.7**: Excelente clustering
- **Score promedio > 0.5**: Aceptable
- **Score promedio < 0.3**: Clustering débil

### 3. PCA: Visualización en 2D/3D

**El Problema**: Tienes 50 features (dimensiones). ¿Cómo visualizar?

**La Solución - PCA (Principal Component Analysis)**:
- Reduce dimensiones manteniendo máxima varianza
- Encuentra nuevas direcciones que capturan la información
- Permite visualizar clusters en 2D o 3D

**Concepto clave**:
```
PC1 = Dirección de máxima varianza
PC2 = Dirección ortogonal de siguiente mayor varianza
PC3 = ...
```

**Interpretación de varianza explicada**:
- Si PC1 + PC2 explican 85% de varianza → Pérdida aceptable
- Si PC1 + PC2 explican 50% de varianza → Probablemente necesites más dimensiones

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
print(f"Varianza explicada: {pca.explained_variance_ratio_.sum()}")
```

## 📁 Estructura del Proyecto

```
Parte1º/
├── notebooks/              # Ejercicios: enunciado y soluciones
├── data/                   # Dataset de segmentación
├── docs/                   # Guías y referencias
├── requirements.txt        # Dependencias
├── environment.yml         # Entorno conda
└── README.md              # Este archivo
```

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
conda activate big_data_bloque4_parte1
jupyter lab
```

## 📚 Contenido de los Notebooks

### Enunciado
Preguntas a resolver:
1. Carga el dataset de segmentación
2. Escala las features
3. Experimenta con K-Means para diferentes valores de K
4. Calcula Silhouette Score para cada K
5. Visualiza clusters usando PCA
6. Interpreta el significado de cada cluster

### Resuelto
Soluciones profesionales que incluyen:
- Preprocesamiento correcto
- Método del codo + Silhouette
- Visualización con PCA
- Perfilado de clusters
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
