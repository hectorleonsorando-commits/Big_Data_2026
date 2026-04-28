# Bloque 3: Clasificación, Matriz de Confusión y Curva ROC

## 📋 Descripción General del Bloque

El Bloque 3 introduce el **aprendizaje supervisado de clasificación**, una de las aplicaciones más importantes en ciencia de datos. Pasaremos de predecir valores continuos (regresión) a asignar observaciones a categorías discretas (clasificación).

Este bloque está dividido en dos partes:

### Parte 1: Fundamentos
- Regresión logística y conceptos básicos
- Matriz de confusión y sus interpretaciones
- Métricas de evaluación (Precision, Recall, F1-Score)
- Curva ROC y AUC
- Selección del threshold de decisión

### Parte 2: Técnicas Avanzadas
- Manejo de datos desbalanceados
- Clasificación multiclase
- Validación cruzada estratificada
- Optimización de hiperparámetros
- Interpretabilidad de modelos (SHAP values)
- Ensemble methods (Random Forest, Gradient Boosting)

## 📁 Estructura del Bloque

```
bloque3º Clasificación,matriz de confusión y ROC/
├── Parte1º/
│   ├── notebooks/          # Ejercicios: enunciado y soluciones
│   ├── data/               # Dataset de churn de clientes
│   ├── docs/               # Guías y referencias
│   ├── requirements.txt    # Dependencias
│   ├── environment.yml     # Entorno conda
│   └── README.md          # Guía de la Parte 1
├── Parte2º/
│   ├── notebooks/          # Ejercicios avanzados
│   ├── data/               # Datasets
│   ├── docs/               # Referencias avanzadas
│   ├── requirements.txt    # Dependencias
│   ├── environment.yml     # Entorno conda
│   └── README.md          # Guía de la Parte 2
└── README.md              # Este archivo
```

## 🚀 Cómo Comenzar

### Paso 1: Configura tu entorno

**Opción A (Recomendado para Windows):**
```bash
cd Parte1º
pip install -r requirements.txt
```

**Opción B (Conda):**
```bash
cd Parte1º
conda env create -f environment.yml
conda activate big_data_bloque3_parte1
```

### Paso 2: Abre Jupyter
```bash
jupyter lab
```

### Paso 3: Comienza con la Parte 1
1. Abre `Parte1º/notebooks/01_Bloque_III_Clasificacion_Matriz_ROC_Enunciado.ipynb`
2. Trabaja a través de los ejercicios
3. Consulta `Ejercicio_Resuelto.ipynb` cuando sea necesario

### Paso 4 (Opcional): Procede a la Parte 2
Una vez domines los fundamentos, pasa a técnicas avanzadas.

## 📚 Contenido Detallado

### Parte 1 - Fundamentos de Clasificación

#### Conceptos Clave
- **Clasificación Binaria**: Dos clases (churn/no-churn)
- **Matriz de Confusión**: Tabla de verdaderos/falsos positivos/negativos
- **Trade-offs**: Precision vs Recall, Sensibilidad vs Especificidad
- **ROC Curve**: Visualización de rendimiento a diferentes thresholds
- **AUC (Area Under Curve)**: Métrica única de desempeño

#### Skills que Desarrollarás
- Entrenar un clasificador logístico
- Calcular e interpretar métricas de clasificación
- Visualizar y analizar matrices de confusión
- Graficar e interpretar curvas ROC
- Elegir el threshold óptimo según contexto de negocio

### Parte 2 - Clasificación Avanzada

#### Conceptos Clave
- **Desbalanceo de Clases**: Cuando una clase es mucho más frecuente
- **SMOTE**: Síntesis de muestras de la clase minoritaria
- **Cross-Validation**: Validación robusta
- **Grid Search**: Búsqueda sistemática de hiperparámetros
- **Feature Importance**: Identificación de variables clave
- **SHAP**: Explicabilidad de predicciones individuales
- **Ensemble Methods**: Combinación de múltiples modelos

#### Skills que Desarrollarás
- Detectar y resolver problemas de desbalanceo
- Implementar validación cruzada estratificada
- Optimizar hiperparámetros automáticamente
- Usar Random Forest y Gradient Boosting
- Explicar por qué un modelo hizo una predicción

## 🎯 Aplicaciones Prácticas

### Casos de Uso Reales

1. **Churn Prediction** (nuestro caso)
   - Identificar clientes en riesgo de abandono
   - Permite intervención preventiva

2. **Detección de Fraude**
   - Transacciones fraudulentas vs legítimas
   - FN es peligroso (fraude no detectado)
   - FP es costoso (cliente rechazado injustamente)

3. **Diagnóstico Médico**
   - Enfermo vs Sano
   - Equilibrio crítico entre detectar todas las enfermedades y no alarmar falsamente

4. **Spam Detection**
   - Correo válido vs Spam
   - FP molesto, FN no es crítico

5. **Aprobación de Préstamos**
   - Crédito aprobado vs rechazado
   - Decisiones con impacto económico

## 💡 Conceptos Fundamentales a Recordar

### Métrica | Qué Mide | Cuándo Usarla
---|---|---
**Accuracy** | % global de aciertos | Solo si clases balanceadas
**Precision** | De positivos predichos, cuántos correctos | Importa no falsos positivos
**Recall/Sensitivity** | De positivos reales, cuántos detecté | Importa no falsos negativos
**Specificity** | De negativos reales, cuántos detecté | Evaluar tasa de falsos positivos
**F1-Score** | Balance precision-recall | Resumen single metric
**AUC-ROC** | Rendimiento general a todos los thresholds | Comparación robusta de modelos

### Interpretación Rápida de AUC

- **AUC = 1.0**: Perfección (poco realista)
- **AUC > 0.9**: Excelente
- **AUC > 0.8**: Muy bueno
- **AUC > 0.7**: Bueno
- **AUC = 0.5**: Aleatorio (inútil)
- **AUC < 0.5**: Peor que aleatorio (revisa el modelo)

## 📖 Recursos de Referencia

### Documentación Oficial
- [Scikit-learn Classification](https://scikit-learn.org/stable/modules/classification.html)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Imbalanced-learn](https://imbalanced-learn.org/)

### Artículos y Tutoriales
- Understanding ROC Curves
- Confusion Matrix Explained
- Handling Imbalanced Datasets

### Videos Recomendados
- Logistic Regression Intuition
- ROC Curve Explained
- SMOTE and Resampling Techniques

## 🔧 Herramientas y Librerías

| Librería | Uso |
|----------|-----|
| **scikit-learn** | Algoritmos, métricas, validación |
| **pandas** | Manipulación de datos |
| **numpy** | Operaciones numéricas |
| **matplotlib/seaborn** | Visualización |
| **imbalanced-learn** | Técnicas de resampling |
| **shap** | Explicabilidad |
| **jupyter** | Entorno de programación |

## 📊 Ejemplos de Outputs Esperados

### Matriz de Confusión
```
                    Predicción: No Churn    Predicción: Churn
Real: No Churn              940                     60
Real: Churn                  40                    160
```

### Interpretación:
- **TP (160)**: Clientes que abandonaban y detectamos
- **TN (940)**: Clientes que se quedaban y clasificamos correctamente
- **FP (60)**: Clientes que se quedaban pero predijimos que abandonaban
- **FN (40)**: Clientes que abandonaban pero no detectamos

## 🎓 Pedagogía

### Enfoque de Enseñanza

1. **Conceptual First**: Entiende qué y por qué
2. **Hands-On**: Implementa desde cero
3. **Application**: Aplica a problemas reales
4. **Reflection**: Reflexiona sobre resultados

### Cómo Aprender Mejor

✅ **Haz**: Ejecuta código, experimenta  
✅ **Visualiza**: Genera gráficos, observa patrones  
✅ **Explica**: Resume lo que aprendiste en tus palabras  
✅ **Compara**: Contrasta diferentes enfoques  

❌ **No hagas**: Solo leer sin ejecutar  
❌ **No hagas**: Copiar-pegar sin entender  
❌ **No hagas**: Memorizar fórmulas sin intuición  

## 🏆 Criterios de Éxito

Al completar este bloque, deberías poder:

- [ ] Explicar la diferencia entre precision y recall
- [ ] Construir e interpretar una matriz de confusión
- [ ] Graficar y analizar una curva ROC
- [ ] Elegir el threshold óptimo para tu problema
- [ ] Identificar si tus datos están desbalanceados
- [ ] Aplicar técnicas para manejar desbalanceo
- [ ] Comparar múltiples modelos de clasificación
- [ ] Explicar por qué tu modelo hizo una predicción

## 📝 Notas Importantes

- **Siempre explora primero**: EDA es crucial antes de modelar
- **Nunca asumas balance**: Verifica la distribución de clases
- **Normaliza si es necesario**: Algunos algoritmos lo requieren
- **Valida correctamente**: Usa stratified K-fold si hay desbalanceo
- **Piensa en el negocio**: El mejor modelo es el útil para tu problema

---

**Profesor**: Unidad de Ciencia de Datos  
**Duración Total**: 10-12 horas  
**Nivel**: Intermediate  
**Requisitos**: Haber completado Bloques 1 y 2
