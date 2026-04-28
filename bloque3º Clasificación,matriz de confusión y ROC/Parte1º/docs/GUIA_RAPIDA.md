# GUIA_RAPIDA.md - Bloque 3, Parte 1: Clasificación y ROC

## Referencia Rápida de Código

### 1. Preparación de Datos

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Cargar datos
df = pd.read_csv('clientes_abandono_mayo_2026.csv')

# Separar features y target
X = df.drop('Churn', axis=1)  # Features
y = df['Churn']               # Target

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Escalar (si es necesario)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 2. Entrenar Regresión Logística

```python
from sklearn.linear_model import LogisticRegression

# Crear modelo
model = LogisticRegression(random_state=42, max_iter=1000)

# Entrenar
model.fit(X_train_scaled, y_train)

# Predicciones
y_pred = model.predict(X_test_scaled)           # Clases: 0 o 1
y_pred_proba = model.predict_proba(X_test_scaled)  # Probabilidades

# Acceder a probabilidad de clase 1
y_pred_proba_class1 = y_pred_proba[:, 1]
```

### 3. Matriz de Confusión

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Calcular matriz
cm = confusion_matrix(y_test, y_pred)
print(cm)
# [[TN   FP]
#  [FN   TP]]

# Visualizar
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()

# Acceder a valores
tn, fp, fn, tp = cm.ravel()
print(f"TP: {tp}, FP: {fp}, FN: {fn}, TN: {tn}")
```

### 4. Métricas de Clasificación

```python
from sklearn.metrics import (
    precision_score, recall_score, f1_score,
    accuracy_score, classification_report, roc_auc_score
)

# Calcular métricas individuales
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba_class1)

print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-Score: {f1:.3f}")
print(f"Accuracy: {accuracy:.3f}")
print(f"AUC: {auc:.3f}")

# Reporte completo
print(classification_report(y_test, y_pred))
```

### 5. Curva ROC

```python
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Calcular ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba_class1)
roc_auc = auc(fpr, tpr)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, 
         label=f'ROC curve (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.show()

# Encontrar threshold óptimo (Youden's J statistic)
j_scores = tpr - fpr
optimal_idx = np.argmax(j_scores)
optimal_threshold = thresholds[optimal_idx]
print(f"Threshold óptimo: {optimal_threshold:.3f}")
```

### 6. Usar Threshold Personalizado

```python
# Predicciones con threshold personalizado
threshold = 0.5
y_pred_custom = (y_pred_proba_class1 >= threshold).astype(int)

# Recalcular métricas con nuevo threshold
precision_custom = precision_score(y_test, y_pred_custom)
recall_custom = recall_score(y_test, y_pred_custom)
f1_custom = f1_score(y_test, y_pred_custom)

print(f"Con threshold {threshold}:")
print(f"  Precision: {precision_custom:.3f}")
print(f"  Recall: {recall_custom:.3f}")
print(f"  F1: {f1_custom:.3f}")
```

## Interpretación Rápida

### Matriz de Confusión

```
                    Predicción Negativa    Predicción Positiva
Real Negativo              TN (acierto)        FP (falsa alarma)
Real Positivo              FN (omisión)        TP (acierto)
```

### Definiciones de Métricas

| Métrica | Fórmula | Interpretación |
|---------|---------|----------------|
| **Precision** | TP/(TP+FP) | De los que predije positivos, ¿cuántos fueron correctos? |
| **Recall** | TP/(TP+FN) | De los positivos reales, ¿cuántos detecté? |
| **F1-Score** | 2×(P×R)/(P+R) | Media armónica de precision y recall |
| **Accuracy** | (TP+TN)/(Total) | % global de aciertos (cuidado: engañoso) |
| **Specificity** | TN/(TN+FP) | De los negativos reales, ¿cuántos detecté? |

### Cuándo Usar Cada Métrica

- **Precision**: Cuando FP es costoso (spam: falso positivo molesta)
- **Recall**: Cuando FN es costoso (cáncer: falso negativo es peligroso)
- **F1**: Cuando ambos errores importan igualmente
- **AUC**: Comparación general, robusta a threshold

## Interpretación de ROC

- **Curva cercana a esquina superior-izquierda**: Modelo excelente
- **Curva diagonal**: Modelo aleatorio (AUC = 0.5)
- **Curva bajo la diagonal**: Modelo invertido (necesita inversión)

### Valores de AUC

- AUC > 0.90: Excelente
- AUC > 0.80: Muy bueno
- AUC > 0.70: Bueno
- AUC > 0.60: Aceptable
- AUC ≤ 0.60: Pobre

## Errores Comunes

❌ **Usar accuracy en datos desbalanceados**
- Si 95% es no-churn, predecir siempre "no-churn" da 95% accuracy
- Usa precision/recall/F1 en su lugar

❌ **Confundir TP con TN**
- TP = Positivo real predicho positivo (acierto en la clase de interés)
- TN = Negativo real predicho negativo (acierto en la otra clase)

❌ **Threshold fijo de 0.5**
- A menudo 0.5 no es óptimo
- Usa la curva ROC para elegir según tu negocio

❌ **No estratificar en split**
```python
# ❌ Malo
train_test_split(X, y, test_size=0.2)

# ✅ Bien
train_test_split(X, y, test_size=0.2, stratify=y)
```

❌ **Escalar después del split**
```python
# ❌ Malo: Data leakage
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Usa TODO X
X_train, X_test = train_test_split(X_scaled)

# ✅ Bien: Ajustar solo con train
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## Template Completo

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, classification_report, 
                            roc_curve, auc, precision_score, recall_score)
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Escalar
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# 4. Entrenar
model = LogisticRegression(max_iter=1000)
model.fit(X_train_s, y_train)

# 5. Predecir
y_pred = model.predict(X_test_s)
y_pred_proba = model.predict_proba(X_test_s)[:, 1]

# 6. Evaluar
print(classification_report(y_test, y_pred))
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
auc_score = auc(fpr, tpr)
print(f"AUC: {auc_score:.3f}")

# 7. Visualizar
plt.plot(fpr, tpr, label=f'ROC (AUC={auc_score:.3f})')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend()
plt.show()
```

## Recursos Rápidos

- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Confusion Matrix Explained](https://en.wikipedia.org/wiki/Confusion_matrix)
- [ROC Curve Explained](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
