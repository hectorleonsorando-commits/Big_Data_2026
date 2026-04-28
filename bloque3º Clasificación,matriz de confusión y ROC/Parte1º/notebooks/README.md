# Notebooks - Bloque 3, Parte 1

## Descripción

En esta carpeta encontrarás los Jupyter notebooks principales para el aprendizaje del Bloque 3, Parte 1.

## Notebooks Disponibles

### 01_Bloque_III_Clasificacion_Matriz_ROC_Enunciado.ipynb
**Propósito**: Enunciado del problema y preguntas guiadas

Este notebook presenta:
1. Contexto del negocio (churn de clientes)
2. Carga y exploración inicial de datos
3. Preguntas específicas a responder
4. Espacios para que escribas tu código

**Recomendación**: Comienza aquí. Intenta resolver los problemas antes de ver las soluciones.

### 01_Bloque_III_Ejercicio_Resuelto.ipynb
**Propósito**: Soluciones con explicaciones detalladas

Este notebook contiene:
1. Soluciones completas a cada pregunta
2. Comentarios y explicaciones de decisiones
3. Visualizaciones de resultados
4. Interpretación de matrices de confusión y curvas ROC

**Recomendación**: Consulta después de intentar resolver o cuando necesites ayuda conceptual.

## Flujo de Trabajo Recomendado

```
1. Lee el enunciado (Enunciado.ipynb)
   ↓
2. Intenta resolver los problemas por tu cuenta
   ↓
3. Compara con las soluciones (Ejercicio_Resuelto.ipynb)
   ↓
4. Experimenta: cambia parámetros, prueba nuevos algoritmos
   ↓
5. Reflexiona: ¿por qué funcionó o no?
```

## Temas Cubiertos

- ✅ Regresión Logística
- ✅ Matriz de Confusión
- ✅ Métricas de Clasificación (Precision, Recall, F1-Score)
- ✅ Curva ROC y AUC
- ✅ Selección de Threshold

## Consejos para Máximo Aprendizaje

1. **No copies/pegues código**: Entiende cada línea
2. **Experimenta**: Cambia valores y observa qué sucede
3. **Visualiza**: Usa gráficos para entender mejor
4. **Documenta**: Comenta tu código y explicaciones
5. **Debuggea**: Usa print() y pdb para entender el flujo

## Errores Comunes a Evitar

- ❌ Confundir TP con TN en la matriz
- ❌ Usar Accuracy como única métrica
- ❌ No estratificar el split en datos desbalanceados
- ❌ Usar threshold fijo de 0.5 sin justificación
- ❌ No normalizar/escalar features antes de algunos algoritmos

## Próximos Pasos

Cuando domines esta parte:
- Procede a la Parte 2 para técnicas avanzadas
- Experimenta con otros algoritmos (Decision Trees, SVM)
- Aplica lo aprendido a tus propios datasets
