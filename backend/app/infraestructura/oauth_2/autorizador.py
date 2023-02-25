from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError  # noqa
from starlette import status

from app.dominio.entidades.usuario_entidad import UsuarioEntidad
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio
from app.infraestructura.mongo_db.repositorios.usuario_repositorio import UsuarioRepositorio
from app.infraestructura.oauth_2.modelos.usuario_registrado_modelo import UsuarioRegistradoModelo
from app.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth")


def obtener_usuario_id_desde_token(token: str) -> str:
    try:
        informacion_token: dict = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        usuario_id: str = informacion_token.get("sub")
        if not usuario_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="El identificador del usuario no es válido")
        return str(usuario_id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El token proporcionado es inválido")


async def obtener_usuario_registrado(token: str = Depends(oauth2_scheme),
                                     usuario_repositorio: IUsuarioRepositorio = Depends(
                                         UsuarioRepositorio)) -> UsuarioRegistradoModelo:
    usuario_id: str = obtener_usuario_id_desde_token(token)
    usuario: UsuarioEntidad = await usuario_repositorio.obtener_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Las credenciales del usuario son inválidas")
    if not usuario.esta_habilitado:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="El usuario se encuentra deshabilitado")
    return UsuarioRegistradoModelo(
        id=usuario.id,
        username=usuario.username,
        roles=usuario.roles,
    )
