# GUIA_RAPIDA.md - Bloque 4, Parte 2: Clustering Avanzado y Análisis ROI

## Clustering Jerárquico Aglomerativo

```python
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Calcular matriz de linkage
linkage_matrix = linkage(X_scaled, method='ward')

# Visualizar dendrograma
plt.figure(figsize=(12, 7))
dendrogram(linkage_matrix, 
           leaf_font_size=10,
           labels=df.index)
plt.axhline(y=10, color='r', linestyle='--', label='Corte sugerido')
plt.xlabel('Índice del cliente')
plt.ylabel('Distancia')
plt.title('Dendrograma de Clustering Jerárquico')
plt.legend()
plt.show()

# Métodos de linkage disponibles
# 'ward' (recomendado): minimiza varianza
# 'complete': distancia máxima entre clusters
# 'average': distancia promedio
# 'single': distancia mínima

# Clustering con K clusters específico
agg_clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = agg_clustering.fit_predict(X_scaled)

# Comparar con K-Means
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Ambigüedad: ¿Cuál es mejor?
silhouette_agg = silhouette_score(X_scaled, labels)
silhouette_kmeans = silhouette_score(X_scaled, kmeans_labels)

print(f"Silhouette (Jerárquico): {silhouette_agg:.3f}")
print(f"Silhouette (K-Means): {silhouette_kmeans:.3f}")
```

## Métricas Múltiples de Validación

```python
from sklearn.metrics import (silhouette_score, davies_bouldin_score, 
                            calinski_harabasz_score)

# Comparar múltiples K con diferentes métricas
results = []

for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    silhouette = silhouette_score(X_scaled, labels)
    davies_bouldin = davies_bouldin_score(X_scaled, labels)
    calinski_harabasz = calinski_harabasz_score(X_scaled, labels)
    
    results.append({
        'k': k,
        'silhouette': silhouette,
        'davies_bouldin': davies_bouldin,  # Menor mejor
        'calinski_harabasz': calinski_harabasz  # Mayor mejor
    })

results_df = pd.DataFrame(results)
print(results_df)

# Visualizar
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(results_df['k'], results_df['silhouette'], 'bo-')
axes[0].set_title('Silhouette (Mayor mejor)')
axes[0].set_xlabel('K')

axes[1].plot(results_df['k'], results_df['davies_bouldin'], 'ro-')
axes[1].set_title('Davies-Bouldin (Menor mejor)')
axes[1].set_xlabel('K')

axes[2].plot(results_df['k'], results_df['calinski_harabasz'], 'go-')
axes[2].set_title('Calinski-Harabasz (Mayor mejor)')
axes[2].set_xlabel('K')

plt.tight_layout()
plt.show()
```

## Feature Importance en Clustering

```python
from scipy.stats import f_oneway
import pandas as pd

# Para cada feature, calcular F-statistic
feature_importance = {}

for col in X.columns:
    groups = [X.loc[labels == i, col].values for i in range(best_k)]
    f_stat, p_value = f_oneway(*groups)
    feature_importance[col] = {'f_stat': f_stat, 'p_value': p_value}

importance_df = pd.DataFrame(feature_importance).T
importance_df = importance_df.sort_values('f_stat', ascending=False)

print(importance_df)

# Visualizar
plt.figure(figsize=(10, 6))
plt.barh(importance_df.index, importance_df['f_stat'])
plt.xlabel('F-Statistic (Mayor = Más importante para clustering)')
plt.title('Feature Importance en Clustering')
plt.show()

# Normalizar importancia
importance_normalized = importance_df['f_stat'] / importance_df['f_stat'].sum()
print("\nImportancia Normalizada:")
print(importance_normalized)
```

## Análisis de Varianza por Cluster

```python
# Estadísticas detalladas por cluster
for cluster_id in range(best_k):
    print(f"\n=== CLUSTER {cluster_id} ===")
    cluster_data = df[df['cluster'] == cluster_id]
    
    print(f"Tamaño: {len(cluster_data)} clientes ({len(cluster_data)/len(df)*100:.1f}%)")
    print(f"\nEstadísticas:")
    
    for col in X.columns:
        mean = cluster_data[col].mean()
        std = cluster_data[col].std()
        min_val = cluster_data[col].min()
        max_val = cluster_data[col].max()
        
        print(f"  {col}: {mean:.2f} ± {std:.2f} [{min_val:.0f}, {max_val:.0f}]")
```

## Cálculo de ROI de Segmentación

```python
# Asumir que cada cliente tiene un valor asociado
# Ejemplo: revenue, lifetime value, purchase frequency, etc.

# Definir métricas de valor
df['customer_value'] = df['compras_12m']  # O cualquier métrica
df['customer_class'] = pd.cut(df['customer_value'], 
                              bins=[0, df['customer_value'].quantile(0.33), 
                                    df['customer_value'].quantile(0.67), 
                                    df['customer_value'].max()],
                              labels=['Low', 'Medium', 'High'])

# Análisis por cluster
cluster_analysis = df.groupby('cluster').agg({
    'customer_value': ['sum', 'mean', 'count'],
    'customer_class': lambda x: (x == 'High').sum()  # Clientes High Value
}).round(2)

print("Análisis de Valor por Cluster:")
print(cluster_analysis)

# ROI de segmentación
print("\n=== ROI DE SEGMENTACIÓN ===")

# Costo base de marketing (sin segmentación)
marketing_budget = 100000

# Asignación uniforme (sin segmentación)
budget_uniform = marketing_budget / len(df)

# Asignación diferenciada (con segmentación)
cluster_value = df.groupby('cluster')['customer_value'].sum()
cluster_pct = cluster_value / cluster_value.sum()

print("\nSin segmentación:")
print(f"  Budget por cliente: ${budget_uniform:.2f}")
print(f"  ROI asumido: 2x")

print("\nCon segmentación (estrategia diferenciada):")
for cluster_id in range(best_k):
    budget_cluster = marketing_budget * cluster_pct[cluster_id]
    cluster_size = len(df[df['cluster'] == cluster_id])
    budget_per_customer = budget_cluster / cluster_size if cluster_size > 0 else 0
    
    # Asumir ROI diferenciado
    if cluster_pct[cluster_id] > 0.3:  # High value cluster
        roi_multiplier = 3
        print(f"  Cluster {cluster_id}: ${budget_per_customer:.2f}/cliente, ROI ~3x")
    elif cluster_pct[cluster_id] > 0.1:  # Medium
        roi_multiplier = 2
        print(f"  Cluster {cluster_id}: ${budget_per_customer:.2f}/cliente, ROI ~2x")
    else:  # Low
        roi_multiplier = 1.5
        print(f"  Cluster {cluster_id}: ${budget_per_customer:.2f}/cliente, ROI ~1.5x")

print("\nImpacto esperado: +30-40% en ROI general")
```

## Propuesta de Acción Estructurada

```python
# Template de estrategia por cluster

cluster_strategies = {}

for cluster_id in range(best_k):
    cluster_data = df[df['cluster'] == cluster_id]
    size = len(cluster_data)
    value = cluster_data['customer_value'].sum()
    
    # Características clave
    avg_recency = cluster_data['dias_desde_ultima_compra'].mean()
    avg_frequency = cluster_data['compras_12m'].mean()
    avg_value = cluster_data['ticket_medio'].mean()
    
    # Clasificación
    if value / len(df) > df['customer_value'].mean() * 0.5:
        segment = "HIGH VALUE"
        strategy = "Premium Engagement + Upsell"
        channels = "Dedicated Account Manager, VIP Events, Personalized Offers"
        objective = "Retention 95%+, Upsell 3x/year"
        budget_per_customer = 500
    elif avg_recency < 30:
        segment = "ACTIVE"
        strategy = "Retention + Cross-sell"
        channels = "Email, SMS, App Notifications"
        objective = "Retention 80%, Cross-sell 2x/year"
        budget_per_customer = 100
    else:
        segment = "AT RISK"
        strategy = "Win-back + Reactivation"
        channels = "Special Offers, Email Campaigns"
        objective = "Reactivate 20%, Retention 60%"
        budget_per_customer = 200
    
    cluster_strategies[cluster_id] = {
        'segment': segment,
        'size': size,
        'total_value': value,
        'pct_customers': size / len(df) * 100,
        'pct_value': value / df['customer_value'].sum() * 100,
        'strategy': strategy,
        'channels': channels,
        'objective': objective,
        'budget_per_customer': budget_per_customer,
        'total_budget': size * budget_per_customer
    }

# Mostrar resumen
summary_df = pd.DataFrame(cluster_strategies).T
print(summary_df[['segment', 'size', 'pct_value', 'strategy', 'total_budget']])
```

## Validación Empresarial de Clusters

```python
# Preguntas que debes responder:

validation_checklist = {
    "¿Los clusters tienen características claramente diferenciadas?": None,
    "¿Puedo proponer estrategias diferentes para cada cluster?": None,
    "¿El tamaño de cada cluster es manejable?": None,
    "¿Los clusters son estables en el tiempo?": None,
    "¿El ROI esperado justifica la complejidad?": None,
    "¿Pueden implementarse en sistemas reales?": None,
}

# Llenar respuestas
for question in validation_checklist:
    print(f"□ {question}")

# Si todas son YES → Procede con segmentación
# Si alguna es NO → Reconsider K o revisa datos
```

## Comparación de Algoritmos

```python
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler

algorithms = {
    'KMeans': KMeans(n_clusters=3, random_state=42, n_init=10),
    'Hierarchical': AgglomerativeClustering(n_clusters=3, linkage='ward'),
    'DBSCAN': DBSCAN(eps=0.5, min_samples=5)
}

comparison_results = {}

for name, algorithm in algorithms.items():
    labels = algorithm.fit_predict(X_scaled)
    
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    silhouette = silhouette_score(X_scaled, labels) if n_clusters > 1 else -1
    
    comparison_results[name] = {
        'n_clusters': n_clusters,
        'silhouette': silhouette,
        'labels': labels
    }

comparison_df = pd.DataFrame(comparison_results).T
print(comparison_df)

# Visualizar comparación
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for idx, (name, result) in enumerate(comparison_results.items()):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    axes[idx].scatter(X_pca[:, 0], X_pca[:, 1], c=result['labels'], cmap='viridis')
    axes[idx].set_title(f"{name} (K={result['n_clusters']}, Silhouette={result['silhouette']:.3f})")

plt.tight_layout()
plt.show()
```

---

**Uso**: Adapta a tu contexto empresarial  
**Nivel**: Advanced Intermediate
