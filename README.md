# GSTI-proyecto — Obra Futura

Repositorio público: https://github.com/jperezh04/GSTI-proyecto

Investigación aplicada sobre detección temprana del riesgo de retraso en obras públicas del departamento de Arequipa. Arranque M0: acceso real a datos, colaboración y calidad reproducible. No hay predictor entrenado ni cobertura demostrada.

## Equipo y primera iteración

| Issue | Responsable propuesto | Revisión independiente |
|---|---|---|
| OF-01 Producto | Jeremy | Sebastian |
| OF-02 Repositorio y Project | Mauricio | Alan |
| OF-03 Calidad | Sebastian | Jeremy |
| OF-04 CI | Alan | Mauricio |
| OF-05 Fuentes | Ower | Jeremy |
| OF-06 Perfilado | Ower, con apoyo de Alan | Alan, para cambios no escritos por él |

Una tarea principal activa por persona: Ower empieza OF-06 después de OF-05. Si Alan es coautor, Mauricio revisa ese cambio. Roles pendientes de aceptación del equipo y cuentas GitHub pendientes salvo Jeremy (`jperezh04`).

## Alcance

Las ocho provincias: Arequipa, Camaná, Caravelí, Castilla, Caylloma, Condesuyos, Islay y La Unión; ubicación de la obra y distintos niveles de gobierno. Saneamiento, transporte, educación y salud siguen como candidatos. Evento, horizonte, sector y viabilidad se deciden después de la auditoría. Un CUI no equivale a un contrato ni una obra.

## Ejecutar localmente

Python 3.10 o superior. El perfilador usa únicamente la biblioteca estándar.

```sh
python -m unittest discover -s tests -v
python -m src.analysis.profile_sources data/samples/test_fixture.csv --output reports/test-profile.json --date FECHA --date-format %d/%m/%Y --id CUI --location PROVINCIA --text TEXTO
```

La muestra de tests es sintética, exclusivamente para verificar software. No es evidencia empírica ni acredita OF-06. Para datos reales, revisar `docs/data/profiling.md`.

## Organización

`docs/issues`: únicamente OF-01 a OF-06, criterios literales del backlog. `docs/requirements/traceability.csv`: matriz criterio–responsable–evidencia. `docs/data`: inventario y protocolo. `data/raw`: originales locales excluidos de Git. `src`: ingesta, validación, procesamiento y análisis. No publicar originales grandes, secretos o datos personales innecesarios.

Ver `docs/quality/project.md`, `docs/quality/collaboration.md` y `docs/quality/ci-cd.md`. M0 no termina con estas seis tareas: OF-12 decidirá continuar, acotar o reformular en una iteración posterior.

## Entrega de avance

[Informe M0 y recorrido de demostración](docs/AVANCE-M0.md) · [Gestión y calidad ISO](docs/quality/gestion-y-calidad-iso.md) · [Acta inicial](docs/management/project-charter.md) · [Riesgos](docs/management/risk-register.csv) · [Matriz RNF](docs/quality/rnf-matrix.csv). Documentos propuestos; pendientes y limitaciones explícitos.
