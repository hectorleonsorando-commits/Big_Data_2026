# Notebooks - Bloque 3, Parte 2: Clasificación Avanzada

## Descripción

En esta carpeta encontrarás los Jupyter notebooks para técnicas avanzadas de clasificación y machine learning en producción.

## Notebooks Disponibles

### 02_Bloque_III_Clasificacion_Avanzada_ENUNCIADO.ipynb
**Propósito**: Ejercicios de clasificación avanzada

Este notebook presenta:
1. Comparación de múltiples algoritmos (Logística, Random Forest, Gradient Boosting)
2. Evaluación de rendimiento en datos realistas
3. Manejo de datos desbalanceados
4. Optimización de hiperparámetros
5. Técnicas de validación robusta

**Temas cubiertos:**
- Regresión Logística como baseline
- Random Forest classifier
- Gradient Boosting
- Cross-validation estratificada
- Métricas multiples (AUC, Precision, Recall, F1)

**Recomendación**: Comienza aquí. Intenta resolver los problemas antes de ver las soluciones.

### 02_Bloque_III_Clasificacion_Avanzada_RESUELTO.ipynb
**Propósito**: Soluciones profesionales con mejores prácticas

Este notebook contiene:
1. Implementaciones completas de múltiples modelos
2. Pipeline sklearn correctamente implementado
3. Manejo profesional de desbalanceo (SMOTE, class weights)
4. Grid Search para optimización
5. Visualizaciones profesionales
6. Interpretabilidad (Feature Importance)
7. Análisis comparativo de resultados

**Contenido especial:**
- Funciones auxiliares reutilizables
- Validación cruzada estratificada
- Comparación lado a lado de modelos
- Recomendaciones prácticas

**Recomendación**: Consulta después de intentar resolver o para aprender implementación profesional.

## Flujo de Trabajo Recomendado

```
1. Revisa Parte 1 si necesitas refrescar conceptos fundamentales
   ↓
2. Lee el enunciado (ENUNCIADO.ipynb)
   ↓
3. Intenta resolver los problemas por tu cuenta
   ↓
4. Consulta /docs/GUIA_RAPIDA.md cuando necesites ayuda de código
   ↓
5. Compara con las soluciones (RESUELTO.ipynb)
   ↓
6. Experimenta: cambia hiperparámetros, prueba nuevos algoritmos
   ↓
7. Reflexiona: ¿por qué funcionó mejor o peor?
```

## Temas Cubiertos

### Algoritmos
- ✅ Regresión Logística (revisión)
- ✅ Árboles de Decisión
- ✅ Random Forest
- ✅ Gradient Boosting
- ✅ SVM (Support Vector Machines)

### Validación y Evaluación
- ✅ Cross-validation estratificada
- ✅ Métricas múltiples
- ✅ ROC curves
- ✅ Precision-Recall curves
- ✅ Curvas de aprendizaje

### Manejo de Desbalanceo
- ✅ Detección de desbalanceo
- ✅ SMOTE (Synthetic Minority Over-sampling)
- ✅ Class weights
- ✅ Undersampling/Oversampling

### Optimización
- ✅ Grid Search
- ✅ Random Search
- ✅ Tuning de hiperparámetros
- ✅ Early stopping

### Interpretabilidad
- ✅ Feature Importance
- ✅ Permutation Importance
- ✅ SHAP values (introducción)

## Consejos para Máximo Aprendizaje

### Antes de ejecutar código
1. **Lee las instrucciones** completamente
2. **Piensa en la solución** antes de escribir código
3. **Anticipa resultados** antes de ejecutar

### Durante la ejecución
1. **No copies/pegues**: Entiende cada línea
2. **Experimenta**: Cambia valores, observa efectos
3. **Visualiza**: Usa gráficos para intuición
4. **Documenta**: Comenta tu código

### Después de resolver
1. **Reflexiona**: ¿Por qué funcionó?
2. **Compara**: ¿Mi solución vs la profesional?
3. **Itera**: ¿Cómo mejora más?

## Errores Comunes a Evitar

❌ **Olvidar stratify en train/test split**
```python
# ❌ Malo
train_test_split(X, y, test_size=0.2)

# ✅ Bien
train_test_split(X, y, test_size=0.2, stratify=y)
```

❌ **Escalar después del split**
```python
# ❌ Malo: Information leak
scaler.fit(X)  # Usa TODO
X_scaled = scaler.transform(X)

# ✅ Bien: Fit solo con train
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

❌ **Usar Accuracy como única métrica en datos desbalanceados**
```python
# ❌ Malo
print(f"Accuracy: {model.score(X_test, y_test)}")

# ✅ Bien
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

❌ **Aplicar SMOTE antes del split**
```python
# ❌ Malo: Data leakage
X_sm, y_sm = SMOTE().fit_resample(X, y)
train_test_split(X_sm, y_sm)

# ✅ Bien: SMOTE solo en train
train_test_split(X, y, stratify=y)
X_sm, y_sm = SMOTE().fit_resample(X_train, y_train)
```

❌ **Grid Search sin cross-validation**
```python
# ❌ Malo
model.fit(X_train, y_train)
best_params = grid_search.best_params_

# ✅ Bien
grid_search = GridSearchCV(model, params, cv=5)
grid_search.fit(X_train, y_train)
```

❌ **Confundir Feature Importance**
```python
# Diferentes métodos dan resultados diferentes:
# - model.feature_importances_ (built-in)
# - permutation_importance (más confiable)
# - shap_values (interpretabilidad local)
```

## Comparativa Rápida: Algoritmos

| Algoritmo | Velocidad | Interpretable | Rendimiento | Cuándo |
|-----------|-----------|---------------|-------------|--------|
| Logística | ⚡⚡⚡ | ⭐⭐⭐ | ⭐⭐ | Baseline, urgencia |
| Árbol | ⚡⚡ | ⭐⭐⭐ | ⭐⭐⭐ | Exploración |
| Random Forest | ⚡ | ⭐⭐ | ⭐⭐⭐⭐ | Producción |
| Gradient Boosting | ❌ | ⭐ | ⭐⭐⭐⭐⭐ | Máximo rendimiento |

## Metas por Notebook

### ENUNCIADO
Completar:
- [ ] Cargar y explorar datos
- [ ] Entrenar 3+ modelos diferentes
- [ ] Calcular métricas completas
- [ ] Visualizar matriz de confusión
- [ ] Comparar rendimientos
- [ ] Aplicar técnica de rebalanceo
- [ ] Optimizar mejor modelo
- [ ] Documentar hallazgos

### RESUELTO (Aprender)
Entender:
- [ ] Pipeline sklearn profesional
- [ ] Manejo correcto de datos desbalanceados
- [ ] Grid Search implementation
- [ ] Validación robusta
- [ ] Feature Importance vs SHAP
- [ ] Comparación justa de modelos
- [ ] Visualización profesional

## Extensiones Propuestas

Una vez domines los notebooks:

1. **Experimenta**: Prueba otros algoritmos (SVM, XGBoost)
2. **Hipertunea**: Busca parámetros óptimos más agresivamente
3. **Explica**: Aprende SHAP values en profundidad
4. **Ensemble**: Combina múltiples modelos
5. **Deploya**: Guarda el modelo en pickle
6. **Documenta**: Crea un reporte profesional

## Recursos Complementarios

- [Scikit-learn Classification Guide](https://scikit-learn.org/stable/modules/classification.html)
- [Imbalanced-learn Documentation](https://imbalanced-learn.org/)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Random Forest Explained](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)
- [Gradient Boosting Explained](https://towardsdatascience.com/gradient-boosting-explained-9b87f63b8e46)

---

**Duración estimada**: 4-5 horas de trabajo activo  
**Nivel**: Advanced Intermediate  
**Requisitos**: Bloque 3 Parte 1 completado
