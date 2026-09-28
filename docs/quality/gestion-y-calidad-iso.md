# Obra Futura — Gestión del proyecto y calidad

Estado: propuesta para revisión del equipo. Complementa el backlog; no reemplaza sus criterios ni declara conformidad o certificación ISO. Consulta de fuentes públicas: 28 de septiembre de 2026. La evaluación por cláusula requiere la edición completa aplicable y evidencia de ejecución; no se ha realizado.

## Referencias y alcance

| Referencia | Uso propuesto en Obra Futura |
|---|---|
| [ISO 21502:2020](https://www.iso.org/standard/74947.html) | Guía principal de gestión del proyecto: organizar alcance, responsabilidades, planificación, riesgos, cambios y seguimiento. |
| [ISO 10006:2017](https://www.iso.org/standard/70376.html) | Orientar la gestión de calidad dentro del proyecto; complementa la gestión del proyecto. |
| [ISO 9001:2026](https://www.iso.org/quality-management/iso-9001-2026) | Referencia para el sistema de gestión de calidad del equipo: procesos, responsabilidades, evaluación y mejora. No es una certificación del software ni de un workflow. |
| [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Modelo para especificar y evaluar calidad del producto software. |
| [ISO/IEC 25012:2008](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso-iec%3A25012%3Aed-1%3Av1%3Aen) | Referencia para calidad de datos; aplicar a los registros efectivamente inspeccionados. |

ISO ya presenta la edición 2026 de ISO 9001. Si el curso exige expresamente 2015, registrar esa base y la diferencia de edición. Las prácticas y umbrales siguientes son decisiones propuestas del equipo, no citas ni requisitos textuales atribuidos a ISO.

## Seis tareas, seis resultados verificables

| Issue real | Por qué importa para Obra Futura | Complemento de gestión y calidad | Responsable / revisión |
|---|---|---|---|
| [OF-01, #4](https://github.com/jperezh04/GSTI-proyecto/issues/4) | Define quién revisará las obras y qué decisión mejorará el sistema. | Acta breve: objetivo medible, interesados, alcance y exclusiones, entregables, supuestos, restricciones de tiempo/costo y aceptación del usuario. Documentar entrevista; no dar por validado un supuesto. | Jeremy / Sebastian |
| [OF-02, #5](https://github.com/jperezh04/GSTI-proyecto/issues/5) | Mantiene trazabilidad de decisiones, archivos y colaboración entre cinco personas. | Matriz de responsabilidades, reglas de revisión, registro de decisiones/cambios, dependencias y evidencia de controles reales de GitHub. | Mauricio / Alan |
| [OF-03, #6](https://github.com/jperezh04/GSTI-proyecto/issues/6) | Define qué significa una entrega aceptable y cómo comprobarlo. | Plan de calidad: objetivos, matriz RNF–riesgo–prueba, criterios de aceptación, revisión interna y tratamiento de no conformidades. | Sebastian / Jeremy |
| [OF-04, #7](https://github.com/jperezh04/GSTI-proyecto/issues/7) | Detecta regresiones del código que inspecciona los datos. | Evidencia de CI verde y rojo intencional, revisión independiente y control de cambios de herramientas. CI verde por sí solo no cierra la issue. | Alan / Mauricio |
| [OF-05, #8](https://github.com/jperezh04/GSTI-proyecto/issues/8) | Determina acceso sostenible a fuentes oficiales, sus restricciones y costos. | Riesgos por fuente, responsable, condiciones de reutilización, alternativas y estados de verificación separados. | Ower / Jeremy |
| [OF-06, #9](https://github.com/jperezh04/GSTI-proyecto/issues/9) | Comprueba datos reales y si existe texto útil; sustenta la viabilidad. | Manifiestos y perfiles reproducibles, diccionario, incidencias de calidad y límites de cobertura. Datos de prueba no sustituyen registros reales. | Ower con Alan / Mauricio si Alan fue coautor |

Conservar los 18 criterios originales OF-01-CA1 a OF-06-CA3. Estos complementos se revisan con el equipo y se vinculan a esos criterios; no crear nuevas issues fuera de OF-01 a OF-06 por este ajuste.

## Procedimiento operativo propuesto

1. Jeremy coordina una revisión semanal breve: avance por evidencia, bloqueos, capacidad y decisiones. Cada responsable actualiza su issue antes de la revisión. Registrar acuerdos, responsable y fecha; no inventar disponibilidad de compañeros.
2. Mauricio mantiene la línea base de alcance y entregables en Git. Un cambio registra motivo, impacto en alcance/tiempo/costo/calidad, decisión del equipo y enlaces a issue/PR. Las decisiones de sector y evento requieren evidencia de datos y no se toman para facilitar la implementación.
3. Sebastian revisa aceptación y calidad con alguien distinto al autor. Un incumplimiento registra descripción, evidencia, impacto, responsable, corrección, causa cuando proceda y comprobación de eficacia. No cerrar por haber realizado una corrección sin verificarla.
4. Alan mantiene CI y evidencia de versiones. No fusionar actualizaciones automáticas solo porque pasan tests; revisar compatibilidad y permisos. El CD se define cuando exista una entrega desplegable, con staging, reversión y aceptación.
5. Ower conserva originales y procedencia. Evaluar calidad por fuente, período, provincia y granularidad; no inventar disponibilidad histórica ni sumar filas como obras únicas.

## Indicadores iniciales del equipo

| Indicador | Cálculo o condición | Meta propuesta | Evidencia |
|---|---|---|---|
| Cierre trazable | Criterios cerrados con evidencia / criterios declarados cerrados | 100%; si no hay cierres, no aplica | Matriz de trazabilidad y revisión |
| Revisión independiente | PR fusionadas revisadas por otra persona / PR fusionadas | 100% después del arranque inicial | Revisiones de GitHub; registrar cualquier excepción |
| Reproducibilidad | Perfiles reales que otra persona puede repetir / perfiles entregados | 100%; si aún no hay perfiles, no aplica | Archivo/hash, configuración, versión y reporte |
| Procedencia | Archivos usados con URL, fecha de adquisición, tamaño y hash / archivos usados | 100% | Manifiestos; adquisición no equivale a publicación |
| Calidad por fuente | Nulos, duplicados, fechas inválidas y cobertura observada | Medir primero; acordar umbrales después del diagnóstico | OF-06; no imponer un porcentaje universal sin contexto |
| Bloqueos | Días abiertos, causa y siguiente acción | Revisar semanalmente | Project y registro de decisiones |

M0 completo exige posteriormente OF-07 a OF-12 y decisión de viabilidad; estas seis tareas no prueban aún que pueda construirse un predictor.

## Estado observado y pendientes

La salida de GitHub CLI compartida por Jeremy confirma seis issues (#4–#9), Project 2 y CI inicial exitoso (run 36375590336). También informa éxito en tres PR de Dependabot; eso no demuestra revisión independiente ni fusión. Project: https://github.com/users/jperezh04/projects/2

Pendientes: validación con usuario, aceptación del reparto, cuentas del equipo, vistas/iteración, dependencias nativas, protecciones, prueba intencional fallida, auditoría de datos reales y aprobación de este plan. No se afirma certificación ISO ni se han entrenado modelos.
