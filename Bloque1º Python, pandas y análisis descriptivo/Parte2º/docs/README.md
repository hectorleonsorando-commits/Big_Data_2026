# 📚 Documentación Completa: Análisis Avanzado con Pandas (Parte 2)

## Introducción

Ahora que dominas los fundamentos, es tiempo de convertirte en un **maestro de la manipulación de datos**. En esta parte aprenderás técnicas que te permitirán trabajar con datasets complejos, descubrir patrones ocultos y crear análisis que impresionan a los stakeholders.

---

## 🎯 Objetivos

1. ✅ Dominar operaciones avanzadas de GroupBy y agregaciones complejas
2. ✅ Restructurar datos (pivots, melts) para diferentes perspectivas de análisis
3. ✅ Combinar múltiples fuentes de datos (joins, merges)
4. ✅ Detectar y tratar outliers de forma sistemática
5. ✅ Realizar análisis multivariante y correlaciones
6. ✅ Crear visualizaciones avanzadas que comunican patrones complejos
7. ✅ Automatizar reportes reproducibles

---

## 📖 Capítulo 1: GroupBy Avanzado

### Más Allá de la Media

En la Parte 1 aprendiste groupby básico. Ahora iremos más profundo:

```python
import pandas as pd
import numpy as np

df = pd.read_csv("../data/ventas_mayo_2026.csv")

# Agrupamiento multiple
resumen = df.groupby(['region', 'categoria']).agg({
    'importe': ['sum', 'mean', 'std', 'min', 'max'],
    'unidades': 'sum',
    'cliente_id': 'nunique'
})

print(resumen)
```

**¿Qué vemos aquí?**
- Agrupamos por DOS columnas simultáneamente
- Aplicamos múltiples funciones a la vez
- Obtenemos una vista multidimensional de los datos

### Funciones de Agregación Personalizadas

```python
# Función personalizada
def rango_percentil(x):
    """Calcula la amplitud del 90% central de datos"""
    return x.quantile(0.95) - x.quantile(0.05)

# Usar con agg
resumen = df.groupby('categoria')['importe'].agg([
    ('total', 'sum'),
    ('media', 'mean'),
    ('desviacion', 'std'),
    ('rango_central_90', rango_percentil)
])

print(resumen)
```

**Interpretación:**
- El rango del 90% central te dice cuánta variabilidad hay
- Ignora los extremos, lo que es útil para análisis robustos

### Transform: Operaciones que Mantienen Dimensionalidad

```python
# Problema: Quiero el PORCENTAJE de ventas por categoría respecto al total

# Forma manual (complicada)
total_por_region = df.groupby('region')['importe'].transform('sum')
df['porcentaje_del_total'] = (df['importe'] / total_por_region * 100)

# Alternativamente con transform
df['porcentaje_del_total'] = df.groupby('region')['importe'].transform(lambda x: x / x.sum() * 100)

print(df[['region', 'importe', 'porcentaje_del_total']].head(10))
```

**¿Por qué transform?**
- `groupby().agg()` reduce el tamaño de los datos
- `groupby().transform()` mantiene el número de filas
- Útil cuando quieres propagar agregaciones a cada fila

---

## 📖 Capítulo 2: Reshaping - Cambiar la Forma de los Datos

### Problema: Diferentes Perspectivas de los Mismos Datos

A menudo necesitas ver los mismos datos de diferentes formas:

```python
# Vista actual (formato LARGO)
print(df[['fecha', 'categoria', 'importe']].head())

# SALIDA:
#      fecha categoria  importe
# 0  2024-01-01   Electrónica     150
# 1  2024-01-01      Ropa      200
# 2  2024-01-02   Electrónica     180
# 3  2024-01-02   Alimentos     100
```

Pero a veces quieres una tabla así (formato ANCHO):

```python
# Vista pivotada
pivot_table = df.pivot_table(values='importe', index='fecha', columns='categoria', aggfunc='sum')
print(pivot_table)

# SALIDA:
# categoria    Alimentos  Electrónica  Ropa
# fecha
# 2024-01-01        100           150  200
# 2024-01-02        100           180  250
```

### Pivot Table: El Análisis Cruzado

```python
# Ejemplo completo: Ventas por región y categoría
pivot = df.pivot_table(
    values='importe',                 # Qué valores agregar
    index='region',                   # Filas
    columns='categoria',              # Columnas
    aggfunc='sum',                    # Cómo agregarlos
    margins=True                      # Incluir totales
)

print(pivot)

# Con múltiples agregaciones
pivot_multi = df.pivot_table(
    values=['importe', 'unidades'],
    index='region',
    columns='categoria',
    aggfunc={'importe': 'sum', 'unidades': 'mean'}
)
```

**Interpretación comercial:**
- ¿Cuál región vende más de cada categoría?
- ¿Hay especialización por región?
- Dónde debería enfocar recursos?

### Melt: Lo Opuesto a Pivot

```python
# Tienes datos en formato ancho
datos_ancho = pd.DataFrame({
    'Cliente': ['A', 'B', 'C'],
    'Enero': [100, 150, 200],
    'Febrero': [120, 140, 210],
    'Marzo': [110, 160, 195]
})

print("Datos iniciales (ANCHO):")
print(datos_ancho)

# Lo conviertes a formato largo
datos_largo = datos_ancho.melt(
    id_vars=['Cliente'],           # Columnas que mantienen su forma
    var_name='Mes',                # Nombre para los meses
    value_name='Ventas'            # Nombre para los valores
)

print("\nDatos transformados (LARGO):")
print(datos_largo)
```

---

## 📖 Capítulo 3: Joins y Merges - Combinando Datos

### El Escenario Real

Tienes dos tablas separadas:
- Tabla 1: Transacciones de venta
- Tabla 2: Información de clientes

Necesitas combinarlas:

```python
# Tabla de ventas
ventas = pd.DataFrame({
    'cliente_id': [1, 2, 3, 1, 2],
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'importe': [100, 150, 200, 120, 180]
})

# Tabla de clientes
clientes = pd.DataFrame({
    'cliente_id': [1, 2, 3, 4],
    'nombre': ['Ana', 'Braulio', 'Carmen', 'David'],
    'segmento': ['Premium', 'Regular', 'VIP', 'Regular']
})

print("Ventas:")
print(ventas)
print("\nClientes:")
print(clientes)

# Fusionar: INNER JOIN (solo clientes con ventas)
fusionado = ventas.merge(clientes, on='cliente_id', how='inner')
print("\nInner Join (coincidencias exactas):")
print(fusionado)
```

### Tipos de Join

```python
# 1. INNER JOIN: Solo registros que existen en ambas tablas
inner = ventas.merge(clientes, on='cliente_id', how='inner')
# Resultado: 5 filas (todas las ventas tienen cliente)

# 2. LEFT JOIN: Todos de la tabla izquierda + coincidencias
left = ventas.merge(clientes, on='cliente_id', how='left')
# Resultado: 5 filas (mantiene todas las ventas)

# 3. RIGHT JOIN: Todos de la tabla derecha + coincidencias
right = ventas.merge(clientes, on='cliente_id', how='right')
# Resultado: 4 filas (incluye clientes sin ventas)

# 4. OUTER JOIN: Todos los registros de ambas tablas
outer = ventas.merge(clientes, on='cliente_id', how='outer')
# Resultado: 6 filas (todas las ventas + cliente sin ventas)
```

**¿Cuándo usar cada uno?**
- **INNER**: Cuando quieres solo datos completos
- **LEFT**: Cuando quieres mantener todas las transacciones
- **RIGHT**: Cuando quieres todos los clientes (hayan comprado o no)
- **OUTER**: Cuando quieres auditoría completa

---

## 📖 Capítulo 4: Detección y Tratamiento de Outliers

### El Problema

Un cliente compró por $99,999 cuando el promedio es $500. ¿Es error o es real?

```python
# Visualizar distribución
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histograma
axes[0].hist(df['importe'], bins=50, color='steelblue')
axes[0].set_title('Distribución sin Escala')
axes[0].set_ylabel('Frecuencia')

# Boxplot
axes[1].boxplot(df['importe'])
axes[1].set_title('Boxplot - Ver Outliers')
axes[1].set_ylabel('Importe ($)')

plt.tight_layout()
plt.show()
```

### Método IQR (Rango Intercuartílico)

```python
# Calcular cuartiles
Q1 = df['importe'].quantile(0.25)
Q3 = df['importe'].quantile(0.75)
IQR = Q3 - Q1

print(f"Q1 (25%): {Q1}")
print(f"Q3 (75%): {Q3}")
print(f"IQR: {IQR}")

# Definir límites
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"\nLímites normales:")
print(f"Inferior: {limite_inferior}")
print(f"Superior: {limite_superior}")

# Identificar outliers
outliers = df[(df['importe'] < limite_inferior) | (df['importe'] > limite_superior)]
print(f"\nOutliers detectados: {len(outliers)}")
print(outliers.sort_values('importe', ascending=False).head())
```

### Decisiones sobre Outliers

```python
# Opción 1: Investigar primero
outliers_altos = df[df['importe'] > limite_superior]
print(f"Outliers altos: {len(outliers_altos)}")
print(outliers_altos[['cliente_id', 'categoria', 'importe']].head())

# Opción 2: Eliminar si son errores evidentes
df_sin_outliers = df[(df['importe'] >= limite_inferior) & (df['importe'] <= limite_superior)]
print(f"Registros antes: {len(df)}, después: {len(df_sin_outliers)}")

# Opción 3: Transformar para reducir efecto
df['importe_log'] = np.log1p(df['importe'])  # Log de (1 + valor)

# Opción 4: Winsorización (limitar extremos)
df['importe_winsorizado'] = df['importe'].clip(limite_inferior, limite_superior)
```

---

## 📖 Capítulo 5: Análisis de Correlación

### ¿Qué Es Correlación?

Dos variables están correlacionadas cuando cambian juntas:
- Si X sube, Y también sube (correlación positiva)
- Si X sube, Y baja (correlación negativa)
- No hay relación (sin correlación)

```python
# Matriz de correlación
corr_matrix = df[['importe', 'unidades', 'precio_unitario']].corr()
print(corr_matrix)

# Valores cercanos a 1: Correlación positiva fuerte
# Valores cercanos a -1: Correlación negativa fuerte  
# Valores cercanos a 0: Sin correlación
```

### Visualizar Correlaciones

```python
import seaborn as sns

# Heatmap de correlaciones
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Matriz de Correlación')
plt.show()

# Scatter plot para relación individual
plt.figure(figsize=(10, 6))
plt.scatter(df['unidades'], df['importe'], alpha=0.5)
plt.xlabel('Unidades Vendidas')
plt.ylabel('Importe de Venta ($)')
plt.title('Relación: Cantidad vs Importe')
plt.show()
```

---

## 📖 Capítulo 6: Análisis Multidimensional

### Segmentación RFM (Recency, Frequency, Monetary)

Es un método para clasificar clientes:

```python
from datetime import datetime, timedelta

# Fecha de referencia
fecha_ref = df['fecha'].max() + timedelta(days=1)

# Calcular RFM para cada cliente
rfm = df.groupby('cliente_id').agg({
    'fecha': lambda x: (fecha_ref - x.max()).days,      # R: Días desde última compra
    'cliente_id': 'count',                               # F: Número de compras
    'importe': 'sum'                                     # M: Dinero gastado
}).rename(columns={
    'fecha': 'Recency',
    'cliente_id': 'Frequency',
    'importe': 'Monetary'
})

print(rfm.head())

# Segmentar por cuartiles
for col in rfm.columns:
    rfm[f'{col}_score'] = pd.qcut(rfm[col], q=4, labels=[1, 2, 3, 4], duplicates='drop')

print("\nCon scores:")
print(rfm.head())

# Clasificación final
rfm['cliente_tipo'] = rfm.apply(lambda row: 
    'Campeón' if row['Recency_score'] == 4 and row['Frequency_score'] == 4 else
    'En riesgo' if row['Recency_score'] == 1 else
    'Normal',
    axis=1
)

print("\nDistribución de clientes:")
print(rfm['cliente_tipo'].value_counts())
```

---

## 📖 Capítulo 7: Reportes Automatizados

### Generar Resumen Ejecutivo

```python
import pandas as pd
from datetime import datetime

def generar_reporte(df, periodo):
    """
    Genera un reporte automatizado de ventas
    """
    
    # Resumen de KPIs
    total_ventas = df['importe'].sum()
    num_transacciones = len(df)
    ticket_promedio = df['importe'].mean()
    num_clientes = df['cliente_id'].nunique()
    
    # Categoría top
    cat_top = df.groupby('categoria')['importe'].sum().idxmax()
    venta_cat_top = df.groupby('categoria')['importe'].sum().max()
    
    # Generar texto del reporte
    reporte = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║        REPORTE DE VENTAS - {periodo}                     ║
    ║           Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}                        ║
    ╚═══════════════════════════════════════════════════════════╝
    
    📊 KPIs PRINCIPALES:
    ─────────────────────────────────────────────────────────────
    • Ventas Totales:           ${total_ventas:,.2f}
    • Transacciones:            {num_transacciones:,}
    • Ticket Promedio:          ${ticket_promedio:,.2f}
    • Clientes Únicos:          {num_clientes:,}
    
    🏆 DESEMPEÑO POR CATEGORÍA:
    ─────────────────────────────────────────────────────────────
    • Categoría Líder:          {cat_top}
    • Venta Categoría Líder:    ${venta_cat_top:,.2f}
    
    📈 OPORTUNIDADES:
    ─────────────────────────────────────────────────────────────
    • Enfoque en expansión de {cat_top}
    • Analizar causas de underperformance en otras categorías
    • Considerar bundle de productos para aumentar ticket promedio
    """
    
    return reporte

# Usar
print(generar_reporte(df, "MAYO 2026"))
```

---

## 📖 Capítulo 8: Ejercicio Integrador

### Caso Completo: Análisis Profundo de Ventas

```python
# PASO 1: Preparación
df = pd.read_csv("../data/ventas_mayo_2026.csv")
df['fecha'] = pd.to_datetime(df['fecha'])

# PASO 2: Análisis Multidimensional
print("=== ANÁLISIS MULTIDIMENSIONAL ===")
pivot = df.pivot_table(
    values='importe',
    index='region',
    columns='categoria',
    aggfunc='sum'
)
print(pivot)

# PASO 3: Detección de Outliers
print("\n=== DETECCIÓN DE ANOMALÍAS ===")
Q1, Q3 = df['importe'].quantile([0.25, 0.75])
IQR = Q3 - Q1
outliers = df[(df['importe'] > Q3 + 1.5*IQR)]
print(f"Transacciones atípicas: {len(outliers)}")
print(outliers[['fecha', 'cliente_id', 'importe', 'categoria']].head())

# PASO 4: Correlaciones
print("\n=== ANÁLISIS DE CORRELACIÓN ===")
print(df[['importe', 'unidades', 'precio_unitario']].corr())

# PASO 5: Segmentación
print("\n=== SEGMENTACIÓN DE CLIENTES ===")
cliente_stats = df.groupby('cliente_id').agg({
    'importe': ['sum', 'count', 'mean']
}).round(2)
cliente_stats.columns = ['gasto_total', 'num_compras', 'ticket_promedio']
print(cliente_stats.nlargest(10, 'gasto_total'))

# PASO 6: Visualización Avanzada
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Heatmap
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlOrRd', ax=axes[0, 0])
axes[0, 0].set_title('Ventas por Región y Categoría')

# Correlaciones
sns.heatmap(df[['importe', 'unidades']].corr(), annot=True, cmap='coolwarm', ax=axes[0, 1], vmin=-1, vmax=1)
axes[0, 1].set_title('Correlaciones')

# Scatter
axes[1, 0].scatter(df['unidades'], df['importe'], alpha=0.5, c=df['precio_unitario'], cmap='viridis')
axes[1, 0].set_xlabel('Unidades')
axes[1, 0].set_ylabel('Importe ($)')
axes[1, 0].set_title('Relación Cantidad-Importe (coloreado por precio)')

# Distribución
axes[1, 1].hist(df['importe'], bins=40, color='steelblue', edgecolor='black')
axes[1, 1].set_title('Distribución de Importes')
axes[1, 1].set_xlabel('Importe ($)')

plt.tight_layout()
plt.show()
```

---

## 🎓 Consejos de Maestría

### Señales de que lo estás haciendo bien

✅ Exploras los datos desde múltiples ángulos  
✅ Documentas cada decisión de transformación  
✅ Visualizas antes de sacar conclusiones  
✅ Comunicas hallazgos en lenguaje de negocio  
✅ Tus análisis son reproducibles  

### Errores a evitar

❌ Asumir correlación implica causalidad  
❌ Eliminar outliers sin investigar primero  
❌ Hacer análisis sin preguntas claras  
❌ No documentar transformaciones  
❌ Presentar números sin contexto  

### Próximos Pasos

Ahora que dominas manipulación avanzada, estás listo para:
- **Bloque 2 Parte 1**: Modelado estadístico y regresión
- **Bloque 2 Parte 2**: Predicción y machine learning

---

¡Felicitaciones! Has avanzado significativamente. 🎉
