# Entrega de avance — Obra Futura / GSTI

**Corte documental:** 28 de septiembre de 2026. **Equipo:** Jeremy, Mauricio, Ower, Sebastian y Alan.

## Resultado de esta entrega

El proyecto dispone de repositorio público, seis issues de la primera iteración, un Project y una ejecución inicial de integración continua exitosa. Se prepararon herramientas reproducibles de perfilado y registro de procedencia, junto con una propuesta de gestión y calidad. La viabilidad empírica del predictor todavía no está demostrada.

La confirmación remota procede de la salida de GitHub CLI compartida por Jeremy; los documentos distinguen ese registro de las pruebas ejecutadas localmente. No se presenta un porcentaje global de avance: aún no existe una estimación acordada de todo el proyecto.

## Evidencia navegable

| Resultado | Evidencia | Límite |
|---|---|---|
| Repositorio público y primer commit | [Repositorio](https://github.com/jperezh04/GSTI-proyecto), commit inicial `0985607` | La publicación no demuestra calidad del dato. |
| Primera iteración registrada | [OF-01 #4](https://github.com/jperezh04/GSTI-proyecto/issues/4), [OF-02 #5](https://github.com/jperezh04/GSTI-proyecto/issues/5), [OF-03 #6](https://github.com/jperezh04/GSTI-proyecto/issues/6), [OF-04 #7](https://github.com/jperezh04/GSTI-proyecto/issues/7), [OF-05 #8](https://github.com/jperezh04/GSTI-proyecto/issues/8), [OF-06 #9](https://github.com/jperezh04/GSTI-proyecto/issues/9) | Abiertas; no confundir responsables propuestos con cuentas asignadas. |
| Project configurado por script | [Project 2](https://github.com/users/jperezh04/projects/2) | Acceso público al Project, vistas, fechas y reglas pendientes de verificar. |
| CI inicial correcto | [Run 36375590336](https://github.com/jperezh04/GSTI-proyecto/actions/runs/36375590336) | Pendiente prueba remota de fallo intencional y protección de main. |
| Perfilador y manifiestos | [Código](../src/analysis/profile_sources.py), [registro de fuente](../src/ingestion/register_source.py), [tests](../tests/) | CSV; prueba sintética, sin evidencia de cobertura real. |
| Gestión y calidad | [Plan ISO](quality/gestion-y-calidad-iso.md), [RNF](quality/rnf-matrix.csv), [riesgos](management/risk-register.csv) | Propuestas por aprobar; no certificación. |
| Trazabilidad | [18 criterios originales](requirements/traceability.csv) | Conserva pendientes y evidencia parcial. |

## Estado de las seis tareas

| Tarea | Entregado | Falta para aceptar |
|---|---|---|
| OF-01 | Brief, ámbito y tres tareas de usuario; acta inicial | Entrevista, frecuencia/cupo de revisión, aceptación y revisión independiente. |
| OF-02 | Repositorio, Project e issues; reglas y plantillas | Cuentas del equipo, vistas/iteración, protecciones efectivas y PR revisada. |
| OF-03 | DoD, matriz de calidad, riesgos y plan de gestión | Acordar métricas/entornos y aprobar documentos con el equipo. |
| OF-04 | Workflow, herramientas fijadas, seis tests y CI verde | Fallo intencional remoto, comprobación de bloqueo y revisión independiente. |
| OF-05 | Inventario inicial de ocho fuentes candidatas | Verificar acceso, recursos, derechos, frecuencia, costos y restricciones. |
| OF-06 | Perfilador, registro de hash/procedencia y protocolo | Descargar e inspeccionar archivos reales y diccionarios; revisar texto y cobertura. |

## Cómo presentar el avance

1. Abrir las seis issues y mostrar aceptación, responsables y dependencias.
2. Abrir el run inicial de Actions y explicar qué comprobó.
3. Ejecutar `python -m unittest discover -s tests -v` desde la raíz del repo.
4. Ejecutar el comando de perfilado del README. Aclarar que la muestra es sintética y prueba software.
5. Mostrar trazabilidad, riesgos, RNF y plan ISO. Explicar qué decisiones requieren usuario o datos reales.

## Siguiente incremento y condición de salida

Jeremy valida el problema con un posible usuario; Mauricio completa colaboración; Sebastian revisa los requisitos de calidad; Alan demuestra el check fallido; Ower verifica acceso a fuentes y luego inicia el perfilado real con Alan. Las fechas se acuerdan según disponibilidad, sin convertir puntos en días.

M0 completo dependerá de OF-07 a OF-12 en la siguiente iteración: identidad, historia, variables, evento, comparación sectorial y decisión continuar/acotar/reformular. No se entrenaron modelos ni se eligió un sector definitivo.
