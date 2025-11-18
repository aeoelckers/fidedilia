# Fidelia – Resumen del producto

## 1. Concepto general

**Nombre tentativo:** "fidelia"

**Idea central:** Plataforma web + app móvil enfocada en vendedores que les permite registrar sus actividades diarias (llamadas, reuniones, cotizaciones). Un sistema de IA transcribe, clasifica y analiza las conversaciones para alimentar automáticamente un CRM inteligente, mientras actúa como coach de ventas brindando recomendaciones y métricas personalizadas.

## 2. Flujo básico del sistema

### Captura de datos
- El vendedor puede grabar audio desde su teléfono o desde la app.
- También tiene la opción de escribir notas o adjuntar correos/WhatsApp.
- Cada registro se asocia al cliente o reunión correspondiente.

### Procesamiento con IA
- Modelos tipo Whisper convierten el audio en texto.
- GPT analiza el contenido y lo clasifica (cliente nuevo, renovación, objeción, producto discutido, etc.).
- Se generan etiquetas y un resumen ejecutivo de cada interacción.

### Almacenamiento estructurado
- Toda la información se guarda en una base tipo CRM (Supabase, Airtable, Notion o SQL).
- Cada vendedor dispone de un panel con seguimiento de clientes, reuniones registradas, alertas automáticas (renovaciones/seguimiento), KPIs personales y retroalimentación.

### Retroalimentación de IA
- El sistema genera sugerencias como:
  - "Tu cliente habló 70% del tiempo, excelente equilibrio."
  - "Usaste 3 veces la palabra ‘seguro’, intenta explicar beneficios más concretos."
  - "Podrías ofrecerle el seguro de vehículos por el perfil mencionado."
- La app se convierte en un coach digital que entrena y guía al vendedor.

### Dashboard de control
- El equipo de Viento Sur (o jefes comerciales) visualiza todo en un dashboard BI: actividad diaria, progreso de cada ejecutivo, conversaciones más efectivas y oportunidades abiertas.

## 3. Primer prototipo técnico

Para comenzar el desarrollo se añadió un backend mínimo en [`backend/app/main.py`](backend/app/main.py) construido con FastAPI. Esta primera iteración expone endpoints para registrar actividades, listarlas y consultarlas individualmente usando un almacenamiento en memoria. Consulta [`backend/README.md`](backend/README.md) para instrucciones de ejecución local.

---

Este repositorio centralizará la definición técnica y el desarrollo del producto.
