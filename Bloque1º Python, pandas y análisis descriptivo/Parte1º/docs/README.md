# 📚 Documentación Completa: Python, Pandas y Análisis Descriptivo (Parte 1)

## Introducción: Por Qué Aprender Esto

Antes de sumergirte en el código, necesitas entender **por qué** estos temas importan.

En el mundo actual, **los datos están en todas partes**: en ventas de tiendas, en comportamiento de usuarios en línea, en logs de servidores, en redes sociales. Pero los datos sin procesar son caóticos, incompletos y confusos.

**Tu misión en esta parte:** Aprender a transformar datos desordenados en información limpia, comprensible y accionable. No serás un científico de datos teórico; serás un **detective de datos** que sabe hacer preguntas, obtener respuestas claras y comunicas conclusiones que la gente puede entender.

---

## 🎯 Objetivos Específicos

Al terminar esta parte, **podrás**:

1. ✅ Escribir código Python limpio y funcional para tareas de análisis
2. ✅ Cargar datos desde archivos y explorar su estructura
3. ✅ Detectar y reparar problemas comunes en datos (duplicados, valores faltantes, tipos incorrectos)
4. ✅ Calcular estadísticas que resumirán el comportamiento de los datos
5. ✅ Crear gráficos que comunican patrones visualmente
6. ✅ Sacar conclusiones que tienen sentido comercial

---

## 📖 Capítulo 1: Fundamentos de Python para Análisis de Datos

### ¿Qué es Python?

Python es un lenguaje de programación diseñado para ser **legible y poderoso**. A diferencia de otros lenguajes, Python se parece casi al inglés:

```python
# Esto es Python - fácil de leer, ¿verdad?
edad = 35
nombre = "María"
print(f"Hola, {nombre} tiene {edad} años")
```

**Por qué lo usamos para análisis de datos:**
- Es simple de aprender pero increíblemente potente
- Tiene librerías especializadas (pandas, numpy, matplotlib)
- La comunidad de ciencia de datos es masiva
- Es gratis y de código abierto

### Conceptos Fundamentales

#### Variables: Contenedores de Información

Una variable es un nombre que apunta a un valor. Piensa en ello como etiquetas en cajas:

```python
# Ejemplo 1: Variables simples
precio_producto = 29.99          # Número decimal (float)
cantidad_vendida = 150           # Número entero (int)
nombre_cliente = "Juan López"    # Texto (string)
es_cliente_vip = True            # Booleano (verdadero/falso)

print(f"Vendimos {cantidad_vendida} unidades de {nombre_cliente} a ${precio_producto} cada una")
```

**Por qué importa en análisis:**
- Almacenarás datos temporalmente en variables
- Las reutilizarás múltiples veces en tu análisis
- El nombre debe ser **significativo** (usa `precio_total`, no `x` o `pt`)

#### Listas: Colecciones Ordenadas

Una lista es como un carrito de compras: contiene múltiples artículos en orden:

```python
# Ejemplo 2: Listas
ventas_diarias = [100, 150, 125, 180, 200, 175, 160]
categorias = ["Electrónica", "Ropa", "Alimentos", "Libros"]

# Acceder a elementos (comienza en 0, no en 1)
primera_venta = ventas_diarias[0]        # 100
ultima_venta = ventas_diarias[-1]        # 160
primeras_tres = ventas_diarias[0:3]      # [100, 150, 125]

# Operaciones útiles
print(f"Total de ventas: {sum(ventas_diarias)}")
print(f"Promedio: {sum(ventas_diarias) / len(ventas_diarias)}")
print(f"Máxima: {max(ventas_diarias)}")
```

**En análisis de datos:**
- Trabajarás constantemente con secuencias de números
- Las listas son la estructura básica antes de pasar a pandas

#### Diccionarios: Datos Estructurados

Un diccionario mapea **claves** a **valores** (como un índice de libro):

```python
# Ejemplo 3: Diccionarios
cliente = {
    "id": 12345,
    "nombre": "Ana García",
    "email": "ana@example.com",
    "compras_totales": 2500.50,
    "es_activo": True
}

# Acceder a valores por clave
print(f"El cliente {cliente['nombre']} ha gastado ${cliente['compras_totales']}")

# Iterar sobre diccionarios
for clave, valor in cliente.items():
    print(f"{clave}: {valor}")
```

**En análisis:**
- Representarás filas de datos como diccionarios
- Pandas convertirá diccionarios en DataFrames automáticamente

#### Control de Flujo: Tomar Decisiones

Los condicionales permiten que tu código tome diferentes caminos según condiciones:

```python
# Ejemplo 4: If-elif-else
monto_compra = 1500

if monto_compra >= 1000:
    descuento = 0.15
    categoria = "Cliente Premium"
elif monto_compra >= 500:
    descuento = 0.10
    categoria = "Cliente Estándar"
else:
    descuento = 0.05
    categoria = "Cliente Regular"

monto_final = monto_compra * (1 - descuento)
print(f"{categoria}: Descuento de {descuento*100}%. Total: ${monto_final}")
```

**Aplicación práctica:**
- Clasificarás clientes por segmentos
- Marcarás datos problemáticos para investigación
- Aplicarás reglas de limpieza condicionales

#### Bucles: Repetición Automatizada

Los bucles evitan escribir el mismo código múltiples veces:

```python
# Ejemplo 5: Bucle for
ventas = [100, 150, 200, 175]
total = 0

for venta in ventas:
    total += venta
    print(f"Venta procesada: ${venta}. Total acumulado: ${total}")

print(f"\nTotal de ventas del período: ${total}")

# Bucle con range()
print("\nClasificación de ventas:")
for i, venta in enumerate(ventas, 1):
    if venta >= 150:
        estado = "Buena"
    else:
        estado = "Baja"
    print(f"Día {i}: ${venta} - {estado}")
```

**En análisis de datos:**
- Procesarás cada fila de un dataset
- Aplicarás transformaciones a múltiples columnas
- Generarás reportes automáticos

#### Funciones: Código Reutilizable

Una función es un bloque de código que puedes usar una y otra vez:

```python
# Ejemplo 6: Definir una función
def calcular_comision(venta, tasa=0.10):
    """
    Calcula la comisión sobre una venta.
    
    Parámetros:
    - venta: el monto de la venta
    - tasa: la tasa de comisión (por defecto 10%)
    
    Retorna: el monto de comisión
    """
    return venta * tasa

# Usar la función
venta1 = calcular_comision(1000)           # Usa tasa por defecto
venta2 = calcular_comision(500, tasa=0.15) # Tasa personalizada

print(f"Comisión 1: ${venta1}")
print(f"Comisión 2: ${venta2}")

# Otra función más compleja
def clasificar_cliente(monto_anual):
    """Clasifica cliente según gasto anual"""
    if monto_anual >= 5000:
        return "VIP"
    elif monto_anual >= 2000:
        return "Premium"
    else:
        return "Regular"

# Usar con múltiples clientes
clientes = [1500, 3000, 6000, 1000, 4500]
for monto in clientes:
    clase = clasificar_cliente(monto)
    print(f"Monto ${monto} -> Clase: {clase}")
```

**Beneficios:**
- **Reutilización**: Escribe una vez, usa muchas veces
- **Claridad**: El código se lee como prosa
- **Mantenibilidad**: Cambios en un lugar afectan todo

---

## 📖 Capítulo 2: NumPy - Operaciones Vectorizadas

### ¿Por Qué NumPy?

Imagina que tienes 1 millón de ventas y necesitas multiplicar cada una por 1.21 (con IVA). Con bucles Python sería LENTO. NumPy lo hace **instantáneamente**:

```python
import numpy as np

# Forma lenta (con Python puro)
ventas_python = [100, 150, 200, 175, 125]
ventas_con_iva = []
for venta in ventas_python:
    ventas_con_iva.append(venta * 1.21)

# Forma rápida (con NumPy)
ventas_numpy = np.array([100, 150, 200, 175, 125])
ventas_con_iva_numpy = ventas_numpy * 1.21

print("Con Python:", ventas_con_iva)
print("Con NumPy:", ventas_con_iva_numpy)
```

### Conceptos Clave de NumPy

#### Arrays: La Estructura Central

```python
import numpy as np

# Crear arrays de varias formas
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros(5)                    # Array de ceros
arr3 = np.ones(5)                     # Array de unos
arr4 = np.arange(0, 10, 2)           # Rango: 0, 2, 4, 6, 8
arr5 = np.linspace(0, 1, 5)          # 5 valores distribuidos entre 0 y 1

print("Array 1:", arr1)
print("Ceros:", arr2)
print("Rango:", arr4)
print("Distribuido:", arr5)
```

#### Operaciones Vectorizadas (Lo Mágico)

```python
# Operaciones elemento a elemento
ventas = np.array([100, 150, 200, 175, 125])

# Multiplicación
print("Con IVA (21%):", ventas * 1.21)

# División
print("Comisión (10%):", ventas * 0.10)

# Comparaciones
print("Ventas >= 150:", ventas >= 150)

# Operaciones complejas
iva = ventas * 0.21
neto = ventas
bruto = neto + iva
print("Bruto:", bruto)
```

#### Funciones Estadísticas

```python
ventas = np.array([100, 150, 200, 175, 125, 80, 220])

# Estadísticas básicas
print(f"Media: {np.mean(ventas)}")
print(f"Mediana: {np.median(ventas)}")
print(f"Desv. típica: {np.std(ventas)}")
print(f"Mínimo: {np.min(ventas)}")
print(f"Máximo: {np.max(ventas)}")
print(f"Suma: {np.sum(ventas)}")
print(f"Cuartiles: {np.percentile(ventas, [25, 50, 75])}")

# Interpretación:
# - La media te dice el "centro" típico
# - La desv. típica te dice qué tan dispersos están los datos
# - Los percentiles te dicen "el 25% tiene menos de X"
```

---

## 📖 Capítulo 3: Introducción a Pandas

### ¿Qué es Pandas?

Pandas es una librería que trabaja con **tablas de datos** (como Excel). La estructura principal es el **DataFrame**:

```python
import pandas as pd

# Crear un DataFrame simple
datos = {
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'cliente': ['Juan', 'María', 'Pedro'],
    'monto': [100, 150, 200],
    'categoria': ['Electrónica', 'Ropa', 'Alimentos']
}

df = pd.DataFrame(datos)
print(df)
```

Output:
```
        fecha cliente  monto     categoria
0  2024-01-01    Juan    100  Electrónica
1  2024-01-02   María    150       Ropa
2  2024-01-03   Pedro    200    Alimentos
```

### Cargar Datos desde Archivos

La mayoría de análisis comienza cargando datos existentes:

```python
import pandas as pd

# Cargar CSV
df = pd.read_csv("../data/ventas_mayo_2026.csv")

# Primeras filas para inspeccionar
print(df.head())

# Últimas filas
print(df.tail())

# Dimensiones
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
```

### Exploración Inicial

Antes de hacer cálculos, **debes entender tus datos**:

```python
# Información general
df.info()          # Tipos de datos, valores no nulos

# Estadísticas descriptivas
df.describe()      # Media, desv. típica, min, max

# Verificar valores nulos
print(df.isnull().sum())

# Primeros valores por columna
print(df.head(3))
```

**Qué buscar:**
- ¿Hay columnas que esperabas pero faltan?
- ¿Los tipos son correctos? (¿la fecha es realmente fecha o texto?)
- ¿Cuántos valores faltantes hay?
- ¿El rango de números tiene sentido?

---

## 📖 Capítulo 4: Limpieza de Datos (La Parte Difícil)

### El 80% del Tiempo de un Analista

En la vida real, **80% del tiempo en análisis se gasta limpiando datos**. Es tedioso pero crítico. Datos sucios = conclusiones falsas.

### Problema 1: Duplicados

```python
import pandas as pd

df = pd.read_csv("../data/ventas_mayo_2026.csv")

# Detectar duplicados
print(f"Total de registros: {len(df)}")
print(f"Duplicados totales: {df.duplicated().sum()}")
print(f"Duplicados en columna específica: {df.duplicated(subset=['cliente_id']).sum()}")

# Ver ejemplos de duplicados
duplicados = df[df.duplicated(keep=False)].sort_values('cliente_id')
print(duplicados.head(10))

# Eliminar duplicados
df_limpio = df.drop_duplicates()
print(f"Después de eliminar: {len(df_limpio)} registros")
```

**Decisión importante:** ¿Mantener la primera ocurrencia o la última?
- `keep='first'`: Mantiene la primera (por defecto)
- `keep='last'`: Mantiene la última
- `keep=False`: Marca todas las duplicadas para inspección manual

### Problema 2: Valores Faltantes (NaN)

```python
# Detectar valores faltantes
print("Valores faltantes por columna:")
print(df.isnull().sum())

# Porcentaje de faltantes
print("\nPorcentaje de faltantes:")
print((df.isnull().sum() / len(df) * 100).round(2))

# Visualizar dónde están
print("\nPrimeros registros con faltantes:")
print(df[df.isnull().any(axis=1)].head())
```

**Estrategias de imputación:**

```python
# Opción 1: Eliminar registros con faltantes
df_eliminado = df.dropna()
print(f"Registros después de eliminar faltantes: {len(df_eliminado)}")

# Opción 2: Imputar con la mediana (para variables numéricas)
df['precio_unitario'] = df['precio_unitario'].fillna(df['precio_unitario'].median())

# Opción 3: Imputar con un valor específico
df['region'] = df['region'].fillna('Sin informar')

# Opción 4: Imputar con el valor anterior (para series temporales)
df['valor'] = df['valor'].fillna(method='ffill')
```

**Decisión:** ¿Qué estrategia usar?
- **Eliminar:** Si hay muy pocos faltantes (< 5%)
- **Mediana:** Si es variable numérica (menos sensible a extremos que media)
- **Valor fijo:** Si hay un valor "por defecto" lógico
- **Interpolación:** Si hay patrón temporal

### Problema 3: Tipos de Datos Incorrectos

```python
print(df.dtypes)  # Ver tipos actuales

# Problema: La fecha está como texto, no como datetime
print(f"Tipo de 'fecha': {df['fecha'].dtype}")

# Convertir a tipo correcto
df['fecha'] = pd.to_datetime(df['fecha'])
print(f"Tipo después: {df['fecha'].dtype}")

# Convertir a numérico
df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')

# Convertir a categórico (ahorra memoria)
df['categoria'] = df['categoria'].astype('category')
```

**Por qué importa:**
- Fechas como texto no se pueden ordenar correctamente
- Números como texto no se pueden calcular
- Categorías numéricas ahorran memoria

### Problema 4: Outliers (Valores Extremos)

```python
import numpy as np

# Detectar outliers con el método IQR
Q1 = df['importe'].quantile(0.25)
Q3 = df['importe'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['importe'] < limite_inferior) | (df['importe'] > limite_superior)]
print(f"Outliers encontrados: {len(outliers)}")
print(outliers.sort_values('importe', ascending=False).head())

# Decisión: ¿Eliminar o mantener?
# - Investiga primero si son errores o valores reales
# - Si son reales, considéralos en tu análisis
# - Si son errores (ej: 999 cuando debería ser 99), corrígelos
```

### Crear Variables Derivadas

A menudo necesitas crear nuevas columnas basadas en existentes:

```python
# Extraer componentes de fecha
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.day_name()
df['trimestre'] = df['fecha'].dt.quarter

# Calcular ratios
df['ticket_unitario'] = df['importe'] / df['unidades']
df['importe_con_iva'] = df['importe'] * 1.21
df['margen_estimado'] = (df['precio_unitario'] - df['costo_unitario']) / df['precio_unitario']

# Variables binarias (sí/no)
df['es_grande_importe'] = (df['importe'] > df['importe'].median()).astype(int)

# Categorizar
df['segmento_importe'] = pd.cut(df['importe'], 
                                 bins=[0, 100, 500, 1000, float('inf')],
                                 labels=['Pequeño', 'Medio', 'Grande', 'Premium'])
```

---

## 📖 Capítulo 5: Análisis Descriptivo - Sacando Conclusiones

### Estadísticas Univariantes (Una Variable)

```python
# Resumen completo de una variable
print(df['importe'].describe())

# Output típico:
# count     1000.000     (1000 registros)
# mean       487.532     (promedio $487.53)
# std        312.145     (dispersión)
# min          10.000    (mínima venta)
# 25%        218.750    (25% de los datos está debajo de esto)
# 50%        451.000    (mediana - 50% arriba, 50% abajo)
# 75%        698.250    (75% está debajo de esto)
# max       1999.000    (máxima venta)

# ¿Cómo interpretar?
# - Si mean ≈ median: datos distribuidos normalmente
# - Si mean >> median: hay valores extremos arriba (outliers positivos)
# - Si mean << median: hay valores extremos abajo
```

### Agregaciones: Agrupar y Resumir

```python
# Ventas totales por categoría
ventas_por_categoria = df.groupby('categoria')['importe'].sum().sort_values(ascending=False)
print(ventas_por_categoria)

# Múltiples estadísticas a la vez
resumen = df.groupby('categoria').agg({
    'importe': ['sum', 'mean', 'count'],
    'unidades': 'sum',
    'cliente_id': 'nunique'  # Clientes únicos
})

print(resumen)

# Renombrar columnas para claridad
resumen.columns = ['ventas_totales', 'venta_media', 'num_transacciones', 
                   'unidades_totales', 'clientes_unicos']
```

**Interpretación:**
- `sum`: ¿Cuál es el total?
- `mean`: ¿Cuál es el promedio?
- `count`: ¿Cuántas transacciones?
- `nunique`: ¿Cuántos clientes diferentes?

### Comparaciones: Entender Diferencias

```python
# ¿Qué región vende más?
ventas_por_region = df.groupby('region')['importe'].sum()
print("Ventas por región:")
print(ventas_por_region)

# ¿Cuál es la diferencia?
maxima = ventas_por_region.max()
minima = ventas_por_region.min()
diferencia_porcentaje = ((maxima - minima) / minima) * 100
print(f"La región con más ventas supera a la menor por {diferencia_porcentaje:.1f}%")

# Análisis más profundo: promedio vs total
print("\nPromedio vs Total por región:")
resumen_region = df.groupby('region')['importe'].agg(['sum', 'mean', 'count'])
resumen_region.columns = ['total', 'promedio_transaccion', 'num_transacciones']
print(resumen_region)
```

---

## 📖 Capítulo 6: Visualización - Comunicar con Gráficos

### ¿Por Qué Visualizar?

Un gráfico comunica en **segundos** lo que un número nunca podría. Imagina:
- 5000 filas de números en una tabla
- vs. un gráfico que muestra la tendencia instantáneamente

### Matplotlib Básico

```python
import matplotlib.pyplot as plt

# Configurar estilo
plt.figure(figsize=(10, 6))  # Tamaño del gráfico

# Histograma: ¿Cómo se distribuyen las ventas?
plt.hist(df['importe'], bins=30, color='steelblue', edgecolor='black')
plt.title('Distribución de Importes de Venta', fontsize=14, fontweight='bold')
plt.xlabel('Importe ($)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.3)
plt.show()

# ¿Qué significa?
# - Eje X: Rangos de importe
# - Eje Y: Cuántas ventas cayeron en cada rango
# - Patrón: ¿Es simétrico? ¿Tiene una cola?
```

### Comparaciones entre Grupos

```python
# Boxplot: Comparar importes por categoría
plt.figure(figsize=(10, 6))
df.boxplot(column='importe', by='categoria', figsize=(10, 6))
plt.title('Importe de Venta por Categoría')
plt.suptitle('')  # Quitar título automático
plt.xlabel('Categoría')
plt.ylabel('Importe ($)')
plt.show()

# Interpretar boxplot:
# - Caja: Donde está el 50% central de datos
# - Línea en la caja: Mediana
# - Bigotes: Extremos de datos "normales"
# - Puntos: Outliers
```

### Series Temporales

```python
# ¿Cómo evolucionan las ventas en el tiempo?
df['fecha'] = pd.to_datetime(df['fecha'])
ventas_diarias = df.groupby('fecha')['importe'].sum()

plt.figure(figsize=(12, 6))
ventas_diarias.plot(kind='line', color='darkgreen', linewidth=2)
plt.title('Evolución de Ventas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Venta Total ($)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Variante: Con barras
plt.figure(figsize=(12, 6))
ventas_diarias.plot(kind='bar', color='coral')
plt.title('Ventas por Día')
plt.xlabel('Fecha')
plt.ylabel('Venta Total ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Gráficos de Categorías

```python
# Gráfico de barras para categorías
ventas_por_categoria = df.groupby('categoria')['importe'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
ventas_por_categoria.plot(kind='bar', color='skyblue')
plt.title('Ventas Totales por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Venta Total ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# ¿Qué preguntas responde?
# - ¿Cuál categoría vende más?
# - ¿Cuál es el rango?
# - ¿Hay grandes diferencias o es equilibrado?
```

---

## 📖 Capítulo 7: Ejercicio Integrador - Poniéndolo Todo Junto

### El Caso: Análisis de Ventas de Mayo 2026

Tienes un dataset de ventas del mes de mayo. Tu misión es:

**Tareas:**
1. Cargar el dataset y explorar su estructura
2. Limpiar los datos (duplicados, valores faltantes, tipos)
3. Crear variables derivadas útiles
4. Responder preguntas específicas:
   - ¿Cuál es la categoría con mayor venta total?
   - ¿Cuál es el ticket medio por región?
   - ¿Qué categoría tiene más unidades vendidas?
   - ¿Hay patrones temporales (ciertos días venden más)?
5. Crear visualizaciones claras
6. Redactar conclusiones de negocio

### Solución Paso a Paso

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# PASO 1: Cargar y explorar
df = pd.read_csv("../data/ventas_mayo_2026.csv")
print("=== EXPLORACIÓN INICIAL ===")
print(f"Dimensiones: {df.shape}")
print(f"\nTipos de datos:\n{df.dtypes}")
print(f"\nValores nulos:\n{df.isnull().sum()}")
print(f"\nPrimeros registros:\n{df.head()}")

# PASO 2: Limpiar
print("\n=== LIMPIEZA ===")
print(f"Duplicados: {df.duplicated().sum()}")
df = df.drop_duplicates()

# Convertir fecha
df['fecha'] = pd.to_datetime(df['fecha'])

# Imputar valores faltantes
df['precio_unitario'] = df['precio_unitario'].fillna(df['precio_unitario'].median())
df['region'] = df['region'].fillna('Sin informar')

print("Datos limpios. Registro final:")
print(f"Dimensiones: {df.shape}")

# PASO 3: Variables derivadas
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.day_name()
df['dia_semana_num'] = df['fecha'].dt.weekday
df['importe_con_iva'] = df['importe'] * 1.21
df['ticket_unitario'] = df['importe'] / df['unidades']

# PASO 4: Responder preguntas
print("\n=== ANÁLISIS ===")

# Pregunta 1: Categoría con mayor venta
ventas_por_categoria = df.groupby('categoria')['importe'].sum().sort_values(ascending=False)
print(f"\n1. Ventas por categoría:")
print(ventas_por_categoria)
categoria_top = ventas_por_categoria.index[0]
venta_top = ventas_por_categoria.iloc[0]
print(f"   → La categoría '{categoria_top}' lidera con ${venta_top:,.2f}")

# Pregunta 2: Ticket medio por región
ticket_por_region = df.groupby('region')['importe'].mean().sort_values(ascending=False)
print(f"\n2. Ticket promedio por región:")
print(ticket_por_region)

# Pregunta 3: Categoría con más unidades
unidades_por_categoria = df.groupby('categoria')['unidades'].sum().sort_values(ascending=False)
print(f"\n3. Unidades vendidas por categoría:")
print(unidades_por_categoria)
categoria_unidades = unidades_por_categoria.index[0]
print(f"   → '{categoria_unidades}' lideró en volumen")

# Pregunta 4: Patrones por día de semana
dia_semana_orden = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ventas_por_dia = df.groupby('dia_semana')['importe'].sum().reindex(dia_semana_orden)
print(f"\n4. Ventas por día de semana:")
print(ventas_por_dia)

# PASO 5: Visualizaciones
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1
ventas_por_categoria.plot(ax=axes[0, 0], kind='bar', color='steelblue')
axes[0, 0].set_title('Ventas por Categoría')
axes[0, 0].set_ylabel('Importe ($)')

# Gráfico 2
ticket_por_region.plot(ax=axes[0, 1], kind='bar', color='coral')
axes[0, 1].set_title('Ticket Promedio por Región')
axes[0, 1].set_ylabel('Importe Promedio ($)')

# Gráfico 3
unidades_por_categoria.plot(ax=axes[1, 0], kind='bar', color='green')
axes[1, 0].set_title('Unidades Vendidas por Categoría')
axes[1, 0].set_ylabel('Unidades')

# Gráfico 4
ventas_por_dia.plot(ax=axes[1, 1], kind='line', color='purple', marker='o', linewidth=2)
axes[1, 1].set_title('Ventas por Día de Semana')
axes[1, 1].set_ylabel('Importe Total ($)')
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# PASO 6: Conclusiones
print("\n=== CONCLUSIONES ===")
print(f"""
1. LIDERAZGO POR CATEGORÍA:
   La categoría '{categoria_top}' lideró con ${venta_top:,.2f} en ventas.
   
2. SEGMENTACIÓN REGIONAL:
   La región con mayor ticket promedio es '{ticket_por_region.index[0]}'
   con un promedio de ${ticket_por_region.iloc[0]:,.2f} por transacción.
   
3. VOLUMEN:
   '{categoria_unidades}' vendió la mayor cantidad de unidades,
   demostrando su posición estratégica.
   
4. PATRÓN TEMPORAL:
   Las ventas tienden a ser {'más altas' if ventas_por_dia.index[ventas_por_dia.argmax()] != 'Sunday' else 'más bajas'}
   los fines de semana, sugiriendo patrones de compra específicos.
   
RECOMENDACIONES:
- Aumentar inventario en '{categoria_top}' para Q2
- Investigar por qué '{ticket_por_region.index[0]}' tiene tickets más altos
- Considerar promociones en categorías con menor rendimiento
""")
```

---

## 🎓 Consejos Finales

### Buenas Prácticas

1. **Siempre explora primero**: Antes de cualquier cálculo, entiende tus datos
2. **Documenta decisiones**: ¿Por qué eliminaste esos outliers? Anótalo
3. **Verifica suposiciones**: No confíes en los datos automáticamente
4. **Comunica en lenguaje simple**: Los stakeholders no entienden técnico
5. **Itera**: El análisis es un proceso, no un evento único

### Errores Comunes

❌ **Trabajar con datos sin limpiar**: Basura entra, basura sale  
❌ **Ignorar valores faltantes**: Distorsionan resultados  
❌ **Sacar conclusiones sin visualizar**: Los números pueden mentir  
❌ **No revisar tipos de datos**: Fechas como texto son un desastre  
❌ **Hacer análisis sin preguntas claras**: ¿Qué quiero saber?  

### Próximos Pasos

Una vez domines esta parte:
- Avanza a **Bloque 1 Parte 2** para técnicas avanzadas
- Luego a **Bloque 2 Parte 1** para modelado estadístico
- Finalmente a **Bloque 2 Parte 2** para predicciones

---

## 📚 Recursos Adicionales

- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)

¡Ahora estás listo. Abre el notebook y empieza a practicar!
