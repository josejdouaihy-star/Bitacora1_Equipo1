# Bitácora 1: Implementación y Pruebas
## Algoritmo: Ordenamiento por Selección (Selection Sort)
### Maestría en Tecnologías de la Información · Cohorte X (2026-III)
### Análisis y Diseño de Algoritmos · Profesora Msc. Ana Sosa
### Equipo 1 · Sección 4: Implementación y Pruebas

---

## 1. Contenido del Repositorio

* `selection_sort.py`: Implementación canónica *in-place* según Rance D. Necaise (*Data Structures and Algorithms Using Python*, John Wiley & Sons, Inc., 2011, pág. 137, Listing 5.6), siguiendo la estructura de la Sección 11 de la Guía de lectura de la Unidad I.
* `test_selection_sort.py`: Batería de pruebas automatizadas según la metodología de la Sección 9.1 de la Guía con `pytest` y `hypothesis` (7 pruebas unitarias de casos borde, prueba de propiedades de postcondición con `Counter` y orden no decreciente, y prueba diferencial contra `sorted()`).
* `README.md`: Instrucciones técnicas de reproducción.

---

## 2. Comandos de Ejecución de Pruebas

Para ejecutar la suite de pruebas completa:

```bash
uv run --with pytest --with hypothesis pytest test_selection_sort.py -v
```

*(O si tiene `pytest` e `hypothesis` instalados en su entorno: `pytest test_selection_sort.py -v`)*

Salida esperada:
```text
test_selection_sort.py::test_empty_sequence PASSED                               [ 11%]
test_selection_sort.py::test_single_element_sequence PASSED                      [ 22%]
test_selection_sort.py::test_already_sorted_sequence PASSED                      [ 33%]
test_selection_sort.py::test_reverse_sorted_sequence PASSED                      [ 44%]
test_selection_sort.py::test_sequence_with_duplicate_elements PASSED             [ 55%]
test_selection_sort.py::test_sequence_with_negative_numbers PASSED               [ 66%]
test_selection_sort.py::test_sequence_with_floating_point_numbers PASSED         [ 77%]
test_selection_sort.py::test_selection_sort_properties_postcondition PASSED      [ 88%]
test_selection_sort.py::test_selection_sort_differential_against_language_reference PASSED [100%]

============================== 9 passed in 2.07s ==============================
```
