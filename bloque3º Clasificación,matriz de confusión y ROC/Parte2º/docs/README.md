# Documentación - Bloque 3, Parte 2: Clasificación Avanzada

## Contenido de esta Carpeta

Materiales profesionales de referencia para la Parte 2 del Bloque 3, orientados a técnicas avanzadas de machine learning.

## Archivos Disponibles

### GUIA_RAPIDA.md
Referencia rápida con templates de código para:

**Detección de Desbalanceo**
```python
y.value_counts(normalize=True)  # Ver distribución
ratio = y.value_counts()[0] / y.value_counts()[1]  # Calcular ratio
```

**SMOTE - Balanceo Sintético**
```python
from imblearn.over_sampling import SMOTE
smote = SMOTE()
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)
```

**Class Weights**
```python
model = RandomForestClassifier(class_weight='balanced')
```

**Cross-Validation Estratificada**
```python
from sklearn.model_selection import StratifiedKFold, cross_validate
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_validate(model, X, y, cv=skf)
```

**Grid Search**
```python
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(model, param_grid, cv=5, scoring='roc_auc')
grid.fit(X_train, y_train)
```

**Feature Importance**
```python
importance = model.feature_importances_
# Visualizar con:
plt.barh(features, importance)
```

**SHAP Values (Explicabilidad)**
```python
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

**Ensemble Voting**
```python
from sklearn.ensemble import VotingClassifier
voting = VotingClassifier(estimators=[...], voting='soft')
```

**Curva de Aprendizaje**
```python
from sklearn.model_selection import learning_curve
train_sizes, train_scores, val_scores = learning_curve(...)
# Visualizar para diagnosticar overfitting/underfitting
```

**Calibración de Probabilidades**
```python
from sklearn.calibration import CalibratedClassifierCV
calibrated = CalibratedClassifierCV(model, cv=5)
calibrated.fit(X_train, y_train)
```

### environment.yml
Configuración del entorno Conda para Parte 2:
```yaml
name: big_data_bloque3_parte2
dependencies:
  - python=3.11
  - numpy, pandas, scipy, matplotlib, jupyter
  - pip
  - pip:
    - scikit-learn==1.4.2
    - imbalanced-learn==0.11.0
    - shap
```

Uso:
```bash
conda env create -f environment.yml
conda activate big_data_bloque3_parte2
```

### requirements.txt
Alternativa a conda para instalación vía pip:
```
scikit-learn>=0.24.0
imbalanced-learn>=0.10.0
pandas>=1.3.0
numpy>=1.20.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

Uso:
```bash
pip install -r requirements.txt
```

## Temas de Referencia Rápida

### Algoritmos Disponibles

| Algoritmo | Librería | Cuándo Usar |
|-----------|----------|------------|
| Logística | sklearn.linear_model | Baseline, rápido |
| Árbol | sklearn.tree | Interpretación |
| Random Forest | sklearn.ensemble | Producción normal |
| Gradient Boosting | sklearn.ensemble | Máximo rendimiento |
| XGBoost | xgboost | Competiciones |
| SVM | sklearn.svm | Datos complejos |

### Técnicas de Desbalanceo

| Técnica | Pro | Contra |
|---------|-----|--------|
| SMOTE | Sintético realista | Puede duplicar |
| Undersampling | Rápido | Pierde datos |
| Oversampling | Completo | Riesgo overfitting |
| Class Weights | Simple, rápido | A veces insuficiente |
| Combinado | Balanceo óptimo | Más complejidad |

### Métricas por Problema

**Detección de Fraude** (pocos positivos, FN crítico):
- Focus: Recall > Precision
- Métrica: AUC-ROC

**Spam Detection** (muchos positivos, FP molesto):
- Focus: Precision > Recall  
- Métrica: F1-Score

**Diagnóstico Médico** (equilibrio):
- Focus: Balance
- Métrica: AUC-ROC, F1

### Interpretación de Curva de Aprendizaje

```
UNDERFITTING (Model too simple)
train_score: 0.60, val_score: 0.62
→ Solución: Modelo más complejo

OVERFITTING (Model memorizing)
train_score: 0.95, val_score: 0.65
→ Solución: Regularización, más datos

BALANCED (Sweet spot)
train_score: 0.85, val_score: 0.83
→ ✅ Buen modelo
```

### Debugging Problemas Comunes

**Problema**: AUC = 0.5 (aleatorio)
- Verificar: ¿Datos correctos? ¿Features relevantes?
- Solución: Exploración de datos más profunda

**Problema**: AUC = 0.99 en train, 0.65 en test
- Verificar: Overfitting
- Solución: Cross-validation, regularización, early stopping

**Problema**: Grid Search tarda 2 horas
- Verificar: ¿Demasiados parámetros?
- Solución: Fewer params, RandomizedSearchCV, reduce CV folds

**Problema**: Todos los modelos iguales
- Verificar: ¿Features escaladas? ¿Datos limpios?
- Solución: EDA, preprocesamiento

## Checklist Antes de Modelar

- [ ] ¿Los datos están limpios?
- [ ] ¿He verificado desbalanceo?
- [ ] ¿He explorado correlaciones?
- [ ] ¿He tratado valores faltantes?
- [ ] ¿He escalado/normalizado si necesario?
- [ ] ¿He usado stratified split?
- [ ] ¿He decidido métrica de éxito?
- [ ] ¿Tengo baseline de comparación?

## Checklist Después de Modelar

- [ ] ¿He validado con cross-validation?
- [ ] ¿He probado múltiples algoritmos?
- [ ] ¿He optimizado hiperparámetros?
- [ ] ¿He visualizado matriz de confusión?
- [ ] ¿He generado ROC/Precision-Recall?
- [ ] ¿He analizado feature importance?
- [ ] ¿He detectado overfitting?
- [ ] ¿He documentado decisiones?

## Recursos Externos

### Documentación Oficial
- [Scikit-learn Classification](https://scikit-learn.org/stable/modules/classification.html)
- [Scikit-learn Model Selection](https://scikit-learn.org/stable/modules/model_selection.html)
- [Scikit-learn Ensemble](https://scikit-learn.org/stable/modules/ensemble.html)
- [Imbalanced-learn](https://imbalanced-learn.org/)
- [SHAP Documentation](https://shap.readthedocs.io/)

### Tutoriales Recomendados
- Random Forest: Understanding Random Forests
- Gradient Boosting: Gradient Boosting Machines Explained
- SMOTE: Handling Imbalanced Datasets
- SHAP: Model Interpretability with SHAP
- Grid Search: Hyperparameter Optimization Techniques

### Libros Relacionados
- "Hands-On Machine Learning" - Chapter 6-7
- "Introduction to Statistical Learning" - Chapter 4, 8
- "Machine Learning in Production" - Chapters 2-3

## Tabla de Decisión: ¿Qué Técnica Usar?

```
¿Desbalanceo moderado (<30% clase minoritaria)?
├─ Sí → Class Weights
└─ No → Salta este paso

¿Datos complejos con relaciones no-lineales?
├─ Sí → Random Forest o Gradient Boosting
└─ No → Logística puede funcionar

¿Necesitas interpretabilidad?
├─ Sí → Árbol o Logística
├─ Relativa → Random Forest con Feature Importance
└─ No necesaria → Gradient Boosting

¿Necesitas máximo rendimiento?
├─ Sí → Gradient Boosting + Tuning
└─ No → Random Forest + validación rápida

¿Necesitas explicar cada predicción?
├─ Sí → SHAP values
└─ No → Feature Importance es suficiente
```

## Propuesta de Estudio

**Semana 1**: Algoritmos básicos
- Árbol de decisión
- Random Forest
- Validación cruzada

**Semana 2**: Desbalanceo
- SMOTE
- Class Weights  
- Undersampling

**Semana 3**: Optimización
- Grid Search
- Curvas de aprendizaje
- Diagnóstico

**Semana 4**: Interpretabilidad
- Feature Importance
- Permutation Importance
- SHAP values

## Notas Finales

1. **No existe un algoritmo único "mejor"** - depende del contexto
2. **Validación > Accuracy** - es la métrica más importante
3. **Explica tus decisiones** - datos + gráficos > números
4. **Itera constantemente** - ML es experimental
5. **Documenta todo** - el código futuro eres tú

---

**Última actualización**: Mayo 2026  
**Nivel**: Advanced Intermediate  
**Duración recomendada**: 6-8 horas de estudio activo

