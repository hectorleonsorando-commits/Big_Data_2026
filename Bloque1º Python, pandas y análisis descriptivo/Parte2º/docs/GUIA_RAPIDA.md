# Guía Rápida - Bloque 1 Parte 2

## 🎯 Objetivo General

Al finalizar esta parte, dominarás **técnicas avanzadas de manipulación, agregación y visualización de datos**, permitiéndote realizar análisis multidimensionales y descubrir patrones complejos en datasets grandes.

## 📚 Contenidos Específicos

### 1. Manipulación Avanzada con Pandas
- **GroupBy avanzado**: Agrupamientos múltiples, funciones custom en `agg()`
- **Pivotes y melt**: Reestructuración de datos de forma amplia a larga y viceversa
- **Joins y merges**: Combinación de múltiples fuentes con `merge()`, `join()`, `concat()`
- **Duplicación y deduplicación**: Estrategias complejas de limpieza
- **Ordenamiento multidimensional**: `sort_values()` con múltiples criterios

### 2. Análisis de Correlación y Relaciones
- **Matriz de correlaciones**: Pearson, Spearman, Kendall
- **Covarianza**: Interpretación y aplicación
- **Análisis bivariante**: Relaciones entre pares de variables
- **Identificación de multicolinealidad**
- **Visualización de dependencias**: Scatter plots, regressions plots

### 3. Limpieza Avanzada de Datos
- **Detección de outliers**: Z-score, IQR, métodos robustos
- **Tratamiento de outliers**: Winsorización, transformaciones log
- **Transformaciones no lineales**: Log, raíz cuadrada, potencias
- **Normalización y estandarización**: Escalado min-max, z-score
- **Manejo de desbalances**: En categorías y eventos

### 4. Segmentación y Perfiles
- **Análisis por grupos**: Patrones en subconjuntos
- **Segmentación de clientes**: RFM, cohortes, clustering descriptivo
- **Comparación de perfiles**: Tablas cross-tab, chi-cuadrado descriptivo
- **Análisis de tendencias**: Evolución temporal de segmentos

### 5. Visualización Avanzada
- **Heatmaps**: Correlaciones y patrones complejos
- **Violin plots y ridge plots**: Distribuciones por grupo
- **Scatter plots multidimensionales**: Con tamaño y color como variables
- **Faceted plots**: Múltiples gráficos en una grilla
- **Visualización de series temporales multivariantes**
- **Dashboards simples**: Múltiples visualizaciones coordinadas

### 6. Reportes Automatizados
- **Documentación de hallazgos**: Markdown + código ejecutable
- **Generación de tablas de resumen**: Formatos claros y profesionales
- **Conclusiones iterativas**: De hechos numéricos a interpretación
- **Documentación de metodología**: Reproducibilidad y auditoría

## 📋 Tareas Prácticas Esperadas

1. **Análisis multidimensional**: Ventas cruzadas por región, categoría y canal
2. **Perfiles de cliente**: Segmentación RFM con interpretación
3. **Detección de anomalías**: Identificación de transacciones atípicas
4. **Análisis de correlación**: Relaciones entre precio, cantidad e importe
5. **Tendencias temporales**: Evolución de ventas y patrones estacionales
6. **Dashboard resumen**: Múltiples visualizaciones coordinadas

## ✅ Criterios de Éxito

Al finalizar, podrás:

- [ ] Manipular estructuras de datos complejas (pivotes, joins, reshapes)
- [ ] Calcular e interpretar correlaciones multivariantes
- [ ] Detectar y tratar outliers de forma sistemática
- [ ] Segmentar datos y comparar perfiles
- [ ] Crear visualizaciones multidimensionales claras
- [ ] Generar reportes automatizados reproducibles

## 🔗 Referencias Rápidas

```python
# GroupBy múltiple
df.groupby(['col1', 'col2']).agg({'col3': ['sum', 'mean']})

# Pivote
df.pivot_table(values='venta', index='region', columns='categoria', aggfunc='sum')

# Merge
merged = df1.merge(df2, on='clave', how='inner')

# Correlación
df.corr(method='pearson')

# Outliers (IQR)
Q1, Q3 = df[col].quantile([0.25, 0.75])
IQR = Q3 - Q1
outliers = (df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```

## 💡 Recomendaciones

1. **Revisa Bloque 1 Parte 1** antes de empezar: Los fundamentos son prerequisito
2. **Experimenta con múltiples transformaciones** antes de elegir la final
3. **Documenta cada decisión**: La limpieza y transformación debe ser trazable
4. **Comunica hallazgos claramente**: Los números sin contexto no sirven
