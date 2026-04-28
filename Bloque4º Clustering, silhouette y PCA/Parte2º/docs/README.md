# Documentación - Bloque 4, Parte 2

## Contenido de esta Carpeta

Materiales avanzados para clustering profesional y análisis de negocio.

## Archivos

### GUIA_RAPIDA.md
Referencia rápida de técnicas avanzadas:
- Clustering jerárquico
- Dendrogramas
- Métricas múltiples (Davies-Bouldin, Calinski-Harabasz)
- Feature importance en clustering
- Análisis ROI
- Propuestas de acción

### environment.yml y requirements.txt
Configuración del entorno

## Temas Avanzados

### Clustering Jerárquico
```python
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Calcular matriz de linkage
linkage_matrix = linkage(X_scaled, method='ward')

# Visualizar dendrograma
dendrogram(linkage_matrix)
plt.show()

# Clustering
agg = AgglomerativeClustering(n_clusters=3)
labels = agg.fit_predict(X_scaled)
```

### Davies-Bouldin Index
```python
from sklearn.metrics import davies_bouldin_score

# Menor es mejor
score = davies_bouldin_score(X_scaled, labels)
```

### Calinski-Harabasz Index
```python
from sklearn.metrics import calinski_harabasz_score

# Mayor es mejor
score = calinski_harabasz_score(X_scaled, labels)
```

### Feature Importance
```python
from scipy.stats import f_oneway

# F-statistic entre grupos para cada feature
for col in X.columns:
    groups = [X.loc[labels == i, col] for i in range(n_clusters)]
    f_stat, p_val = f_oneway(*groups)
    print(f"{col}: F={f_stat:.2f}, p={p_val:.4f}")
```

### Análisis ROI
```python
# Definir valor por cluster
cluster_revenue = df.groupby('cluster')['revenue'].sum()
cluster_size = df.groupby('cluster').size()
cluster_value_per_capita = cluster_revenue / cluster_size

print(f"Cluster 0: {cluster_value_per_capita[0]:.2f} por cliente")
print(f"Cluster 1: {cluster_value_per_capita[1]:.2f} por cliente")
print(f"Cluster 2: {cluster_value_per_capita[2]:.2f} por cliente")

# Estrategia de marketing diferenciada por cluster
marketing_budget_total = 100000
clusters_by_value = cluster_value_per_capita.sort_values(ascending=False)
distribution = clusters_by_value / clusters_by_value.sum()

for cluster, pct in distribution.items():
    budget = marketing_budget_total * pct
    print(f"Cluster {cluster}: ${budget:.0f}")
```

## Comparativa de Algoritmos

| Algoritmo | Ventajas | Desventajas | Cuándo |
|-----------|----------|------------|--------|
| **K-Means** | Rápido, simple | K fijo, outliers | General |
| **Jerárquico** | Dendrograma, flexible | Lento, N² memoria | Exploración |
| **DBSCAN** | Clusters arbitrarios | Parámetros difíciles | Outliers |
| **GMM** | Probabilístico, flexible | Lento | Datos complejos |

## Métricas de Decisión

```
SI Silhouette alto Y Davies-Bouldin bajo Y Calinski-Harabasz alto
├─ → Clustering excelente

SI Silhouette medio Y métricas discrepan
├─ → Usa conocimiento empresarial

SI Silhouette bajo
├─ → Los datos no tienen estructura clara
└─ → ¿Tiene sentido segmentar?
```

## Workflow Profesional

```
1. EXPLORACIÓN
   └─ Entender la pregunta de negocio

2. PREPARACIÓN
   ├─ Escalado
   └─ Selección de features

3. EXPERIM ENTACIÓN
   ├─ Probar múltiples K
   ├─ Probar múltiples algoritmos
   └─ Calcular todas las métricas

4. VALIDACIÓN TÉCNICA
   ├─ Silhouette
   ├─ Davies-Bouldin
   └─ Calinski-Harabasz

5. VALIDACIÓN EMPRESARIAL
   ├─ ¿Tiene sentido?
   ├─ ¿Puedo actuar diferenciado?
   └─ ¿Vale la pena?

6. ANÁLISIS PROFUNDO
   ├─ Feature importance
   ├─ Análisis de varianza
   └─ Perfil descriptivo

7. ROI
   ├─ Cuantificar valor de segmentación
   ├─ Diseñar estrategias
   └─ Proponer presupuesto

8. REPORTE
   └─ Comunicar a stakeholders
```

## Propuesta de Acción por Cluster

**Template:**
```
Cluster X: "[Nombre Significativo]"
├─ Tamaño: [N clientes, %]
├─ Ingresos: [$X millones, %]
├─ Características: [Describe]
├─ Estrategia: [Propuesta]
├─ Canales: [Email, SMS, etc.]
├─ Objetivo: [KPI medible]
└─ Presupuesto: [$X/cliente/año]
```

## Recursos Externos

- [Scipy Hierarchical Clustering](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Davies-Bouldin Index](https://en.wikipedia.org/wiki/Davies%E2%80%93Bouldin_index)
- [Calinski-Harabasz Index](https://en.wikipedia.org/wiki/Calinski%E2%80%93Harabasz_index)

## Debugging Avanzado

**Problema**: Métricas contradicen elección de K
- **Verificar**: ¿Los datos tienen estructura natural?
- **Decisión**: Usa validación empresarial

**Problema**: Dendrograma no tiene corte claro
- **Verificar**: La distancia es gradual
- **Decisión**: Prueba diferentes métodos de linkage

**Problema**: Feature importance poco diferenciador
- **Verificar**: Todas las features igual de importantes
- **Decisión**: Quizá los clusters no son robustos

---

**Nivel**: Advanced Intermediate  
**Duración estimada**: Referencia profesional
