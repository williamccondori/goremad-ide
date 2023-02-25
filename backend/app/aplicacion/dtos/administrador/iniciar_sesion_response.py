from pydantic import BaseModel


class IniciarSesionResponse(BaseModel):
    access_token: str
