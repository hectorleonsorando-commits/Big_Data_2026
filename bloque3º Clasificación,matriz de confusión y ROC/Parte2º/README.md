# Bloque 3 - Parte 2: Clasificación Avanzada y Ensemble Methods

## 📚 Introducción Profesional

Bienvenidos a la Parte 2 del Bloque 3, donde llevaremos nuestras habilidades de clasificación al siguiente nivel. Si la Parte 1 fue el primer paso en el mundo de la clasificación, esta parte es el viaje hacia la **maestría en modelos predictivos de alto rendimiento**.

### ¿Qué Cambió desde la Parte 1?

En la Parte 1, aprendiste:
- Cómo entrenar un clasificador (Regresión Logística)
- Cómo evaluar su rendimiento (Matriz de Confusión, ROC)
- Por qué las métricas importan

En la Parte 2, aprenderemos:
- **Cómo mejorar significativamente el rendimiento** usando múltiples algoritmos
- **Cómo validar de forma robusta** nuestros modelos
- **Cómo manejar los datos del mundo real** (desbalanceados, complejos)
- **Cómo explicar por qué** nuestro modelo toma cada decisión
- **Cómo combinar modelos** para obtener lo mejor de cada uno

### El Desafío Real: Datos Desbalanceados

En la práctica empresarial, raramente los datos están perfectamente balanceados. Por ejemplo:
- **Churn**: 90% clientes activos, 10% que abandonan
- **Fraude**: 99.9% transacciones legítimas, 0.1% fraudulentas
- **Enfermedades raras**: 99% sanos, 1% enfermos

El problema: si tu modelo simplemente predice "no fraude" para todo, ¡tendrá 99.9% de accuracy pero será completamente inútil!

Esta parte te enseña a **vencer este desafío**.

## 📋 Conceptos Avanzados que Dominarás

### 1. Algoritmos Superiores a Regresión Logística

#### Random Forest
- **Idea**: Entrenar múltiples árboles de decisión y dejar que "voten"
- **Ventaja**: Captura relaciones no lineales complejas
- **Desventaja**: Menos interpretable que Logística
- **Cuándo usarlo**: Datos complejos, necesitas máximo rendimiento

#### Gradient Boosting
- **Idea**: Entrenar árboles secuencialmente, cada uno corrige los errores del anterior
- **Ventaja**: Rendimiento excepcional, muchas veces el mejor
- **Desventaja**: Lento de entrenar, riesgo de overfitting
- **Cuándo usarlo**: Competencias Kaggle, proyectos críticos

#### SVM (Support Vector Machines)
- **Idea**: Encontrar el hiperplano óptimo que separa clases
- **Ventaja**: Excelente en espacios de alta dimensión
- **Desventaja**: Difícil de interpretar, computacionalmente caro
- **Cuándo usarlo**: Datos con muchas features

### 2. Validación Robusta: Cross-Validation Estratificada

```python
# ❌ Malo: Split simple
X_train, X_test, y_train, y_test = train_test_split(X, y)

# ✅ Bien: Stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y  # Mantiene proporción de clases
)

# ⭐ Mejor: Cross-validation estratificada
from sklearn.model_selection import StratifiedKFold, cross_validate
skf = StratifiedKFold(n_splits=5)
scores = cross_validate(model, X, y, cv=skf)
```

**¿Por qué es importante?** Porque cada fold tendrá la misma proporción de churn/no-churn que el dataset original, dándote estimaciones más realistas.

### 3. Manejo del Desbalanceo: SMOTE vs Class Weights

#### Opción 1: SMOTE (Synthetic Minority Over-sampling)
```python
from imblearn.over_sampling import SMOTE

smote = SMOTE()
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
```
- **Pros**: Crea datos sintéticos realistas, completo balanceo
- **Contras**: Puede crear duplicados, aumenta datos de entrenamiento

#### Opción 2: Class Weights
```python
model = RandomForestClassifier(class_weight='balanced')
```
- **Pros**: Simple, rápido, no añade datos
- **Contras**: No siempre es suficiente

**Regla de oro**: Usa SMOTE si tienes tiempo y datos suficientes; usa class_weight si necesitas rapidez.

### 4. Optimización de Hiperparámetros: Grid Search

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5, scoring='roc_auc')
grid.fit(X_train, y_train)
print(f"Mejor: {grid.best_params_}")
```

**¿Qué es?** Una búsqueda exhaustiva: "Prueba todas las combinaciones de parámetros y dime cuál es mejor"

**Tiempo estimado**: Para 3×3×3 combinaciones con CV=5, son 135 entrenamientos. Con GPU: minutos. Sin GPU: café.

### 5. Explicabilidad: ¿Por Qué Decidió el Modelo?

#### Feature Importance (Importancia de Variables)
```python
importance = model.feature_importances_
# Gráfico: "Edad" es la variable más importante → 35% de la decisión
```

#### SHAP Values (Shapley Additive exPlanations)
```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
# Visualización: "Para este cliente específico, Edad = 45 lo empujó a CHURN"
```

**La diferencia**: Feature Importance = "Globalmente, ¿qué importa?" SHAP = "Para esta predicción específica, ¿qué importó?"

### 6. Ensemble Methods: Combinar Modelos

La sabiduría de las masas: pregunta a 3 expertos en lugar de 1

```python
from sklearn.ensemble import VotingClassifier

ensemble = VotingClassifier(estimators=[
    ('logit', LogisticRegression()),
    ('rf', RandomForestClassifier()),
    ('gb', GradientBoostingClassifier())
], voting='soft')
```

**Resultado típico**: Mejor que cualquier modelo individual

## 📁 Estructura del Proyecto

```
Parte2º/
├── notebooks/              # Ejercicios avanzados
│   ├── 02_Bloque_III_Clasificacion_Avanzada_ENUNCIADO.ipynb
│   └── 02_Bloque_III_Clasificacion_Avanzada_RESUELTO.ipynb
├── data/                   # Datasets balanceados y desbalanceados
│   ├── clientes_clasificacion.csv
│   └── README.md
├── docs/                   # Guías técnicas avanzadas
│   ├── GUIA_RAPIDA.md
│   └── README.md
├── requirements.txt        # Librerías (incluye imbalanced-learn)
├── environment.yml         # Entorno conda
└── README.md              # Este archivo
```

## 🚀 Cómo Empezar

### Opción 1: Usando pip (recomendado para Windows)
```bash
cd Parte2º
pip install -r requirements.txt
jupyter lab
```

### Opción 2: Usando Conda
```bash
cd Parte2º
conda env create -f environment.yml
conda activate big_data_bloque3_parte2
jupyter lab
```

## 📚 Contenido de los Notebooks

### Enunciado (02_Bloque_III_Clasificacion_Avanzada_ENUNCIADO.ipynb)
Problemas a resolver:
1. Entrena 3 modelos diferentes (Logística, Random Forest, Gradient Boosting)
2. Compara su rendimiento en datos desbalanceados
3. Aplica técnicas de rebalanceo
4. Optimiza hiperparámetros del mejor modelo
5. Explica decisiones usando Feature Importance y/o SHAP

### Resuelto (02_Bloque_III_Clasificacion_Avanzada_RESUELTO.ipynb)
Soluciones con:
- Implementaciones completas
- Mejores prácticas
- Interpretación de resultados
- Visualizaciones profesionales

## 🎯 Flujo de Aprendizaje

```
1. Revisa Parte 1 si lo necesitas
   ↓
2. Lee el enunciado - intenta resolver
   ↓
3. Consulta la guía rápida (/docs/GUIA_RAPIDA.md)
   ↓
4. Compara con soluciones
   ↓
5. Experimenta: cambia parámetros, prueba nuevos modelos
   ↓
6. Reflexiona: ¿por qué funcionó mejor?
```

## 💡 Principios Clave de Esta Parte

### 1. No Existe un Modelo Único "Mejor"
- Logística: Rápida, interpretable, baseline
- Random Forest: Versátil, buen rendimiento
- Gradient Boosting: Máximo rendimiento, complejidad
- SVM: Altas dimensiones

**Tu trabajo**: Elegir según contexto

### 2. Validación es Más Importante que Accuracy
```python
# ❌ Malo
print(f"Accuracy: {model.score(X_test, y_test)}")

# ✅ Bien
cv_scores = cross_validate(model, X, y, cv=5, scoring=['accuracy', 'precision', 'recall', 'roc_auc'])
print(f"CV Scores: {cv_scores}")
```

### 3. Desbalanceo No Es Un Enemigo, Es Un Dato
- **Detectar**: `y.value_counts(normalize=True)`
- **Entender**: ¿Por qué está desbalanceado?
- **Decidir**: ¿Es el desbalanceo parte del problema real?

### 4. La Explicabilidad Importa
- Stakeholders no confían en cajas negras
- Regulación (GDPR, ML Act) lo exige
- Debugging: "¿Por qué se equivocó el modelo?"

## 🏆 Criterios de Éxito

Al completar esta parte, podrás:

- [ ] Entrenar y comparar 5+ algoritmos de clasificación
- [ ] Detectar y manejar datos desbalanceados
- [ ] Implementar validación cruzada estratificada
- [ ] Optimizar hiperparámetros con Grid Search
- [ ] Explicar decisiones de modelos individuales
- [ ] Evaluar cuándo tienes overfitting/underfitting
- [ ] Combinar múltiples modelos en ensembles
- [ ] Implementar un pipeline ML completo

## 📊 Comparativa de Algoritmos

| Algoritmo | Velocidad | Interpretabilidad | Rendimiento | Manejo Desbalanceo | Cuándo Usarlo |
|-----------|-----------|------------------|-------------|-------------------|---------------|
| **Logística** | ⚡⚡⚡ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | Baseline, baseline, baseline |
| **Árbol** | ⚡⚡ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Inicio rápido |
| **RF** | ⚡ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Producción normal |
| **GB** | ⚡ | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Máximo rendimiento |
| **SVM** | ❌ | ⭐ | ⭐⭐⭐ | ⭐⭐ | Datos especiales |

## 🔍 Debugging de Problemas Comunes

### Problema: AUC perfecto en train, pobre en test
**Solución**: Overfitting. Prueba:
- Reduce complejidad (max_depth, n_estimators)
- Aumenta regularización
- Más datos

### Problema: Todos los modelos dan accuracy ~95%
**Solución**: Datos muy desbalanceados, verifica:
```python
print(y.value_counts(normalize=True))
# Si ves [0.95, 0.05], ese es el problema
```

### Problema: Grid Search tarda 3 horas
**Solución**: Reduce búsqueda:
- Menos parámetros
- Menos valores por parámetro
- Use RandomizedSearchCV en lugar de GridSearchCV

## 📖 Materiales de Referencia

Consulta la carpeta `docs/` para obtener:
- Guía rápida de código (GUIA_RAPIDA.md)
- Objetivos de aprendizaje
- Referencias a documentación oficial
- Sugerencias de temporalización

## 🎓 Metodología de Enseñanza

**Enfoque**: Learning by doing
1. **Código**: Escribe, ejecuta, experimenta
2. **Visualiza**: Observa resultados, intuición
3. **Compara**: Contrasta enfoques
4. **Explica**: Resume lo aprendido

---

**Profesor**: Unidad de Ciencia de Datos  
**Nivel**: Advanced Intermediate  
**Duración estimada**: 6-8 horas  
**Requisitos**: Completar Parte 1 del Bloque 3
