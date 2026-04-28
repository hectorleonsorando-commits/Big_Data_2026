# GUIA_RAPIDA.md - Bloque 3, Parte 2: Clasificación Avanzada

## Referencia Rápida - Técnicas Avanzadas

### 1. Detección de Desbalanceo

```python
import pandas as pd
from collections import Counter

# Cargar datos
df = pd.read_csv('clientes_abandono_mayo_2026.csv')
y = df['Churn']

# Ver distribución
print(y.value_counts())
print(y.value_counts(normalize=True))

# Calcular ratio de desbalanceo
ratio = y.value_counts()[0] / y.value_counts()[1]
print(f"Ratio desbalanceo: {ratio:.2f}:1")

# Visualizar
plt.figure(figsize=(8, 4))
y.value_counts().plot(kind='bar')
plt.title('Distribución de Clases')
plt.ylabel('Frecuencia')
plt.show()
```

### 2. SMOTE - Oversampling de Clase Minoritaria

```python
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Split PRIMERO
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# SMOTE SOLO en train
smote = SMOTE(random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

print(f"Original: {Counter(y_train)}")
print(f"Después SMOTE: {Counter(y_train_sm)}")

# Entrenar con datos balanceados
model.fit(X_train_sm, y_train_sm)
```

### 3. Undersampling

```python
from imblearn.under_sampling import RandomUnderSampler

# Undersample clase mayoritaria
undersample = RandomUnderSampler(random_state=42)
X_train_us, y_train_us = undersample.fit_resample(X_train, y_train)

# Entrenar
model.fit(X_train_us, y_train_us)
```

### 4. Class Weights

```python
from sklearn.linear_model import LogisticRegression
from sklearn.utils.class_weight import compute_class_weight

# Opción 1: 'balanced' automático
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# Opción 2: Especificar pesos manualmente
weights = compute_class_weight('balanced', 
                               classes=np.unique(y_train), 
                               y=y_train)
class_weight_dict = {0: weights[0], 1: weights[1]}
model = LogisticRegression(class_weight=class_weight_dict, max_iter=1000)
model.fit(X_train, y_train)

print(f"Pesos: {class_weight_dict}")
```

### 5. Cross-Validation Estratificada

```python
from sklearn.model_selection import StratifiedKFold, cross_validate

# ❌ Mal: CV normal puede desbalancear folds
# kfold = KFold(n_splits=5)

# ✅ Bien: Stratified mantiene proporción en cada fold
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Validar modelo
scores = cross_validate(model, X, y, cv=skfold, 
                       scoring=['accuracy', 'precision', 'recall', 'roc_auc'])

print(f"Accuracy: {scores['test_accuracy'].mean():.3f} ± {scores['test_accuracy'].std():.3f}")
print(f"Precision: {scores['test_precision'].mean():.3f}")
print(f"Recall: {scores['test_recall'].mean():.3f}")
print(f"AUC: {scores['test_roc_auc'].mean():.3f}")
```

### 6. Grid Search con Cross-Validation

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Definir parámetros a probar
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'class_weight': ['balanced', None]
}

# Grid search
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, 
                          scoring='roc_auc', n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

print(f"Mejores parámetros: {grid_search.best_params_}")
print(f"Mejor AUC: {grid_search.best_score_:.3f}")

# Usar mejor modelo
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
```

### 7. Curva de Aprendizaje

```python
from sklearn.model_selection import learning_curve

# Generar curva de aprendizaje
train_sizes, train_scores, val_scores = learning_curve(
    LogisticRegression(max_iter=1000),
    X_train, y_train, cv=5, 
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='roc_auc'
)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_scores.mean(axis=1), label='Train AUC')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Val AUC')
plt.fill_between(train_sizes, 
                 train_scores.mean(axis=1) - train_scores.std(axis=1),
                 train_scores.mean(axis=1) + train_scores.std(axis=1), alpha=0.1)
plt.xlabel('Training Set Size')
plt.ylabel('AUC Score')
plt.legend()
plt.title('Curva de Aprendizaje')
plt.show()

# Interpretación:
# - Si ambas curvas bajas y separadas: underfitting
# - Si train alta, val baja: overfitting
# - Si ambas altas y cercanas: buen balance
```

### 8. Calibración de Probabilidades

```python
from sklearn.calibration import calibration_curve, CalibratedClassifierCV

# Calibrar predicciones
calibrated_model = CalibratedClassifierCV(base_estimator=model, cv=5)
calibrated_model.fit(X_train, y_train)
y_pred_calibrated = calibrated_model.predict_proba(X_test)[:, 1]

# Evaluar calibración
prob_true, prob_pred = calibration_curve(y_test, y_pred_calibrated, n_bins=10)

plt.figure(figsize=(8, 6))
plt.plot(prob_pred, prob_true, 's-', label='Calibrated')
plt.plot([0, 1], [0, 1], 'k--', label='Perfect calibration')
plt.xlabel('Predicted Probability')
plt.ylabel('True Probability')
plt.legend()
plt.title('Calibration Curve')
plt.show()
```

### 9. Feature Importance - Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

# Entrenar Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf.fit(X_train, y_train)

# Obtener importancia
feature_importance = rf.feature_importances_
features = X_train.columns

# Visualizar
plt.figure(figsize=(10, 6))
indices = np.argsort(feature_importance)[-15:]  # Top 15
plt.barh(features[indices], feature_importance[indices])
plt.xlabel('Importancia')
plt.title('Feature Importance - Random Forest')
plt.show()
```

### 10. SHAP Values - Explicabilidad

```python
import shap
from sklearn.ensemble import GradientBoostingClassifier

# Entrenar modelo
gbc = GradientBoostingClassifier(n_estimators=100, random_state=42)
gbc.fit(X_train, y_train)

# Explicador SHAP
explainer = shap.TreeExplainer(gbc)
shap_values = explainer.shap_values(X_test)

# Plot resumen
shap.summary_plot(shap_values[1], X_test, plot_type="bar")

# Plot de impacto (fuerza de cada feature)
shap.summary_plot(shap_values[1], X_test)

# Explicar una predicción específica
shap.force_plot(explainer.expected_value[1], 
                shap_values[1][0], X_test.iloc[0])
```

### 11. Ensemble - Voting Classifier

```python
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# Crear clasificadores base
lr = LogisticRegression(max_iter=1000, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Ensemble
voting_clf = VotingClassifier(
    estimators=[('lr', lr), ('rf', rf), ('gb', gb)],
    voting='soft'  # 'soft' usa predict_proba, 'hard' usa predict
)

# Entrenar
voting_clf.fit(X_train, y_train)

# Predecir
y_pred = voting_clf.predict(X_test)
y_pred_proba = voting_clf.predict_proba(X_test)[:, 1]
```

### 12. Precision-Recall Trade-off

```python
from sklearn.metrics import precision_recall_curve

# Calcular curva
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(recall, precision, 'b-', lw=2)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.grid(True, alpha=0.3)

# Encontrar punto óptimo
f1_scores = 2 * (precision * recall) / (precision + recall + 1e-10)
best_idx = np.argmax(f1_scores)
plt.plot(recall[best_idx], precision[best_idx], 'ro', markersize=10, 
         label=f'Optimal F1={f1_scores[best_idx]:.3f}')
plt.legend()
plt.show()
```

## Interpretación Avanzada

### Curva de Aprendizaje

```
1. UNDERFITTING (Both low)
   train_score ~0.6, val_score ~0.6
   → Solución: Modelo más complejo

2. OVERFITTING (Train high, Val low)
   train_score ~0.95, val_score ~0.65
   → Solución: Regularización, más datos, simplificar

3. BALANCED (Both high and close)
   train_score ~0.85, val_score ~0.83
   → Buen balance ✓
```

### Interpretación de SHAP

- **Red bars**: Predicciones hacia clase 1 (positivo)
- **Blue bars**: Predicciones hacia clase 0 (negativo)
- **Más largo**: Mayor impacto
- **Global**: Feature importance general
- **Local**: Por qué un caso específico

### Class Weights vs SMOTE

| Técnica | Ventajas | Desventajas |
|---------|----------|------------|
| **Class Weight** | Simple, rápido, sin datos nuevos | Puede no ser suficiente |
| **SMOTE** | Crea datos sintéticos balanceados | Puede crear duplicados |
| **Undersampling** | Rápido, reduce datos | Puede perder información |
| **Combinado** | Balance óptimo | Más complejo |

## Pipeline Recomendado

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE

# Pipeline con SMOTE
pipe = ImbPipeline([
    ('scaler', StandardScaler()),
    ('smote', SMOTE(random_state=42)),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Entrenar
pipe.fit(X_train, y_train)

# Predecir
y_pred = pipe.predict(X_test)
```

## Checklist de Mejor Práctica

- [ ] Verificar desbalanceo de clases
- [ ] Usar stratified split y CV
- [ ] Aplicar técnica de rebalanceo
- [ ] Escalar features si es necesario
- [ ] Usar CV para validación robusta
- [ ] Tunear hiperparámetros con Grid/Random Search
- [ ] Evaluar con múltiples métricas
- [ ] Visualizar matriz de confusión
- [ ] Graficar ROC y Precision-Recall
- [ ] Explicar con Feature Importance o SHAP
- [ ] Comparar múltiples modelos
- [ ] Elegir threshold según negocio

## Recursos

- [Imbalanced-learn](https://imbalanced-learn.org/)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Scikit-learn Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html)
- [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
