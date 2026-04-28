# Data - Bloque 3, Parte 1

## Descripción del Dataset

### clientes_abandono_mayo_2026.csv

Dataset sintético que contiene información de clientes y su estado de churn (abandono) de un servicio de telecomunicaciones durante mayo de 2026.

**Variables principales:**
- ID de cliente
- Datos demográficos (edad, género, ubicación)
- Características del servicio (tipo de contrato, antigüedad, servicios adicionales)
- Comportamiento de uso (minutos de llamadas, datos consumidos)
- Información de pago (monto mensual, total gastado)
- **Target**: Churn (0 = se quedó, 1 = abandonó)

**Tamaño**: ~5,000 observaciones

Este dataset ha sido diseñado para que explores patrones reales de churn, con clases desbalanceadas y relaciones complejas entre variables.

## Uso en los Notebooks

- **Exploración**: Análisis descriptivo de la población de clientes
- **Modelado**: Entrenamiento de clasificadores
- **Evaluación**: Construcción de matriz de confusión y ROC
