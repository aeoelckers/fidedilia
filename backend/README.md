# Backend mínimo de Fidelia

Primer prototipo del backend basado en FastAPI. Proporciona endpoints para registrar y consultar actividades de ventas
capturadas por los vendedores.

## Requisitos

- Python 3.11+
- pip

## Instalación y ejecución local

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API quedará disponible en `http://localhost:8000` con documentación automática en `/docs`.

## Endpoints disponibles

| Método | Ruta | Descripción |
| ------ | ---- | ----------- |
| GET | `/health` | Verifica que el servicio esté activo |
| POST | `/activities` | Crea una nueva actividad | 
| GET | `/activities` | Lista todas las actividades registradas |
| GET | `/activities/{id}` | Recupera una actividad específica |

## Próximos pasos sugeridos

1. Persistencia real (Supabase/Postgres) en lugar de almacenamiento en memoria.
2. Integración con servicios de IA (Whisper/GPT) para generar resumen y etiquetas.
3. Autenticación por vendedor y multiempresa.
4. Métricas y dashboards conectados al flujo de actividades.
