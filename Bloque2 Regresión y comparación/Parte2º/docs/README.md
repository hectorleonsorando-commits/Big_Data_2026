# 📚 Documentación Completa: Modelado Avanzado y Predicción (Parte 2)

## Introducción: Del Modelo Básico al Profesional

En la Parte 1 aprendiste regresión lineal. Ahora iremos más allá: técnicas para **casos complejos**, relaciones **no lineales**, y métodos para **evitar trampas comunes**.

Los mejores analistas no usan el modelo más sofisticado; usan **el modelo apropiado para el problema**. A veces eso es regresión lineal simple. A veces es Ridge. A veces es un ensamble.

---

## 🎯 Objetivos

1. ✅ Modelar relaciones no lineales (polinomios)
2. ✅ Usar regularización para evitar sobreajuste
3. ✅ Seleccionar variables de forma sistemática
4. ✅ Trabajar con outliers y datos robustos
5. ✅ Modelar variables binarias (clasificación)
6. ✅ Combinar modelos en ensambles
7. ✅ Comunicar resultados como profesional

---

## 📖 Capítulo 1: Regresión Polinómica - Más Allá de Líneas Rectas

### El Problema

No todas las relaciones son lineales:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Datos no lineales (cuadráticos)
X_real = np.linspace(0, 10, 50).reshape(-1, 1)
y_real = 2 + 3*X_real.flatten() - 0.2*X_real.flatten()**2 + np.random.normal(0, 5, 50)

# Visualizar
plt.scatter(X_real, y_real, alpha=0.6, label='Datos reales')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Relación No Lineal')
plt.legend()
plt.show()

# Si usas regresión lineal simple, fallarás
```

### Solución: Polinomios

```python
# Crear características polinómicas
poly = PolynomialFeatures(degree=2)  # Incluir X y X²
X_poly = poly.fit_transform(X_real)

# Entrenar
modelo_poly = LinearRegression()
modelo_poly.fit(X_poly, y_real)

# Predecir
X_test = np.linspace(0, 10, 100).reshape(-1, 1)
X_test_poly = poly.transform(X_test)
y_pred = modelo_poly.predict(X_test_poly)

# Comparar
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Lineal (mal)
modelo_lineal = LinearRegression()
modelo_lineal.fit(X_real, y_real)
y_pred_lineal = modelo_lineal.predict(X_test)

axes[0].scatter(X_real, y_real, alpha=0.6)
axes[0].plot(X_test, y_pred_lineal, 'r-', linewidth=2, label='Lineal (R²={:.2f})'.format(modlo_lineal.score(X_real, y_real)))
axes[0].set_title('Regresión Lineal (Mal Ajuste)')
axes[0].legend()

# Polinomial (bien)
axes[1].scatter(X_real, y_real, alpha=0.6)
axes[1].plot(X_test, y_pred, 'g-', linewidth=2, label='Polinomial (R²={:.2f})'.format(modelo_poly.score(X_poly, y_real)))
axes[1].set_title('Regresión Polinómica (Buen Ajuste)')
axes[1].legend()

plt.tight_layout()
plt.show()
```

### ¿Qué Grado Usar?

```python
from sklearn.model_selection import cross_val_score

# Probar diferentes grados
grados = range(1, 8)
scores = []

for grado in grados:
    poly = PolynomialFeatures(degree=grado)
    X_poly = poly.fit_transform(X_real)
    modelo = LinearRegression()
    
    # Validación cruzada
    score = cross_val_score(modelo, X_poly, y_real, cv=5, scoring='r2').mean()
    scores.append(score)
    print(f"Grado {grado}: R² = {score:.3f}")

# Graficar
plt.plot(grados, scores, 'o-')
plt.xlabel('Grado del Polinomio')
plt.ylabel('R² (Validación Cruzada)')
plt.title('Seleccionar Grado Óptimo')
plt.show()

# Regla: Elige el grado con mejor CV score, pero evita sobreajuste
```

---

## 📖 Capítulo 2: Regularización - Controlar la Complejidad

### Ridge Regression (L2)

```python
from sklearn.linear_model import Ridge

# Problema: Coeficientes muy grandes (sobreajuste)
modelo_ols = LinearRegression()
modelo_ols.fit(X_poly, y_real)
print("OLS coefficients:", modelo_ols.coef_)

# Solución Ridge: Penaliza coeficientes grandes
modelo_ridge = Ridge(alpha=1.0)  # alpha controla penalización
modelo_ridge.fit(X_poly, y_real)
print("Ridge coefficients:", modelo_ridge.coef_)  # Más pequeños

# ¿Cuál es mejor?
print(f"\nR² OLS: {modelo_ols.score(X_poly, y_real):.3f}")
print(f"R² Ridge: {modelo_ridge.score(X_poly, y_real):.3f}")

# Ridge sacrifica poco R² pero gana estabilidad
```

### Lasso Regression (L1)

```python
from sklearn.linear_model import Lasso

# Lasso: Penaliza aún más, puede hacer coeficientes = 0 (selección)
modelo_lasso = Lasso(alpha=0.1)
modelo_lasso.fit(X_poly, y_real)

print("Lasso coefficients:", modelo_lasso.coef_)
print(f"Coeficientes cero: {(modelo_lasso.coef_ == 0).sum()}")

# Ventaja: Elimina variables automáticamente
```

### Elegir Alpha

```python
from sklearn.linear_model import RidgeCV, LassoCV

# Buscar alpha óptimo automáticamente
alphas = np.logspace(-3, 3, 100)

# Ridge
modelo_ridge_cv = RidgeCV(alphas=alphas, cv=5)
modelo_ridge_cv.fit(X_poly, y_real)
print(f"Alpha óptimo para Ridge: {modelo_ridge_cv.alpha_:.3f}")

# Lasso
modelo_lasso_cv = LassoCV(alphas=alphas, cv=5)
modelo_lasso_cv.fit(X_poly, y_real)
print(f"Alpha óptimo para Lasso: {modelo_lasso_cv.alpha_:.3f}")
```

---

## 📖 Capítulo 3: Selección de Variables

### Forward/Backward Stepwise

```python
from sklearn.feature_selection import RFE

# RFE: Eliminación recursiva de características
modelo_base = LinearRegression()
rfe = RFE(estimator=modelo_base, n_features_to_select=3, step=1)
rfe.fit(X_poly, y_real)

print("Features seleccionadas:")
for i, sel in enumerate(rfe.support_):
    print(f"  Feature {i}: {'✓' if sel else '✗'}")
```

### Feature Importance

```python
# Importancia basada en coeficientes
importancias = np.abs(modelo_ols.coef_)
indices = np.argsort(importancias)[::-1]

print("Top features por importancia:")
for i, idx in enumerate(indices[:5]):
    print(f"  {i+1}. Feature {idx}: {importancias[idx]:.3f}")
```

---

## 📖 Capítulo 4: Regresión Logística - Clasificación Binaria

### De Regresión a Clasificación

A veces tu variable dependiente es 0/1 (compró/no compró):

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

# Datos: ¿Churn (abandono) de cliente?
df = pd.DataFrame({
    'edad': [25, 35, 45, 22, 55, 30],
    'gasto_anual': [500, 2000, 5000, 100, 8000, 1500],
    'meses_cliente': [6, 24, 60, 2, 120, 12],
    'abandono': [1, 0, 0, 1, 0, 1]  # 1 = abandonó, 0 = permaneció
})

X = df[['edad', 'gasto_anual', 'meses_cliente']]
y = df['abandono']

# Entrenar
modelo_log = LogisticRegression()
modelo_log.fit(X, y)

# Predicciones (probabilidades)
y_prob = modelo_log.predict_proba(X)[:, 1]  # Probabilidad de abandono
print(f"Probabilidades de abandono: {y_prob}")

# Predicciones (clasificación)
y_pred = modelo_log.predict(X)
print(f"Clasificaciones: {y_pred}")
```

### Interpretación

```python
# Coeficientes en logística son en escala de log-odds
coefs = modelo_log.coef_[0]

print("Efectos:")
for nombre, coef in zip(X.columns, coefs):
    odds_ratio = np.exp(coef)
    print(f"  {nombre}: Odds Ratio = {odds_ratio:.3f}")
    print(f"    → Cada unidad aumenta odds de abandono por {odds_ratio:.1f}x")
```

### Métricas de Clasificación

```python
# Matriz de confusión
print("Matriz de Confusión:")
print(confusion_matrix(y, y_pred))

# Precisión, Recall, F1
print("\n" + classification_report(y, y_pred))

# ROC-AUC
auc = roc_auc_score(y, y_prob)
print(f"\nROC-AUC: {auc:.3f}")

# Plotear curva ROC
fpr, tpr, _ = roc_curve(y, y_prob)
plt.plot(fpr, tpr, label=f'ROC (AUC={auc:.3f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
```

---

## 📖 Capítulo 5: Ensambles - Combinar Modelos

### Averaging de Modelos

```python
from sklearn.ensemble import VotingRegressor

# Crear múltiples modelos
modelo1 = LinearRegression()
modelo2 = Ridge(alpha=0.5)
modelo3 = Lasso(alpha=0.1)

# Ensamble: Promediar predicciones
ensamble = VotingRegressor([
    ('lineal', modelo1),
    ('ridge', modelo2),
    ('lasso', modelo3)
])

ensamble.fit(X_train, y_train)

# Predicciones
y_pred_ensemble = ensamble.predict(X_test)
print(f"R² Ensamble: {ensamble.score(X_test, y_test):.3f}")
```

### Stacking

```python
from sklearn.ensemble import StackingRegressor

# Modelo meta que aprende a combinar
stacking = StackingRegressor(
    estimators=[('ridge', Ridge()), ('lasso', Lasso())],
    final_estimator=LinearRegression()
)

stacking.fit(X_train, y_train)
print(f"R² Stacking: {stacking.score(X_test, y_test):.3f}")
```

---

## 📖 Capítulo 6: Comunicar Resultados Profesionalmente

### Estructura de Informe

```python
def generar_informe_ejecutivo(modelo, X_test, y_test, X_train, y_train):
    """
    Genera un informe profesional de resultados de modelo
    """
    
    y_pred = modelo.predict(X_test)
    r2_train = modelo.score(X_train, y_train)
    r2_test = modelo.score(X_test, y_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    informe = f"""
    ═══════════════════════════════════════════════════════════════
                    REPORTE DE MODELADO PREDICTIVO
    ═══════════════════════════════════════════════════════════════
    
    1. RESUMEN EJECUTIVO
    ───────────────────────────────────────────────────────────────
    El modelo desarrollado predice la variable objetivo con un
    R² de {r2_test:.1%} en datos de prueba, explicando {r2_test:.1%} de
    la variación.
    
    2. DESEMPEÑO
    ───────────────────────────────────────────────────────────────
    • R² Entrenamiento: {r2_train:.3f}
    • R² Prueba: {r2_test:.3f}
    • RMSE: {rmse:,.2f}
    • Estabilidad: {'✓ Buen' if r2_train - r2_test < 0.05 else '⚠ Hay sobreajuste'}
    
    3. RECOMENDACIONES
    ───────────────────────────────────────────────────────────────
    ✓ El modelo es {'apto' if r2_test > 0.7 else 'limitado'} para producción
    ✓ {'Monitorear regularmente' if r2_test < 0.8 else 'Actualizaciones anuales recomendadas'}
    
    ═══════════════════════════════════════════════════════════════
    """
    
    return informe

print(generar_informe_ejecutivo(modelo, X_test, y_test, X_train, y_train))
```

---

## 📖 Capítulo 7: Ejercicio Integrador Completo

### Caso: Predecir Conversión de Clientes

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt

# PASO 1: Cargar datos
df = pd.read_csv("../data/clientes.csv")
print("Datos:", df.shape)
print(df.head())

# PASO 2: Preparación
X = df.drop('conversion', axis=1)
y = df['conversion']

# Estandarizar (importante para regresión logística)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PASO 3: División
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# PASO 4: Entrenar
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)

# PASO 5: Evaluar
y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print("\nDesempeño:")
print(f"  Exactitud: {modelo.score(X_test, y_test):.3f}")
print(f"  ROC-AUC: {roc_auc_score(y_test, y_prob):.3f}")
print("\n" + classification_report(y_test, y_pred))

# PASO 6: Interpretación
print("\nVariables más importantes:")
coefs = modelo.coef_[0]
indices = np.argsort(np.abs(coefs))[::-1][:5]
for idx in indices:
    print(f"  {X.columns[idx]}: {coefs[idx]:.3f}")
```

---

## 🎓 Lecciones Finales

### Señales de un Modelo Bueno

✅ R² > 0.7 en validación cruzada  
✅ No hay sobreajuste (train ≈ test)  
✅ Predicciones tienen sentido comercial  
✅ Documentado y reproducible  
✅ Monitoreable en producción  

### Errores Fatales a Evitar

❌ Usar el modelo más complejo sin justificación  
❌ No verificar supuestos  
❌ Confiar en R² a ciegas  
❌ Hacer predicciones fuera del rango de entrenamiento  
❌ No actualizar el modelo cuando cambian los datos  

### Próximos Pasos en tu Carrera

Ahora que dominas modelado predictivo:
- 🤖 Aprende Machine Learning (árboles, random forests, XGBoost)
- 📊 Aprende métodos de series temporales (ARIMA, Prophet)
- 🧠 Aprende deep learning (redes neuronales)
- 📈 Especialízate en tu dominio (finanzas, marketing, RH, etc.)

---

## ¡Felicitaciones!

Has completado un viaje de **principiante a profesional en análisis de datos**. 🎉

Tienes las herramientas para:
- Explorar datos complejos
- Crear modelos predictivos
- Comunicar insights de forma profesional
- Tomar decisiones basadas en datos

**Ahora aplica lo aprendido. El mundo necesita análisis de datos de calidad.** 🚀
