# Arquitectura y límites de KUKULKAN

KUKULKAN es una demostración auditable para el Hackathon UnivaBio. El flujo
público valida la forma y las métricas de un pequeño documento JSON revisado:

1. `data/sample/validation_metrics.json` contiene únicamente datos ilustrativos
   sobre Lys22, Asp44 y Gly46.
2. `core/validator.py` comprueba el esquema, tipos, rango de pLDDT y un umbral
   demostrativo configurable.
3. `scripts/parse_kukulkan.py` ofrece un punto de entrada portable sin
   dependencias externas.

El repositorio no contiene pesos, checkpoints, secuencias privadas, datasets
crudos, credenciales ni un modelo predictivo. Los valores son **example/audit
data** transcritos de la especificación del proyecto y no son evidencia clínica,
experimental ni una garantía de estabilidad estructural. `verified` significa
únicamente que el registro pasó la revisión de muestra; no significa validación
biológica independiente.

## Reproducibilidad

Con Python 3.9 o posterior:

```bash
python scripts/parse_kukulkan.py
python -m unittest discover -s tests -v
```

Para probar otro archivo seguro, pásalo como primer argumento. Los JSON fuera de
`data/sample/` se ignoran por defecto mediante `.gitignore`.
