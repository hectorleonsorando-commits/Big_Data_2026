# Bloque 4: Clustering, Silhouette y PCA

## 📋 Descripción General del Bloque

El Bloque 4 introduce el **aprendizaje no supervisado**, el cambio paradigmático más importante de este curso. Por primera vez, descubriremos patrones en datos **sin etiquetas previas**.

### De Supervisado a No Supervisado

**Bloques 1-3**: "Predice X dado Y" (Tienes todas las respuestas)  
**Bloque 4**: "¿Cuál es la estructura de los datos?" (Descubres las respuestas)

### Aplicaciones Reales

- **Segmentación de clientes**: Identificar grupos para marketing diferenciado
- **Recomendaciones**: Netflix agrupa películas similares
- **Detección de anomalías**: Transacciones que no encajan
- **Análisis genómico**: Grupos de genes relacionados
- **Análisis de texto**: Clustering de documentos

## 📁 Estructura del Bloque

```
Bloque4º Clustering, silhouette y PCA/
├── Parte1º/
│   ├── notebooks/          # Ejercicios: K-Means fundamental
│   ├── data/               # Dataset segmentación
│   ├── docs/               # GUIA_RAPIDA, referencias
│   ├── requirements.txt    # Dependencias
│   ├── environment.yml     # Entorno conda
│   └── README.md          # Guía Parte 1
├── Parte2º/
│   ├── notebooks/          # Ejercicios: Clustering avanzado
│   ├── data/               # Datasets complejos
│   ├── docs/               # GUIA_RAPIDA avanzada, análisis ROI
│   ├── requirements.txt    # Dependencias
│   ├── environment.yml     # Entorno conda
│   └── README.md          # Guía Parte 2
└── README.md              # Este archivo
```

## 🚀 Cómo Comenzar

### Opción 1: Usando pip (recomendado para Windows)
```bash
cd Parte1º
pip install -r requirements.txt
jupyter lab
```

### Opción 2: Usando Conda
```bash
cd Parte1º
conda env create -f environment.yml
conda activate big_data_bloque4_parte1
jupyter lab
```

## 📚 Contenido Detallado

### Parte 1 - Fundamentals (K-Means, Silhouette, PCA)

#### Conceptos Clave
- **K-Means**: Algoritmo de clustering más popular
- **Silhouette Score**: Métrica para elegir K óptimo
- **PCA**: Visualización de clusters en 2D/3D
- **Escalado**: Obligatorio para distancia Euclideana

#### Skills que Desarrollarás
- Escalar datos correctamente
- Entrenar K-Means con diferentes K
- Elegir K óptimo usando Silhouette
- Visualizar clusters con PCA
- Perfilar clusters significativamente

#### Responde Preguntas
1. ¿Cuántos clusters naturales tiene mi dataset?
2. ¿Qué características definen cada cluster?
3. ¿Qué nombres significativos asigno?
4. ¿Qué acciones empresariales tomo?

### Parte 2 - Advanced (Validación, Jerárquico, ROI)

#### Conceptos Clave
- **Clustering Jerárquico**: Alternativa exploratoria
- **Dendrogramas**: Visualización de relaciones
- **Múltiples Métricas**: Davies-Bouldin, Calinski-Harabasz
- **Feature Importance**: Variables que crean clusters
- **Análisis ROI**: Valor de la segmentación

#### Skills que Desarrollarás
- Validar clusters técnicamente Y empresarialmente
- Comparar múltiples algoritmos
- Analizar importancia de features
- Calcular ROI de segmentación
- Diseñar estrategias diferenciadas

#### Responde Preguntas
1. ¿Mi clustering es robusto técnicamente?
2. ¿Tiene sentido desde perspectiva empresarial?
3. ¿Cuál es el impacto financiero esperado?
4. ¿Qué estrategia aplicar a cada segmento?

## 💡 Conceptos Fundamentales

### K-Means: El Algoritmo

```
1. Elige K (número de clusters)
2. Inicializa K centros aleatoriamente
3. Asigna cada punto al centro más cercano
4. Recalcula centros
5. Repite 3-4 hasta convergencia
```

**Ventajas**: Rápido, simple, escalable  
**Desventajas**: K fijo, sensible a outliers, óptimo local

### Silhouette Score: Métrica

```
Mide qué tan cohesionado está cada cluster
Rango: -1 (malo) a 1 (perfecto)
Interpretación:
- > 0.7: Excelente
- 0.5-0.7: Bueno
- < 0.3: Débil
```

### PCA: Visualización

```
Reduce dimensiones manteniendo varianza
PC1 = dirección de máxima varianza
PC2 = dirección ortogonal siguiente
Permite visualizar en 2D aunque hayas 50 features
```

## 🏆 Criterios de Éxito del Bloque

Al completar Bloque 4, podrás:

**Parte 1**:
- [ ] Explicar diferencia entre supervisado y no supervisado
- [ ] Escalar datos correctamente
- [ ] Entrenar K-Means
- [ ] Calcular Silhouette Score
- [ ] Usar PCA para visualización
- [ ] Nombrar clusters significativamente

**Parte 2**:
- [ ] Validar clusters con múltiples métricas
- [ ] Usar clustering jerárquico
- [ ] Analizar feature importance
- [ ] Calcular ROI de segmentación
- [ ] Diseñar estrategias por cluster
- [ ] Presentar a stakeholders no-técnicos

## 📊 Workflow Profesional de Clustering

```
1. EXPLORACIÓN
   └─ ¿Qué problema empresarial resuelve clustering?

2. PREPARACIÓN
   ├─ Seleccionar features relevantes
   ├─ Escalar (StandardScaler)
   └─ Verificar valores faltantes

3. EXPERIMENTACIÓN
   ├─ Probar K=2,3,4,5...
   ├─ Calcular Silhouette Score
   ├─ Visualizar con PCA
   └─ Elegir K óptimo

4. VALIDACIÓN TÉCNICA
   ├─ Silhouette Score
   ├─ Davies-Bouldin Index
   └─ Calinski-Harabasz Index

5. VALIDACIÓN EMPRESARIAL
   ├─ ¿Tiene sentido el clustering?
   ├─ ¿Puedo actuar diferenciado?
   └─ ¿Vale la pena?

6. ANÁLISIS PROFUNDO
   ├─ Feature importance
   ├─ Análisis de perfiles
   └─ Identificar outliers

7. ESTRATEGIA
   ├─ Definir acciones por cluster
   ├─ Calcular ROI esperado
   └─ Proponer presupuesto

8. IMPLEMENTACIÓN
   └─ Integrar en sistemas de negocio
```

## 🎯 Flujo de Aprendizaje

```
PARTE 1: Fundamentos
├─ Lección: K-Means, Silhouette, PCA
├─ Ejercicio: Segmentar dataset
├─ Validación: ¿K óptimo?
└─ Resultado: 3-4 clusters interpretables

       ↓↓↓

PARTE 2: Avanzado
├─ Lección: Jerárquico, Validación, ROI
├─ Ejercicio: Análisis profundo
├─ Validación: ¿Tiene sentido empresarialmente?
└─ Resultado: Estrategias diferenciadas
```

## 💻 Tecnologías

| Librería | Uso |
|----------|-----|
| **scikit-learn** | K-Means, PCA, métricas |
| **pandas** | Manipulación de datos |
| **numpy** | Operaciones numéricas |
| **matplotlib/seaborn** | Visualización |
| **scipy** | Clustering jerárquico |

## 📖 Materiales de Referencia

- Parte 1º README: Conceptos y ejemplos
- Parte 2º README: Análisis avanzado y ROI
- docs/GUIA_RAPIDA.md: Templates de código
- docs/README.md: Referencias técnicas

## 🔍 Debugging Común

### Problema: Silhouette Score bajo (<0.3)
**Causa**: Datos no tienen estructura clara  
**Solución**: Verifica features, reconsider si clustering es apropiado

### Problema: PCA explica <70% varianza
**Causa**: Información perdida en visualización 2D  
**Solución**: Usa 3 componentes o verifica dimensionalidad

### Problema: Clusters no tienen sentido empresarial
**Causa**: K-Means encuentra patrón matemático, no empresarial  
**Solución**: Aplica lógica de negocio, selecciona features manualmente

### Problema: K óptimo no es claro
**Causa**: Diferentes métricas sugieren diferentes K  
**Solución**: Usa conocimiento empresarial como desempate

## 📊 Comparativa: Supervisado vs No Supervisado

| Aspecto | Supervisado (Bloques 1-3) | No Supervisado (Bloque 4) |
|--------|--------------------------|--------------------------|
| **Datos** | Con etiquetas | Sin etiquetas |
| **Objetivo** | Predecir | Descubrir |
| **Evaluación** | Métrica clara (AUC, F1) | Subjeti va (validación empresarial) |
| **Complejidad** | Más predecible | Más exploratoria |
| **Casos** | Clasificación, Regresión | Segmentación, Análisis |

## 🎓 Propuesta de Estudio

**Semana 1**: K-Means + Silhouette + PCA
- Conceptos, implementación, visualización

**Semana 2**: Validación y Interpretación
- Múltiples métricas, perfilado, nomenclatura

**Semana 3**: Clustering Jerárquico
- Dendrogramas, comparación, dendrogramas

**Semana 4**: Análisis Empresarial
- ROI, estrategias, comunicación

## 📞 Contacto y Preguntas

Si tienes dudas:
1. Revisa GUIA_RAPIDA.md
2. Consulta docs/README.md
3. Experimenta con parámetros
4. Compara con notebook resuelto

## 🏅 Proyecto Final Recomendado

Usando lo aprendido:
1. Toma un dataset de clientes real
2. Selecciona features de clustering
3. Escala correctamente
4. Prueba múltiples K
5. Valida técnico y empresarialmente
6. Calcula ROI esperado
7. Propone 3 estrategias diferenciadas
8. Presenta hallazgos con visualizaciones

---

**Profesor**: Unidad de Ciencia de Datos  
**Bloques**: 4 (Introducción a No Supervisado)  
**Duración Total**: 8-10 horas  
**Nivel**: Intermediate  
**Requisitos**: Completar Bloques 1-3  

**Proximamente**: Bloque 5 (Series Temporales)
