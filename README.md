# Bitácora 1: Implementación y Pruebas
## Algoritmo: Ordenamiento por Selección (Selection Sort)
### Maestría en Tecnologías de la Información · Cohorte X (2026-III)
### Análisis y Diseño de Algoritmos · Profesora Msc. Ana Sosa
### Equipo 1

---

## 1. Contenido del Repositorio

* `selection_sort.py`: Implementación canónica *in-place* según Rance D. Necaise (*Data Structures and Algorithms Using Python*, John Wiley & Sons, Inc., 2011, pág. 137, Listing 5.6), siguiendo la estructura de la Sección 11 de la Guía de lectura de la Unidad I.
* `test_selection_sort.py`: Batería de pruebas automatizadas según la metodología de la Sección 9.1 de la Guía con `pytest` y `hypothesis` (7 pruebas unitarias de casos borde, prueba de propiedades de postcondición con `Counter` y orden no decreciente, y prueba diferencial contra `sorted()`).
* `README.md`: Instrucciones técnicas de instalación y reproducción.

---

## 2. Requisitos del Sistema y del Entorno

Para ejecutar este proyecto se requiere:

* **Lenguaje:** Python 3.10 o superior (probado en Python 3.12, 3.14 y 3.15).
* **Librerías estándar utilizadas:** `collections` (`Counter`), `typing` (`List`, `Any`).
* **Librerías externas de prueba:**
  * `pytest` (>= 7.0)
  * `hypothesis` (>= 6.80)

### Instalación de dependencias (si se usa pip):
```bash
pip install pytest hypothesis
```

*(Si se utiliza el gestor `uv`, no es necesario instalar nada manualmente en el sistema; `uv` descarga y gestiona las dependencias en un entorno aislado al vuelo).*

---

## 3. Comandos de Ejecución de Pruebas

### Opción A (Recomendada, con `uv`):
```bash
uv run --with pytest --with hypothesis pytest test_selection_sort.py -v
```

### Opción B (Con Python estándar / entorno virtual activo):
```bash
pytest test_selection_sort.py -v
```

---

## 4. Salida Esperada de la Ejecución

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

---

## 5. Declaración de Uso de Herramientas de IA (Nivel Ámbar)

* **Herramienta y versión:** Asistente de IA (Gemini / Antigravity V2.29.0).
* **Nivel de uso declarado:** Ámbar (asistencia en código de pruebas y estructuración sintáctica, verificado por el equipo).

### Prompt Utilizado
> *"Hola, tengo que hacer unas pruebas automatizadas en Python para un algoritmo de ordenamiento por selección (Selection Sort). Necesito probar casos típicos como listas vacías, de un solo número, duplicados, orden inverso, etc., y también me piden hacer pruebas de propiedades con la librería Hypothesis y comparar contra sorted() de Python. ¿Me podrías dar un ejemplo básico de cómo estructurar esos tests con pytest?"*

### Salida Relevante Obtenida
La IA entregó un código genérico preliminar con las siguientes características:
* Agrupó varios casos de prueba dentro de una única función (`test_casos_comunes`).
* Empleó variables genéricas y de una sola letra (`data`, `nums`, `i`, `esperado`).
* Planteó una prueba de propiedades con `@given(st.lists(st.integers()))` que solo comprobaba que los números estuvieran ordenados (`nums[i] <= nums[i+1]`), pero sin fijar semillas deterministas y sin verificar que no se perdieran elementos de la lista original.

### Qué Verificó el Equipo y Cómo (Evidencia Independiente)
* **Cotejo bibliográfico del algoritmo:** El equipo no utilizó la implementación sugerida a ciegas. Se verificó línea por línea frente al libro de texto universitario: Rance D. Necaise (*Data Structures and Algorithms Using Python*, John Wiley & Sons, Inc., 2011, pág. 137, Listing 5.6), asegurando que la búsqueda del menor y la guarda de intercambio (`if minimum_element_index != outer_index:`) respetaran la semántica *in-place*.
* **Ejecución y medición real:** El equipo ejecutó la batería de pruebas en consola local mediante `pytest`, verificando que el 100% de las aserciones pasaran satisfactoriamente en 2.07 segundos.

### Qué Descartó y Refactorizó el Equipo (Aporte Propio)
* **Descarte de pruebas agrupadas (Mala práctica):** La IA agrupó todos los casos borde en una sola función `test_casos_comunes()`. El equipo descartó este enfoque, ya que si un caso falla, el resto de las aserciones nunca se evalúan. El equipo modularizó y separó cada escenario en funciones independientes (`test_empty_sequence`, `test_single_element_sequence`, `test_already_sorted_sequence`, `test_reverse_sorted_sequence`, `test_sequence_with_duplicate_elements`, `test_sequence_with_negative_numbers`, `test_sequence_with_floating_point_numbers`).
* **Descarte de variables de una sola letra y genéricas:** La IA utilizó nombres como `data`, `nums`, `i`. El equipo las descartó por completo y las reemplazó por variables explícitas de dominio (`the_sequence`, `working_sequence`, `generated_integers_list`, `element_index`, `minimum_element_index`) bajo principios de código limpio.
* **Descarte de la postcondición incompleta:** La IA solo verificó que los elementos resultantes estuvieran ordenados (`nums[i] <= nums[i+1]`). El equipo detectó que eso era matemáticamente insuficiente (un algoritmo que devuelva `[0, 0, 0]` pasa ese test pero destruye los datos). El equipo incorporó la propiedad de conservación del multiconjunto mediante `Counter(working_sequence) == Counter(generated_integers_list)` según la definición formal de ordenamiento de Cormen et al. (CLRS).

