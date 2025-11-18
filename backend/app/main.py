from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator


class ActivityBase(BaseModel):
    seller_id: str = Field(..., description="Identificador del vendedor")
    client_name: str = Field(..., description="Nombre del cliente o prospecto")
    channel: str = Field(..., description="Origen del contacto: llamada, whatsapp, reunión, etc.")
    summary: Optional[str] = Field(None, description="Resumen breve redactado por el vendedor")
    transcription: Optional[str] = Field(None, description="Texto transcrito de la conversación")
    tags: List[str] = Field(default_factory=list, description="Etiquetas clasificadas por IA")
    sentiment_score: Optional[float] = Field(
        None,
        ge=-1.0,
        le=1.0,
        description="Puntaje de sentimiento entre -1 y 1",
    )

    @validator("channel")
    def normalize_channel(cls, value: str) -> str:
        normalized = value.strip().lower()
        if not normalized:
            raise ValueError("El canal no puede estar vacío")
        return normalized


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: UUID
    created_at: datetime


class ActivityStore:
    """Almacenamiento en memoria para prototipado temprano."""

    def __init__(self) -> None:
        self._activities: List[Activity] = []

    def add(self, activity_data: ActivityCreate) -> Activity:
        activity = Activity(
            id=uuid4(),
            created_at=datetime.utcnow(),
            **activity_data.dict(),
        )
        self._activities.append(activity)
        return activity

    def list(self) -> List[Activity]:
        return list(self._activities)

    def get(self, activity_id: UUID) -> Activity:
        for activity in self._activities:
            if activity.id == activity_id:
                return activity
        raise KeyError("Activity not found")


store = ActivityStore()
app = FastAPI(title="Fidelia API", description="Backend mínimo para registrar actividades de ventas")


@app.get("/health")
def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/activities", response_model=Activity, status_code=201)
def create_activity(activity_input: ActivityCreate) -> Activity:
    """Registra una nueva actividad de ventas."""

    if not activity_input.summary and not activity_input.transcription:
        raise HTTPException(
            status_code=400,
            detail="Debes proveer al menos un resumen o una transcripción",
        )
    return store.add(activity_input)


@app.get("/activities", response_model=List[Activity])
def list_activities() -> List[Activity]:
    return store.list()


@app.get("/activities/{activity_id}", response_model=Activity)
def retrieve_activity(activity_id: UUID) -> Activity:
    try:
        return store.get(activity_id)
    except KeyError as exc:  # pragma: no cover - FastAPI maneja la excepción
        raise HTTPException(status_code=404, detail=str(exc)) from exc
