# Cultura-Digital-y-Sociedad-Aut-noma-4-Unidad-2-Tema-2
Estudiante: Lesly Keliana Carrasco Mejía 
#  Optimización de Código - Números Primos

## Actividad Autónoma 4 | Cultura Digital y Sociedad | UNACH

---

##  Descripción

Este proyecto compara un algoritmo **original** vs uno **optimizado** para encontrar números primos en un rango de **1 a 100,000**.

El objetivo es demostrar cómo **pequeñas optimizaciones** pueden mejorar drásticamente el rendimiento del código.

---

## Resultados

| Versión | Tiempo | Primos | Mejora |
|---------|--------|--------|--------|
|  Original | 26.81 segundos | 9,592 | - |
|  Optimizado | 0.11 segundos | 9,592 | **99.58%** |

![Comparación de Tiempos](comparacion_tiempos.png)



##  Optimizaciones Aplicadas

| Técnica | Original | Optimizado |
|---------|----------|------------|
| Rango de búsqueda | hasta `n-1` | hasta `√n` |
| Números pares | se verificaban | se excluyen |
| Estructura de datos | `append()` en bucle | List comprehension |
| Función de raíz | `n ** 0.5` | `math.isqrt()` (en C) |
| Complejidad | O(n²) | O(n√n) |


---

##  Cómo Ejecutar

```bash
# Código original (tarda ~27 segundos)
python codigo_original.py

# Código optimizado (tarda ~0.1 segundos)
python codigo_optimizado.py

# Generar gráfico comparativo
python grafico.py

# Ejecutar profiling
python profiling_original.py
python profiling_optimizado.py
