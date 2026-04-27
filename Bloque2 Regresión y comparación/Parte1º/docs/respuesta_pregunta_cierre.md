# Respuesta a la pregunta de cierre

> ¿Elegirías **siempre** el modelo con menor RMSE? Justifica tu respuesta.

---

## Respuesta razonada: No, no siempre.

Elegir el modelo con menor RMSE es un buen punto de partida, pero la decisión final
debe considerar varios factores adicionales:

---

### 1. Interpretabilidad vs. rendimiento

Un modelo como **Random Forest** puede tener un RMSE un 10 % mejor que la regresión
lineal, pero si el negocio necesita **explicar** cada predicción a un cliente o ante
un regulador, la regresión lineal puede ser la opción correcta.

> **Ejemplo:** en un entorno financiero regulado (MiFID II, Basilea), la
> interpretabilidad no es opcional. Un modelo de caja negra con RMSE mínimo puede
> ser inaplicable.

---

### 2. Coste de los errores no es simétrico

El RMSE penaliza igual un error de +500 € que un error de -500 €. En muchos
problemas de negocio, los errores tienen **costes asimétricos**:

- Subestimar el importe de una venta → perdemos margen (costoso)
- Sobreestimar el importe → el cliente no compra (menos costoso)

En esos casos, puede convenir elegir un modelo con **mayor RMSE pero mejor
alineado con la dirección del error aceptable**.

---

### 3. Sobreajuste y generalización

Un RMSE muy bajo en test con una partición concreta puede ser consecuencia del
azar estadístico. Es recomendable validar con **validación cruzada** antes de
concluir que un modelo es mejor:

```python
scores = cross_val_score(
    modelo, X, y,
    cv=5,
    scoring='neg_root_mean_squared_error'
)
print(f'RMSE medio: {-scores.mean():,.1f} ± {scores.std():,.1f}')
```

Si el RMSE de Random Forest es 10 € mejor pero tiene una varianza alta entre
pliegues, Ridge puede ser más estable y preferible en producción.

---

### 4. Coste computacional y tiempo de respuesta

En sistemas que deben predecir en tiempo real (APIs, dashboards en vivo),
un modelo más simple puede ser mejor aunque su RMSE sea levemente peor.

| Criterio | Regresión Lineal | Random Forest |
|----------|-----------------|---------------|
| RMSE | Mayor | Menor |
| Velocidad de inferencia | Muy rápida | Más lenta |
| Interpretabilidad | Alta | Baja |
| Mantenimiento | Sencillo | Más complejo |

---

### 5. Conclusión práctica

La selección de modelo es una **decisión multicriterio**. El RMSE es el criterio
técnico principal, pero debe combinarse con:

- **Interpretabilidad** requerida por el negocio
- **Estabilidad** (RMSE medio ± desviación en validación cruzada)
- **Coste asimétrico** de los distintos tipos de error
- **Recursos** de cómputo disponibles en producción
- **Mantenibilidad** del modelo a largo plazo

> **Regla práctica:** si dos modelos tienen una diferencia de RMSE menor al 5 %,
> elige el más simple. Si la diferencia es mayor, analiza si el beneficio justifica
> la complejidad añadida.
