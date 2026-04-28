# Data - Bloque 3, Parte 2

## Descripción de los Datasets

### clientes_clasificacion.csv

Dataset de clientes con enfoque en técnicas avanzadas de clasificación. Contiene información de clientes de un servicio de telecomunicaciones.

**Estructura del Dataset:**
- **N de observaciones**: ~10,000 registros
- **N de features**: 15-20 variables de cliente
- **Target**: `abandono` (0 = cliente activo, 1 = cliente ha abandonado)

**Características:**

Variables Demográficas:
- Edad
- Género
- Ubicación

Variables de Servicio:
- Antigüedad (meses como cliente)
- Tipo de contrato
- Servicios adicionales (internet, telefonía, etc.)
- Facturación mensual

Variables de Comportamiento:
- Total gastado
- Llamadas al soporte técnico
- Cambios en plan

**Desbalanceo**: Este dataset tiene una distribución realista de churn (~25% abandono), lo que lo hace ideal para practicar técnicas de manejo de desbalanceo sin ser extremo.

**Características Especiales:**
- Variables categóricas y numéricas
- Algunos valores faltantes intencionales
- Relaciones no-lineales entre variables
- Multicolinealidad moderada

## Uso en los Notebooks

### Notebook del Enunciado
- Exploración inicial y análisis descriptivo
- Comparación de múltiples algoritmos
- Aplicación de técnicas de rebalanceo
- Optimización de hiperparámetros

### Notebook Resuelto
- Soluciones completas
- Mejores prácticas implementadas
- Visualizaciones profesionales
- Interpretación de resultados

## Notas Importantes

1. **Preprocesamiento**: Algunos features requieren codificación (one-hot, label encoding)
2. **Escalado**: Recomendado para ciertos algoritmos (SVM, Logística)
3. **Desbalanceo**: El ~25% de churn es realista y educativo
4. **Validación**: Usa stratified split/CV para mantener proporción

## Recomendaciones

- **Para principiantes**: Comienzaen el enunciado intentando resolver
- **Para avanzados**: Experimenta con diferentes técnicas de rebalanceo
- **Para competición**: Intenta alcanzar AUC > 0.85

## Reproducibilidad

El dataset es determinista y reproducible. Para generar variaciones:
```python
# Shuffle stratificado
X_sample = X.sample(frac=0.8, random_state=42)
```

---

**Creación**: Mayo 2026  
**Propósito**: Educativo - Bloque 3, Parte 2  
**Licencia**: Uso educativo interno
