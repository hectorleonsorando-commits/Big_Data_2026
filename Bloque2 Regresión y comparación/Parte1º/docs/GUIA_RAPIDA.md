# Guía Rápida - Bloque 2 Parte 1

## 🎯 Objetivo General

Al finalizar esta parte, comprenderás **cómo modelar relaciones entre variables y comparar grupos**, usando regresión lineal y test estadísticos, validando supuestos y generando conclusiones estadísticamente fundamentadas.

## 📚 Contenidos Específicos

### 1. Fundamentos de Regresión Lineal
- **Concepto**: Predecir una variable continua (Y) a partir de otra(s) (X)
- **Ecuación lineal**: Y = β₀ + β₁X + ε
- **Regresión simple vs. múltiple**: Uno vs. múltiples predictores
- **Interpretación de coeficientes**: ¿Cuánto aumenta Y si X sube una unidad?
- **Ajuste de modelos**: Mínimos cuadrados ordinarios (OLS)

### 2. Evaluación del Ajuste
- **Coeficiente de determinación (R²)**: Proporción de varianza explicada (0-1)
- **Error cuadrático medio (RMSE)**: Magnitud típica del error
- **Error absoluto medio (MAE)**: Interpretación en unidades originales
- **Visualización del ajuste**: Scatter + línea de regresión

### 3. Supuestos del Modelo
- **Linealidad**: Relación lineal entre X e Y
- **Normalidad**: Residuales distribuidos normalmente
- **Homocedasticidad**: Varianza constante de residuales
- **Independencia**: Observaciones no correlacionadas
- **Ausencia de multicolinealidad**: Predictores no correlacionados entre sí

### 4. Diagnóstico de Residuales
- **Gráfico de residuales vs. ajustados**: Detecta heterocedasticidad
- **Q-Q plot**: Comprueba normalidad de residuales
- **Escala-localización**: Varianza en función de valores predichos
- **Residuales vs. leverage**: Identifica puntos influyentes
- **Distancia de Cook**: Detecta observaciones que distorsionan el modelo

### 5. Comparación de Grupos (Paramétrica)
- **Test t de Student**: Comparar medias de dos grupos
- **ANOVA (Análisis de Varianza)**: Comparar medias de 3+ grupos
- **Supuestos**: Normalidad, homogeneidad de varianzas
- **Contrastes post-hoc**: Dunnet, Tukey para identificar diferencias

### 6. Comparación de Grupos (No Paramétrica)
- **Mann-Whitney U**: Alternativa no paramétrica al test t
- **Kruskal-Wallis**: Alternativa no paramétrica a ANOVA
- **Uso**: Cuando los datos no cumplen supuestos de normalidad
- **Interpretación**: Basada en rangos, no en medias

### 7. Contraste de Hipótesis
- **Hipótesis nula vs. alternativa**: H₀ vs. H₁
- **Significancia (α)**: Umbral típico 0.05
- **P-valor**: Probabilidad de observar datos si H₀ es cierta
- **Potencia estadística**: Capacidad de detectar un efecto real
- **Tamaño de efecto**: Magnitud práctica más allá de significancia

### 8. Validación de Modelos
- **Validación cruzada (k-fold)**: Evita sobreajuste
- **Train/test split**: División temporal o aleatoria
- **Curvas de aprendizaje**: Diagnóstico de sesgo/varianza
- **Regularización**: Introducción a Ridge/Lasso (vista previa)

### 9. Selección de Variables
- **Forward stepwise**: Añade variables incrementalmente
- **Backward stepwise**: Elimina variables no significativas
- **Criterios AIC/BIC**: Balance entre ajuste y complejidad
- **Multicolinealidad**: VIF (Variance Inflation Factor)

## 📋 Casos de Uso Prácticos

1. **Predecir ventas** a partir de presupuesto publicitario
2. **Comparar efectividad** de dos estrategias de marketing
3. **Analizar relación** entre precio y demanda
4. **Validar que un modelo** es adecuado para producción

## ✅ Criterios de Éxito

Al finalizar, podrás:

- [ ] Ajustar regresiones simples y múltiples
- [ ] Interpretar coeficientes en contexto de negocio
- [ ] Verificar supuestos del modelo sistemáticamente
- [ ] Comparar grupos con tests paramétricos y no paramétricos
- [ ] Validar modelos antes de implementarlos
- [ ] Redactar conclusiones estadísticas formales

## 🔗 Referencias Rápidas

```python
# Regresión simple (scikit-learn)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Regresión con statsmodels (más detalles)
import statsmodels.api as sm
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# Test t
from scipy import stats
t_stat, p_value = stats.ttest_ind(grupo1, grupo2)

# ANOVA
f_stat, p_value = stats.f_oneway(grupo1, grupo2, grupo3)

# R²
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)

# RMSE
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

## 💡 Recomendaciones

1. **Prerequisito**: Domina Bloque 1 completamente
2. **Practica la interpretación**: Los números sin contexto no valen
3. **Comprueba siempre los supuestos**: No asumas, diagnostica
4. **Comunica incertidumbre**: Los intervalos de confianza importan
