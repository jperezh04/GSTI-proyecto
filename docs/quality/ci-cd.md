# OF-04 — CI y evolución a CD

Workflow preparado para cada PR, push a main y ejecución manual: formato y lint con Ruff 0.11.13 fijado en `requirements-dev.lock`, pruebas de biblioteca estándar y ejecución del perfilador. Runtime sin dependencias de terceros. Permiso `contents: read`, sin persistir credenciales en checkout, timeout de 10 minutos y cancelación de ejecuciones obsoletas. Evidencias de tests conservadas 14 días. Los tests no consultan portales públicos; la instalación inicial de herramientas sí usa red.

Acciones fijadas a commits comprobados en sus releases oficiales:
- [checkout v4.2.2](https://github.com/actions/checkout/commit/11bd71901bbe5b1630ceea73d27597364c9af683)
- [setup-python v5.6.0](https://github.com/actions/setup-python/commit/a26af69be951a213d495a4c3e4e4022e16d87065)
- [upload-artifact v4.6.2](https://github.com/actions/upload-artifact/commit/ea165f8d65b6e75b540449e92b4886f43607fa02)

Son versiones fijadas verificadas, no una afirmación de ser las más recientes. Dependabot propone actualizaciones de acciones. Alan revisará también Ruff y fijará cualquier cambio con PR. No existe frontend aún, por lo que no corresponde un build de frontend. La comprobación estática de tipos queda pendiente de contratos tipados de ingesta; lint y pruebas no se presentan como sustituto de type checking.

## Evidencia necesaria antes de cerrar OF-04

1. Publicar workflow y observar ejecución correcta en GitHub.
2. En una rama temporal agregar un test con `self.fail("fallo intencional OF-04")`, abrir PR y conservar enlace a check fallido.
3. Retirar el fallo con un commit, comprobar verde y revisión independiente; no fusionar el fallo.
4. Activar `quality` como check requerido en main y verificar que una PR roja no se pueda fusionar bajo las reglas efectivas.

Jeremy aportó salida CLI que confirma el CI inicial exitoso en main (run 36375590336) y tres ejecuciones exitosas en PR de Dependabot. Falta prueba de fallo intencional y verificación de protecciones remotas. Los resultados locales se registran aparte.

## CD cuando exista una entrega desplegable

En M1, definir proveedor, entorno de staging, presupuesto y artefacto versionado. El mismo artefacto validado debe promoverse a producción con revisión independiente y permisos del entorno comprobados según plan. Probar salud, reversión y restauración; conservar versión anterior. No guardar secretos en repo ni ejecutar entrenamiento durante una solicitud web. Alan implementa y Mauricio revisa. No hay despliegue ni CD operativo en este arranque de datos.
