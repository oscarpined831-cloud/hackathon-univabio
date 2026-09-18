# KUKULKAN — Hackathon UnivaBio

KUKULKAN es un prototipo de auditoría reproducible para explorar cómo presentar
métricas de residuos en una interfaz proteína–ADN. Este repositorio público
contiene la capa de validación y un conjunto mínimo de datos de ejemplo para
la entrega de **Hackathon UnivaBio / Devpost**; no contiene el modelo privado ni
datos sensibles.

## Qué demuestra

- Validación determinista y sin dependencias externas de registros para **Lys22,
  Asp44 y Gly46**.
- Datos estructurados que distinguen explícitamente `example_audit_data` de
  resultados clínicos o experimentales.
- Un límite de seguridad claro: pesos (`.pth`, `.pt`, `.onnx`, etc.),
  credenciales, datasets privados, archivos comprimidos y JSON fuera de
  `data/sample/` no se publican.

Los valores pLDDT de la muestra (89.2, 88.4 y 87.9) provienen de la
especificación del hackathon y se incluyen solo como **datos ilustrativos de
auditoría**. No afirmamos eficacia clínica, aprobación regulatoria, precisión
predictiva ni acceso a modelos privados.

## Arquitectura

```text
JSON de muestra -> core/validator.py -> salida PASS/FAIL
                         ^
              scripts/parse_kukulkan.py
```

Consulta [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) para el flujo, los límites
y las decisiones de reproducibilidad.

## Ejecutar

Requiere Python 3.9+:

```bash
python scripts/parse_kukulkan.py
python -m unittest discover -s tests -v
```

La validación usa un umbral demostrativo configurable (`--threshold 85.0`); no
es un criterio científico ni clínico.

## Reproducibilidad y seguridad

El proyecto funciona offline y no descarga modelos. Antes de publicar cambios:

```bash
git status --short
git check-ignore -v G5618_WONKA_DNA.pth .env private.json data/sample/validation_metrics.json
```

La licencia es **KUKULKAN Source-Available Evaluation License**: permite
evaluación académica, revisión por pares y juzgamiento del hackathon, pero no
concede derechos comerciales ni acceso a activos propietarios. Lee
[LICENSE](LICENSE) antes de reutilizarlo.

## Descripción para Devpost

KUKULKAN convierte una especificación molecular en una demostración pública,
pequeña y auditable: un validador sin dependencias revisa registros de tres
residuos críticos y reporta resultados reproducibles. La entrega prioriza la
trazabilidad y la seguridad: los datos publicados están etiquetados como
ilustrativos, mientras que pesos, credenciales y datasets privados permanecen
fuera del repositorio. El prototipo no pretende sustituir validación
experimental ni hacer afirmaciones clínicas.
