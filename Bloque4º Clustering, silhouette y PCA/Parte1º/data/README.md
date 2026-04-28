# Data - Bloque 4, Parte 1

## Descripción del Dataset

### segmentacion_clientes_mayo_2026.csv

Dataset sintético de segmentación de clientes de un negocio de retail/e-commerce.

**Estructura:**
- **N observaciones**: ~5,000 clientes
- **N features**: 12-15 variables

**Variables principales:**
- **Ingresos**: Ingreso anual del cliente
- **Compras_12m**: Monto gastado en últimos 12 meses
- **Ticket_medio**: Valor promedio de transacción
- **Visitas_web**: Número de visitas a sitio web
- **Días_desde_última_compra**: Recencia
- **Reclamaciones**: Número de reclamos presentados
- **Antigüedad**: Meses como cliente
- **Categorías_compradas**: Diversidad de categorías
- **Email_clicks**: Interacción con email marketing
- **Reseñas_dejadas**: Engagement con plataforma

**Características:**
- Sin variable target (es unsupervised)
- Variables numéricas (escala inconsistente)
- Relativamente completo (pocos valores faltantes)
- Estructura natural: probablemente existan clusters reales

**Distribuciones esperadas:**
- Algunos clientes VIP (alto gasto, alta frecuencia)
- Clientes regulares (gasto moderado)
- Clientes ocasionales (bajo gasto)
- Clientes en riesgo (alto recency, bajo gasto reciente)

## Uso en Notebooks

- **Exploración**: Análisis descriptivo, correlaciones
- **Clustering**: K-Means con diferentes K
- **Evaluación**: Silhouette Score, método del codo
- **Visualización**: PCA 2D
- **Interpretación**: Perfiles de clusters

## Notas

- **Escalado obligatorio**: Las variables tienen escalas muy diferentes
- **Selección de features**: Considera si usar todas las variables
- **Contexto**: Imagina estrategias reales de marketing para cada cluster
