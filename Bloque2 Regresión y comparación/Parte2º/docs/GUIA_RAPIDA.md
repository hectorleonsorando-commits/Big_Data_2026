# Guía Rápida - Bloque 2 Parte 2

## 🎯 Objetivo General

Al finalizar esta parte, implementarás **modelos predictivos complejos y especializados**, aplicando técnicas de regularización, manejo de relaciones no lineales y métodos de ensamble, para obtener predicciones precisas y robustas.

## 📚 Contenidos Específicos

### 1. Regresión Polinómica
- **Expansión de características**: Términos de grado 2, 3, etc.
- **Overfitting**: Detección visual mediante gráficos
- **Selección del grado**: Validación cruzada y criterios informativos
- **Interpretación**: Relaciones no lineales en contexto
- **Trade-off complejidad-exactitud**: Curva de sesgo-varianza

### 2. Regularización
- **Ridge (L2)**: Penaliza magnitud de coeficientes
- **Lasso (L1)**: Penaliza y realiza selección de variables (shrinkage)
- **ElasticNet**: Combinación de Ridge + Lasso
- **Parámetro λ (alpha)**: Ajuste y selección mediante validación cruzada
- **Estandardización**: Necesaria antes de regularizar
- **Ventajas**: Previene sobreajuste, mejora generalización

### 3. Selección Avanzada de Variables
- **Feature importance**: Coeficientes absolutos, permutation importance
- **RFE (Recursive Feature Elimination)**: Eliminación automática iterativa
- **Métodos univariantes**: Correlación, test estadísticos
- **Multicolinealidad**: VIF, matriz de correlación
- **Validación cruzada** para estabilidad de selección

### 4. Regresión Robusta
- **Problemática**: Outliers distorsionan OLS
- **Métodos robustos**: Huber, RANSAC, Theil-Sen
- **Detección y tratamiento**: Leverage y distancia de Cook
- **Transformaciones**: Log, raíz, Box-Cox
- **Aplicación**: Datos reales con anomalías

### 5. Regresión Logística (Introducción a Clasificación)
- **Variable binaria**: 0/1, Sí/No, Éxito/Fracaso
- **Función logística**: Mapeo a probabilidades (0-1)
- **Odds y log-odds**: Interpretación en términos de riesgo
- **Coeficientes**: Cambios en log-odds por unidad de X
- **Predicción**: Probabilidades y clasificación con threshold
- **Métricas**: Precisión, recall, F1, curva ROC

### 6. Análisis Discriminante Lineal (LDA)
- **Objetivo**: Separar linealmente grupos
- **Supuestos**: Normalidad, igualdad de covarianzas
- **Discriminadores**: Combinaciones lineales que maximizan separación
- **Predicción**: Asignación a grupo más probable
- **Comparación con LR**: Interpretaciones distintas

### 7. Modelos con Interacciones
- **Interacción**: Efecto de X₁ depende de X₂
- **Especificación**: Incluir término X₁*X₂
- **Interpretación**: Cómo cambia pendiente según otra variable
- **Visualización**: Gráficos con múltiples líneas
- **Escalado**: Importancia de centrar variables

### 8. Ensambles Simples
- **Averaging**: Promediar predicciones de múltiples modelos
- **Voting**: Votación mayoritaria en clasificación
- **Stacking**: Entrenar modelo meta sobre predicciones
- **Ventajas**: Reduce varianza, captura distintas perspectivas
- **Cuándo usar**: Modelos con distribuciones de error diversas

### 9. Inferencia Avanzada
- **Intervalos de confianza**: Para predicciones puntuales y medias
- **Predicción vs. estimación**: Diferencias de incertidumbre
- **Bootstrapping**: Estimación no paramétrica de variabilidad
- **Tests de hipótesis**: Significancia de términos complejos
- **Comparación de modelos**: Likelihood ratio test, AIC, BIC

### 10. Comunicación y Reportes
- **Estructura de informe**: Contexto, metodología, resultados, conclusiones
- **Tablas de resultados**: Coeficientes, significancia, intervalos
- **Visualizaciones**: Efectos parciales, importancia, diagnósticos
- **Narrativa**: Traducción de números a decisiones de negocio
- **Reproducibilidad**: Documentación de análisis

## 📋 Casos de Uso Avanzados

1. **Predicción de conversión**: Regresión logística en marketing
2. **Segmentación de riesgo**: Análisis discriminante de default
3. **Modelado de elasticidad**: Relaciones no lineales precio-demanda
4. **Predicción robusta**: Datos con outliers sistemáticos
5. **Ensamble de experimentos**: Múltiples estrategias de negocio

## ✅ Criterios de Éxito

Al finalizar, podrás:

- [ ] Implementar regresión polinómica y evaluar complejidad óptima
- [ ] Aplicar Ridge, Lasso y ElasticNet adecuadamente
- [ ] Detectar y tratar outliers con métodos robustos
- [ ] Ajustar regresión logística e interpretar probabilidades
- [ ] Construir análisis discriminante lineal
- [ ] Modelar interacciones complejas
- [ ] Combinar modelos en ensambles
- [ ] Generar intervalos de confianza y tests de hipótesis
- [ ] Redactar informes estadísticos profesionales

## 🔗 Referencias Rápidas

```python
# Regularización
from sklearn.linear_model import Ridge, Lasso, ElasticNet
ridge = Ridge(alpha=1.0)  # Ajustar con CV
ridge.fit(X_train, y_train)

# Feature importance
importances = np.abs(model.coef_[0])
indices = np.argsort(importances)[::-1]

# Regresión logística
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
y_proba = log_model.predict_proba(X_test)[:, 1]  # Probabilidades

# Regresión robusta
from sklearn.linear_model import HuberRegressor
robust_model = HuberRegressor(epsilon=1.35, max_iter=100)

# ROC-AUC
from sklearn.metrics import roc_auc_score, roc_curve
auc = roc_auc_score(y_test, y_proba)
fpr, tpr, _ = roc_curve(y_test, y_proba)

# Ensamble simple (averaging)
y_pred = (model1.predict(X) + model2.predict(X)) / 2
```

## 💡 Recomendaciones

1. **Prerequisito**: Domina Bloque 2 Parte 1 y Bloque 1 completamente
2. **Valida siempre**: Usa validación cruzada antes de elegir hiperparámetros
3. **Compara modelos**: Evalúa múltiples enfoques antes de decantarte
4. **Comunica incertidumbre**: Intervalos de confianza > puntos estimados
5. **Audita resultados**: Verifica que las predicciones tienen sentido comercial
