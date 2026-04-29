# Bloque 4 - Parte 2: Clustering Avanzado - Análisis de Mercado Multinivel

## 📚 Introducción Profesional

En la Parte 1 aprendiste **qué es clustering** y **cómo hacerlo con K-Means**. En la Parte 2 llevaremos la segmentación al nivel profesional empresarial.

### Del Clustering al Negocio

**Parte 1**: "Estos son mis 3 clusters"  
**Parte 2**: "Cluster A representa $2M anuales, necesita estrategia premium. Cluster B representa riesgo de churn, necesita retención..."

### Lo Que Haremos

1. **Análisis multidimensional**: Segmentación en múltiples contextos
2. **Validación empresarial**: ¿Tienen sentido los clusters para negocio?
3. **Clustering jerárquico**: Alternativa a K-Means
4. **Análisis de características**: Qué hace único cada cluster
5. **ROI de segmentación**: Cuantificar el valor del clustering
6. **Acciones específicas**: Estrategias diferenciadas por segmento

## 📋 Conceptos Avanzados

### 1. Validación Empresarial de Clusters

No es suficiente que Silhouette Score sea 0.8. Debes preguntarte:
- ¿Los clusters reflejan realidades de negocio?
- ¿Puedo justificar estrategias diferentes para cada cluster?
- ¿El esfuerzo de segmentación vale la pena?

**Caso Real**:
```
K-Means encontró 4 clusters con Silhouette=0.75
Pero al analizar:
- Cluster 1: Clientes jóvenes, online, sensibles a precio
- Cluster 2: Profesionales, omnichannel, alto valor
- Cluster 3: Estudiantes, bajo valor
- Cluster 3 = 2% de clientes

Decisión: 3 clusters son suficientes, no 4
```

### 2. Clustering Jerárquico

**K-Means problema**: Debes especificar K de antemano

**Clustering Jerárquico solución**: Crea un "árbol" de clusters

**Dos enfoques**:
- **Aglomerativo** (bottom-up): Comienza con N clusters (1 por punto), los merge
- **Divisivo** (top-down): Comienza con 1 cluster grande, los divide

**Dendrograma**: Visualización tipo árbol que muestra distancias

```python
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Clustering jerárquico
linkage_matrix = linkage(X_scaled, method='ward')
dendrogram(linkage_matrix)
plt.show()

# O directo con sklearn
agg = AgglomerativeClustering(n_clusters=3)
labels = agg.fit_predict(X_scaled)
```

### 3. Métricas de Validación Interna

**Silhouette Score** (ya conoces)

**Davies-Bouldin Index**: 
- Mide ratio similaridad intra-cluster / separación inter-cluster
- Menor es mejor
- Rango típico: 0.5 - 3.0

```python
from sklearn.metrics import davies_bouldin_score
score = davies_bouldin_score(X_scaled, labels)
```

**Calinski-Harabasz Index**:
- Ratio varianza entre clusters / varianza dentro clusters
- Mayor es mejor

```python
from sklearn.metrics import calinski_harabasz_score
score = calinski_harabasz_score(X_scaled, labels)
```

### 4. Feature Importance en Clustering

¿Cuáles son las variables más importantes para formar clusters?

```python
# Calcular correlación entre features y cluster assignment
from scipy.stats import f_oneway

importances = []
for feature in X.columns:
    groups = [X.loc[labels == i, feature] for i in range(n_clusters)]
    f_stat, p_val = f_oneway(*groups)
    importances.append(f_stat)

# Normalizar
importances = np.array(importances) / np.sum(importances)
```

### 5. Análisis ROI de Segmentación

**La pregunta fundamental**: "¿Vale la pena segmentar?"

```
Estrategia 1: Sin segmentación
- Costo marketing: $100k
- Revenue: $1M
- ROI: 10x

Estrategia 2: Con segmentación en 3 clusters
- Costo marketing: $110k (más complejo)
- Revenue: $1.3M (mejor targeting)
- ROI: 11.8x
- Delta: +18% ROI con 10% de costo adicional → ¡Vale la pena!
```

### 6. Acciones Específicas por Cluster

No es suficiente describir. Debes actuar.

```
Cluster "High Value" (20% clientes, 65% revenue)
├─ Estrategia: Premium engagement
├─ Canales: VIP account manager, eventos exclusivos
├─ Objetivo: Retención 98%, upsell 5x/año
└─ Presupuesto: $500/cliente/año

Cluster "Transactional" (50% clientes, 30% revenue)
├─ Estrategia: Automated engagement
├─ Canales: Email/SMS, self-service
├─ Objetivo: Retención 75%, cross-sell 2x/año
└─ Presupuesto: $50/cliente/año

Cluster "Risky" (30% clientes, 5% revenue)
├─ Estrategia: Reactivation campaigns
├─ Canales: Targeted offers, win-back campaigns
├─ Objetivo: Retención 50%, reactivate 10%
└─ Presupuesto: $100/cliente/año
```

## 📁 Estructura del Proyecto

```
Parte2º/
├── notebooks/              # Ejercicios avanzados
├── data/                   # Datasets complejos
├── docs/                   # Referencias avanzadas
├── requirements.txt        # Dependencias
├── environment.yml         # Entorno conda
└── README.md              # Este archivo
```

## 🚀 Cómo Empezar

### Opción 1: Usando pip (recomendado para Windows)
```bash
cd Parte2º
pip install -r requirements.txt
jupyter lab
```

### Opción 2: Usando Conda
```bash
cd Parte2º
conda env create -f environment.yml
conda activate big_data_bloque4_parte2
jupyter lab
```

## 📚 Contenido de los Notebooks

### Enunciado
Problemas a resolver:
1. Realiza clustering con múltiples métricas
2. Valida clusters desde perspectiva empresarial
3. Prueba clustering jerárquico
4. Analiza importancia de features
5. Calcula ROI de segmentación
6. Diseña acciones por cluster

### Resuelto
Incluye:
- Comparación K-Means vs Jerárquico
- Múltiples métricas de validación
- Análisis ROI
- Propuestas de acción concreta

## 💡 Cómo Piensa el Profesional de Datos

**Pregunta Junior**: "Mi Silhouette Score es 0.76, ¿está bien?"

**Respuesta Senior**: "Excelente métrica, pero ¿puedo segmentar de forma diferente? ¿Tiene sentido para Marketing? ¿Puedo implementar estrategias distintas? ¿Cuál es el ROI?"

**Lección**: Métricas técnicas ≠ Utilidad empresarial

## 🏆 Criterios de Éxito

Al completar esta parte, podrás:

- [ ] Comparar múltiples algoritmos de clustering
- [ ] Validar clusters con métricas múltiples
- [ ] Interpretar dendrogramas (clustering jerárquico)
- [ ] Analizar importancia de features en clustering
- [ ] Calcular ROI de segmentación
- [ ] Proponer acciones específicas por cluster
- [ ] Presentar hallazgos a stakeholders no-técnicos

## 📊 Workflow Profesional

```
1. EXPLORACIÓN: ¿Qué problemas puedo resolver con clustering?
   ↓
2. PREPARACIÓN: Escalado, selección de features
   ↓
3. EXPERIMENTACIÓN: Probar múltiples K y algoritmos
   ↓
4. VALIDACIÓN TÉCNICA: Silhouette, Davies-Bouldin, etc.
   ↓
5. VALIDACIÓN EMPRESARIAL: ¿Tiene sentido de negocio?
   ↓
6. PROFUNDIZACIÓN: Feature importance, ROI
   ↓
7. ACCIONES: Estrategias específicas
   ↓
8. MONITOREO: ¿Cómo evoluciona la segmentación?
```

## 🔍 Debugging Problemas Comunes

**Problema**: Clusters no hacen sentido empresarial
- **Verificar**: ¿Escalé correctamente? ¿Incluí variables no relevantes?
- **Solución**: Selección de features más cuidadosa

**Problema**: Silhouette alto pero clusters no interpretables
- **Verificar**: Tal vez los datos no tienen estructura natural
- **Solución**: Pregunta si clustering es el enfoque correcto

**Problema**: Diferentes K con diferentes métricas
- **Verificar**: Silhouette vs Elbow vs Davies-Bouldin en desacuerdo
- **Solución**: Usa conocimiento empresarial como desempate

---

**Profesor**: Unidad de Ciencia de Datos  
**Nivel**: Advanced Intermediate  
**Duración estimada**: 5-7 horas  
**Requisitos**: Completar Parte 1 del Bloque 4
