# 📚 Documentación Completa: Modelado Estadístico y Regresión (Parte 1)

## Introducción: De Describir a Predecir

Hasta ahora has **descrito** datos. Ahora aprenderás a **modelarlos** y **predecirlos**.

Regresión no es solo sobre hacer predicciones; es sobre **entender relaciones causales** entre variables. ¿Por qué suben las ventas cuando aumenta el presupuesto publicitario? ¿Cuánto sube? ¿Es estadísticamente significativo?

---

## 🎯 Objetivos

1. ✅ Entender el concepto de regresión lineal y sus supuestos
2. ✅ Ajustar modelos de regresión simple y múltiple
3. ✅ Interpretar coeficientes en contexto comercial
4. ✅ Verificar que el modelo cumple supuestos (diagnóstico)
5. ✅ Comparar grupos estadísticamente (test t, ANOVA)
6. ✅ Validar modelos antes de confiar en ellos
7. ✅ Comunicar incertidumbre (intervalos de confianza)

---

## 📖 Capítulo 1: Fundamentos de Regresión Lineal

### La Idea Simple

Supon que quieres predecir **ventas** basándote en **presupuesto de marketing**.

La ecuación más simple es una línea recta:

$$\text{Ventas} = \beta_0 + \beta_1 \times \text{Presupuesto} + \text{error}$$

Dónde:
- $\beta_0$ = Intersección (ventas si presupuesto = 0)
- $\beta_1$ = Pendiente (cuánto aumentan ventas por $1 de presupuesto)
- $\text{error}$ = La parte que no explicamos

### Ajustar un Modelo (Scikit-learn)

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos de ejemplo
df = pd.DataFrame({
    'presupuesto': [1000, 2000, 3000, 4000, 5000, 6000],
    'ventas': [10000, 18000, 25000, 32000, 40000, 47000]
})

# Preparar datos
X = df[['presupuesto']].values
y = df['ventas'].values

# Ajustar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Extraer parámetros
intercepcion = modelo.intercept_
pendiente = modelo.coef_[0]

print(f"Ecuación: Ventas = {intercepcion:.2f} + {pendiente:.2f} × Presupuesto")
print(f"\nInterpretación:")
print(f"- Si presupuesto = $0: ventas esperadas = ${intercepcion:,.2f}")
print(f"- Por cada $1 de presupuesto, ventas suben ${pendiente:.2f}")

# Hacer predicciones
presu_nuevo = np.array([[7000]])
prediccion = modelo.predict(presu_nuevo)
print(f"\nSi presupuesto = $7,000: ventas predichas = ${prediccion[0]:,.2f}")
```

### Visualizar el Ajuste

```python
# Crear línea de regresión
X_rango = np.array([[df['presupuesto'].min()], [df['presupuesto'].max()]])
y_linea = modelo.predict(X_rango)

# Graficar
plt.figure(figsize=(10, 6))
plt.scatter(df['presupuesto'], df['ventas'], s=100, alpha=0.6, label='Datos reales')
plt.plot(X_rango, y_linea, color='red', linewidth=2, label='Línea de regresión')
plt.xlabel('Presupuesto de Marketing ($)')
plt.ylabel('Ventas ($)')
plt.title('Regresión Lineal: Marketing vs Ventas')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

---

## 📖 Capítulo 2: Regresión Múltiple

### Más de Una Variable Independiente

En realidad, las ventas dependen de múltiples factores:

```python
# Datos más realistas
df = pd.DataFrame({
    'presupuesto_marketing': [1000, 2000, 1500, 3000, 2500, 4000],
    'equipo_ventas': [3, 5, 4, 6, 5, 8],
    'experiencia_vendedores': [2, 5, 3, 7, 4, 9],
    'ventas': [15000, 45000, 25000, 70000, 40000, 95000]
})

# Múltiples predictores
X = df[['presupuesto_marketing', 'equipo_ventas', 'experiencia_vendedores']]
y = df['ventas']

# Ajustar
modelo = LinearRegression()
modelo.fit(X, y)

# Resultados
print("Coeficientes:")
for nombre, coef in zip(X.columns, modelo.coef_):
    print(f"  {nombre}: {coef:.2f}")
print(f"  Intercepción: {modelo.intercept_:.2f}")

print(f"\nEcuación:")
print(f"Ventas = {modelo.intercept_:.0f} + "
      f"{modelo.coef_[0]:.2f}×Presupuesto + "
      f"{modelo.coef_[1]:.2f}×Equipo + "
      f"{modelo.coef_[2]:.2f}×Experiencia")
```

### Interpretación

- $\beta_1 = 5.5$: Manteniendo constantes el equipo y experiencia, cada $1 de presupuesto → $5.50 de ventas
- $\beta_2 = 3000$: Un vendedor más → $3,000 en ventas
- $\beta_3 = 2000$: Un año más de experiencia → $2,000 en ventas

---

## 📖 Capítulo 3: Evaluación del Modelo - ¿Qué Tan Bueno Es?

### Coeficiente de Determinación (R²)

```python
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Predicciones
y_pred = modelo.predict(X)

# R²: Proporción de varianza explicada (0-1)
r2 = r2_score(y, y_pred)
print(f"R² = {r2:.3f}")

# Interpretación:
# R² = 0.95 → El modelo explica el 95% de la variación en ventas
# R² = 0.50 → El modelo explica solo el 50% (bastante limitado)
# R² = 1.00 → Ajuste perfecto (sospechoso, probablemente sobreajuste)
```

### Errores de Predicción

```python
# RMSE: Raíz del error cuadrático medio
rmse = np.sqrt(mean_squared_error(y, y_pred))
print(f"RMSE: ${rmse:,.2f}")
# Interpretación: En promedio, predicciones están ${rmse:,.2f} alejadas

# MAE: Error absoluto medio
mae = mean_absolute_error(y, y_pred)
print(f"MAE: ${mae:,.2f}")
# Interpretación: Desviación promedio absoluta

# Comparar
print(f"\nVentas promedio: ${y.mean():,.2f}")
print(f"RMSE como % del promedio: {(rmse / y.mean() * 100):.1f}%")
```

---

## 📖 Capítulo 4: Diagnóstico - Verificar Supuestos

### Los 5 Supuestos de Regresión

Todo modelo de regresión asume:

1. **Linealidad**: Relación lineal entre X e Y
2. **Normalidad**: Los residuales (errores) son normales
3. **Homocedasticidad**: Varianza constante de errores
4. **Independencia**: Observaciones no correlacionadas
5. **Sin multicolinealidad**: Predictores no muy correlacionados

### Visualizar Residuales

```python
# Calcular residuales
residuales = y - y_pred

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residuales vs Ajustados (homocedasticidad)
axes[0, 0].scatter(y_pred, residuales, alpha=0.6)
axes[0, 0].axhline(y=0, color='r', linestyle='--')
axes[0, 0].set_xlabel('Valores Ajustados')
axes[0, 0].set_ylabel('Residuales')
axes[0, 0].set_title('¿Varianza constante? Debería ser una nube horizontal')

# 2. Q-Q plot (normalidad)
from scipy import stats
stats.probplot(residuales, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('¿Normalidad? Puntos deberían seguir la línea')

# 3. Histograma de residuales
axes[1, 0].hist(residuales, bins=15, edgecolor='black')
axes[1, 0].set_xlabel('Residuales')
axes[1, 0].set_ylabel('Frecuencia')
axes[1, 0].set_title('¿Distribución Normal? Debería ser campana')

# 4. Escala-Localización
std_residuales = np.sqrt(np.abs(residuales / residuales.std()))
axes[1, 1].scatter(y_pred, std_residuales, alpha=0.6)
axes[1, 1].axhline(y=1, color='r', linestyle='--')
axes[1, 1].set_xlabel('Valores Ajustados')
axes[1, 1].set_ylabel('√|Residuales estandarizados|')
axes[1, 1].set_title('¿Escala constante?')

plt.tight_layout()
plt.show()
```

---

## 📖 Capítulo 5: Comparación de Grupos - Test Estadísticos

### Test t: Comparar Dos Grupos

```python
from scipy import stats

# Datos: Ventas por tipo de vendedor
vendedores_tipo_a = np.array([100, 120, 95, 110, 105])
vendedores_tipo_b = np.array([150, 160, 145, 155, 165])

# Descriptivos
print(f"Tipo A - Media: {vendedores_tipo_a.mean():.2f}, Desv: {vendedores_tipo_a.std():.2f}")
print(f"Tipo B - Media: {vendedores_tipo_b.mean():.2f}, Desv: {vendedores_tipo_b.std():.2f}")

# Test t
t_stat, p_value = stats.ttest_ind(vendedores_tipo_a, vendedores_tipo_b)

print(f"\nTest t:")
print(f"  t-estatístico: {t_stat:.3f}")
print(f"  p-valor: {p_value:.4f}")

if p_value < 0.05:
    print("  ✅ Diferencia SIGNIFICATIVA (p < 0.05)")
    print("  Conclusión: El tipo B vende significativamente más")
else:
    print("  ❌ Diferencia NO significativa")
    print("  Conclusión: No hay evidencia de que un tipo sea mejor")
```

### ANOVA: Comparar 3+ Grupos

```python
# Ventas por región
region_norte = np.array([100, 105, 110, 95, 120])
region_sur = np.array([80, 85, 75, 90, 95])
region_este = np.array([150, 140, 160, 155, 145])

# Test ANOVA
f_stat, p_value = stats.f_oneway(region_norte, region_sur, region_este)

print(f"ANOVA:")
print(f"  F-estadístico: {f_stat:.3f}")
print(f"  p-valor: {p_value:.4f}")

if p_value < 0.05:
    print("  ✅ Hay diferencias significativas entre regiones")
    print(f"  Región con más ventas: Este (${region_este.mean():.0f})")
else:
    print("  ❌ No hay diferencias significativas")
```

---

## 📖 Capítulo 6: Validación Cruzada - Evitar Sobreajuste

### El Problema del Sobreajuste

Un modelo puede ajustarse perfectamente a tus datos pero fracasar en datos nuevos.

```python
from sklearn.model_selection import cross_val_score, train_test_split

# Dividir datos: 80% entrenamiento, 20% prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar en training
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluar en ambos conjuntos
r2_train = modelo.score(X_train, y_train)
r2_test = modelo.score(X_test, y_test)

print(f"R² en datos de entrenamiento: {r2_train:.3f}")
print(f"R² en datos de prueba: {r2_test:.3f}")

if r2_train - r2_test > 0.1:
    print("⚠️  Sobreajuste detectado: El modelo es demasiado específico para los datos de entrenamiento")
else:
    print("✅ Modelo generalizador bien")
```

### Validación Cruzada K-Fold

```python
# Dividir datos en 5 grupos y entrenar 5 veces
scores = cross_val_score(LinearRegression(), X, y, cv=5, scoring='r2')

print(f"Scores de cada fold: {scores.round(3)}")
print(f"Promedio: {scores.mean():.3f} (+/- {scores.std():.3f})")

# El ± es importante: si es muy alto, el modelo es inestable
```

---

## 📖 Capítulo 7: Interpretación Estadística

### Significancia vs Relevancia Práctica

```python
# Un coeficiente puede ser estadísticamente significativo pero sin importancia práctica

# Ejemplo:
# Coeficiente: 0.001 (significativo con p < 0.05)
# Pero en términos prácticos: Aumento de $1,000 en presupuesto → +$1 en ventas
# Eso no es útil para decisiones de negocio

# Usar statsmodels para más detalles
import statsmodels.api as sm

X_con_const = sm.add_constant(X)
modelo_stats = sm.OLS(y, X_con_const).fit()
print(modelo_stats.summary())

# Interpretación de la salida:
# - P>|t|: p-valor (< 0.05 = significativo)
# - [95% Conf. Int.]: Intervalo de confianza del coeficiente
```

---

## 📖 Capítulo 8: Ejercicio Integrador

### Caso: Predecir Ventas Basado en Marketing

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# PASO 1: Cargar datos
df = pd.read_csv("../data/marketing_ventas.csv")
print("Datos:")
print(df.head())

# PASO 2: Explorar
print(f"\nCorrelaciones:")
print(df.corr())

# PASO 3: Preparar
X = df[['presupuesto_marketing', 'num_vendedores']]
y = df['ventas']

# PASO 4: División train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# PASO 5: Entrenar
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# PASO 6: Evaluar
y_pred = modelo.predict(X_test)
r2_test = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\nDesempeño:")
print(f"  R²: {r2_test:.3f}")
print(f"  RMSE: ${rmse:,.2f}")

# PASO 7: Conclusiones
print(f"\nEcuación:")
for nombre, coef in zip(X.columns, modelo.coef_):
    print(f"  {nombre}: ${coef:,.2f}")
print(f"  Intercepción: ${modelo.intercept_:,.2f}")
```

---

## 🎓 Reglas de Oro

✅ Siempre verifica supuestos antes de confiar en predicciones  
✅ Usa validación cruzada, no confíes en R² a ciegas  
✅ Documenta decisiones (¿por qué ese modelo?)  
✅ Comunica incertidumbre (intervalos, no solo puntos)  
✅ La correlación NO implica causalidad  

---

¡Listo para Bloque 2 Parte 2! 🚀
