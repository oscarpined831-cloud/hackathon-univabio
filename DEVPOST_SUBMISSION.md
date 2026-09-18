# KUKULKAN — Borrador de entrega Devpost

## Resumen

KUKULKAN es un prototipo reproducible para auditar métricas de residuos en una
interfaz proteína–ADN. En lugar de publicar activos propietarios, mostramos una
capa de validación pequeña, offline y auditable para Lys22, Asp44 y Gly46.

## Qué construimos

El repositorio incluye un esquema JSON revisado, un validador Python sin
dependencias y un comando portable. El validador comprueba tipos, rangos,
residuos requeridos y un umbral demostrativo para producir una salida
PASS/FAIL determinista.

## Seguridad y honestidad de la demo

Los números publicados son **example/audit data** transcritos de la
especificación del hackathon. No son resultados clínicos, no prueban eficacia y
no implican acceso a un modelo privado. `.gitignore` excluye pesos,
checkpoints, credenciales, archivos comprimidos, datasets privados y JSON no
revisado.

## Reproducir

```bash
python scripts/parse_kukulkan.py
python -m unittest discover -s tests -v
```

## Próximos pasos

Con autorización y datos públicos adecuados, el esquema podría conectarse a
validaciones estructurales independientes. Esa integración requeriría
documentar procedencia, controles de privacidad y evaluación científica antes
de cualquier uso fuera del hackathon.
