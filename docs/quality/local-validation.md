# Validación local del arranque

- Python 3.10, Windows: seis pruebas unitarias aprobadas.
- Ruff 0.11.13: lint aprobado, cuatro archivos con formato comprobado.
- Ejecución del perfilador sobre fixture sintética: correcta.
- Casos comprobados: ceros iniciales en IDs, nulos, duplicados, fechas inválidas, columnas ausentes, cabeceras duplicadas, filas mal formadas, archivo vacío, hash y rechazo de sobrescritura de manifiesto.

No son resultados de datos públicos ni evidencia de cobertura. No hay modelos entrenados. Jeremy aportó salida CLI con CI inicial exitoso (run 36375590336). Sigue pendiente demostrar el fallo intencional remoto.

Repositorio público creado: `jperezh04/GSTI-proyecto`. Jeremy confirmó Project 2 e issues #4–#9 mediante salida CLI. Las asignaciones del resto del equipo siguen pendientes. Las seis issues y sus 18 criterios están preparados en `docs/issues` y `docs/requirements/traceability.csv`. Falta confirmar cuentas GitHub del equipo, revisión independiente, reglas efectivas y configuración remota de campos/vistas.
