# OF-06 — Perfilado reproducible

No se han inspeccionado datasets reales. Esta entrega prepara herramientas; no certifica cobertura ni cumple todavía OF-06.

1. Ower identifica recurso y diccionario en el inventario, verifica permisos y registra acceso observado.
2. Descarga el original sin transformarlo en `data/raw`. Guarda URL exacta, fecha UTC de adquisición, tamaño y SHA-256 en un manifiesto. Fecha de descarga no equivale a disponibilidad histórica.
3. Si es XLSX/PDF, conservar original y documentar conversión, hoja/páginas, herramienta y versión. El perfilador inicial acepta CSV, no convierte silenciosamente.
4. Ejecutar `python -m src.analysis.profile_sources data/raw/archivo.csv --output reports/fuente.json --encoding utf-8-sig --delimiter ";" --id CUI --date FECHA --date-format %d/%m/%Y --location PROVINCIA --text TEXTO`. Mapear columnas explícitamente a partir del diccionario; repetir opciones para múltiples columnas.
5. Revisar tipos indicativos, nulos, fechas inválidas, duplicados exactos e IDs repetidos. IDs conservan ceros iniciales; repetición no implica error sin conocer granularidad. Ubicación de obra no equivale a sede de entidad. Los conteos son del archivo, no del universo.
6. Inspeccionar manualmente texto: narración, URL o metadatos; longitudes no acreditan NLP. Registrar ejemplos permitidos sin datos personales prescindibles. No inferir `available_at` a partir de fecha del hecho.
7. Alan revisa el resultado; si fue coautor revisa Mauricio. Adjuntar evidencia delimitada y actualizar criterios.

Limitaciones iniciales: carga CSV completo en memoria, sin uniones, sin selección automática de Arequipa, sin modelos. Archivos grandes requieren partición documentada antes de usarlo. Los reportes están excluidos de Git; publicar solamente resultados agregados revisados.

## Registrar manifiesto sin sobrescribir evidencia

```sh
python -m src.ingestion.register_source data/raw/archivo.csv --url https://URL-REAL-DEL-RECURSO --acquired-at FECHA-UTC-REAL --output reports/manifiesto-fuente.json
```

Sustituir los marcadores por URL exacta y fecha real de adquisición con zona horaria (ISO 8601). El registro calcula tamaño y SHA-256; rechaza sobrescribir un manifiesto. Este comando no descarga ni confirma permisos de reutilización.
