# Bloque 3 - Parte 1: Clasificación, Matriz de Confusión y Curva ROC

## 📚 Introducción Profesional

Bienvenidos al Bloque 3 de nuestro curso de Ciencia de Datos. En esta unidad, realizaremos una transición fundamental desde los modelos de **regresión** (que predicen valores continuos) hacia los modelos de **clasificación** (que asignan observaciones a categorías discretas).

### ¿Por Qué es Importante la Clasificación?

Los problemas de clasificación son omnipresentes en la práctica profesional: identificar clientes que abandonarán la plataforma (churn), detectar transacciones fraudulentas, diagnosticar enfermedades, clasificar correos como spam/no spam, o predecir si un préstamo será devuelto.

A diferencia de la regresión, donde nos interesa minimizar errores continuos, en clasificación debemos enfrentarnos a un nuevo desafío: **¿cómo sabemos si nuestro modelo está haciendo un buen trabajo cuando comete tanto falsos positivos como falsos negativos?**

### Objetivos de Aprendizaje

Al finalizar esta parte, serás capaz de:

1. **Comprender los fundamentos de la clasificación binaria y multiclase**
   - Diferencia entre regresión logística y regresión lineal
   - Probabilidades y decisiones de clasificación
   - El concepto de threshold (umbral de decisión)

2. **Dominar la matriz de confusión y sus métricas derivadas**
   - Interpretación de verdaderos positivos, falsos positivos, verdaderos negativos, falsos negativos
   - Precisión (Precision), Sensibilidad/Recall, Especificidad
   - F1-Score y por qué el accuracy no siempre es suficiente
   - Relaciones trade-off entre estas métricas

3. **Analizar y construir la curva ROC (Receiver Operating Characteristic)**
   - Concepto del área bajo la curva (AUC)
   - Interpretación visual del rendimiento del modelo
   - Selección óptima del threshold de decisión

4. **Aplicar algoritmos de clasificación supervisada**
   - Regresión Logística
   - Árboles de Decisión
   - Evaluación y comparación de modelos

## 📋 Conceptos Clave

### La Matriz de Confusión: Tu Herramienta Diagnóstica

La matriz de confusión es más que una tabla de números; es el **espejo del desempeño real** de tu clasificador:

```
                    Predicción Positiva    Predicción Negativa
Valor Real Positivo      TP (Acierto)       FN (Omisión)
Valor Real Negativo      FP (Falsa Alarma)  TN (Acierto correcto)
```

**¿Por qué te importa esta distinción?**
- En detección de cáncer, un **FN (falso negativo)** puede ser mortal
- En spam detection, un **FP (falso positivo)** molesta al usuario pero no mata
- En scoring crediticio, ambos tipos de error tienen consecuencias económicas diferentes

### Métricas Fundamentales

- **Sensibilidad (Recall)** = TP/(TP+FN): "De todos los positivos reales, ¿cuántos detecté?"
- **Precisión** = TP/(TP+FP): "De mis predicciones positivas, ¿cuántas fueron correctas?"
- **Especificidad** = TN/(TN+FP): "De todos los negativos reales, ¿cuántos identifiqué?"
- **F1-Score** = Media armónica de Precisión y Sensibilidad: "Balance entre precisión y cobertura"

### La Curva ROC: Visualizando Trade-offs

La curva ROC (Receiver Operating Characteristic) es tu **mapa de navegación** en el espacio de decisiones. Cada punto representa un threshold diferente:

- Eje Y: Tasa de Verdaderos Positivos (Sensibilidad)
- Eje X: Tasa de Falsos Positivos (1 - Especificidad)

**El AUC (Area Under Curve):**
- AUC = 0.5: Tu modelo es aleatorio (inútil)
- AUC = 1.0: Clasificación perfecta
- AUC > 0.8: Modelo excelente
- AUC = 0.7: Modelo aceptable
- AUC < 0.6: Modelo pobre

## 📁 Estructura del Proyecto

```
Parte1º/
├── notebooks/              # Jupyter notebooks con análisis y ejercicios
├── data/                   # Datasets de clasificación (churn, abandono de clientes)
├── docs/                   # Guía rápida y materiales de referencia
├── requirements.txt        # Dependencias Python
├── environment.yml         # Entorno conda
└── README.md              # Este archivo
```

## 🚀 Cómo Empezar

### Opción 1: Usando pip (recomendado para Windows)
```bash
pip install -r requirements.txt
```

### Opción 2: Usando Conda
```bash
conda env create -f environment.yml
conda activate big_data_bloque3_parte1
```

## 📚 Contenido de los Notebooks

- **Enunciado**: Descripción de problemas y preguntas a resolver
- **Ejercicio Resuelto**: Soluciones con explicaciones paso a paso
- **Datos**: Dataset de abandono de clientes (churn) de mayo 2026

## 🎯 Metodología de Aprendizaje

1. **Lectura del enunciado**: Entiende qué pregunta queremos responder
2. **Exploración de datos**: Familiarízate con el dataset
3. **Modelado**: Entrena clasificadores básicos
4. **Evaluación**: Construye matriz de confusión y curva ROC
5. **Interpretación**: ¿Qué significa realmente el AUC de 0.85?
6. **Optimización**: Ajusta threshold, experimenta con algoritmos

## 📖 Materiales de Referencia

Consulta la carpeta `docs/` para obtener:
- Guía rápida de scikit-learn para clasificación
- Fórmulas y definiciones de métricas
- Sugerencias de temporalización
- Preguntas frecuentes

## 💡 Consejos Prácticos

- **No confundas exactitud con rendimiento**: Un modelo que predice todo como "no churn" puede tener 95% accuracy pero 0% sensibilidad
- **Siempre visualiza la matriz de confusión**: Los números crudos mieneten; la visualización aclara
- **Ajusta el threshold según tu negocio**: A menudo no es 0.5
- **Compara siempre con baselines**: ¿Es mi modelo mejor que predecir siempre la clase más frecuente?

---

**Profesor**: Unidad de Ciencia de Datos  
**Nivel**: Intermediate  
**Duración estimada**: 4-6 horas
