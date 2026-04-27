# Bloque 2 - Parte 1: Regresión y Comparación

## 📋 Descripción

Esta parte introduce los fundamentos del modelado estadístico y la inferencia. Aprendes a:

- **Regresión lineal simple**: Modelar relaciones entre variables continuas
- **Regresión lineal múltiple**: Extensión a múltiples predictores
- **Supuestos del modelo**: Normalidad, homocedasticidad, independencia, linealidad
- **Diagnóstico de residuales**: Detección de violaciones de supuestos
- **Comparación de grupos**: Test t, ANOVA, contrastes post-hoc
- **Test no paramétricos**: Mann-Whitney, Kruskal-Wallis para datos no normales
- **Contraste de hipótesis**: Significación estadística, p-valores, interpretación
- **Validación de modelos**: Validación cruzada, métricas de rendimiento (R², RMSE, MAE)
- **Selección de variables**: Stepwise, criterios AIC/BIC

## 📁 Estructura del Proyecto

```
Parte1º/
├── notebooks/          # Jupyter notebooks con los ejercicios
├── data/               # Datasets sintéticos para las prácticas
├── docs/               # Guía rápida y propuesta de uso docente
├── requirements.txt    # Librerías Python necesarias
├── environment.yml     # Entorno conda recomendado
└── README.md          # Este archivo
```

## 🚀 Cómo empezar

### Opción 1: Usando pip (recomendado para usuarios de Windows)
```bash
pip install -r requirements.txt
```

### Opción 2: Usando Conda
```bash
conda env create -f environment.yml
conda activate big_data_bloque2_parte1
```

## 📚 Contenido

- **notebooks/**: Contiene los notebooks de Jupyter con los ejercicios propuestos
- **data/**: Datasets sintéticos reproducibles para practicar
- **docs/**: Guía rápida de referencia y propuesta pedagógica

## 📖 Propuesta de Uso Docente

Consultar la carpeta `docs/` para obtener:
- Guía de uso del material
- Objetivos de aprendizaje
- Sugerencias de temporalización
- Ejercicios complementarios

## 📦 Requisitos

- Python 3.8 o superior
- Conocimientos de Bloque 1
- Ver `requirements.txt` para lista completa de librerías

## 🤝 Notas

Los datasets se regeneran de forma reproducible usando semillas fijas de aleatoriedad.
