from fastapi import Depends
from passlib.context import CryptContext
from starlette import status

from app.aplicacion.dtos.administrador.actualizar_rol_usuario_request import ActualizarRolUsuarioRequest
from app.aplicacion.dtos.administrador.actualizar_usuario_request import ActualizarUsuarioRequest
from app.aplicacion.dtos.administrador.crear_superusuario_request import CrearSuperusuarioRequest
from app.aplicacion.dtos.administrador.crear_usuario_request import CrearUsuarioRequest
from app.aplicacion.dtos.administrador.obtener_por_id_usuario_response import ObtenerPorIdUsuarioResponse
from app.aplicacion.dtos.administrador.obtener_todos_usuario_response import ObtenerTodosUsuarioResponse
from app.aplicacion.utilidades import constantes
from app.dominio.entidades.compartido import base_entidad
from app.dominio.entidades.configuracion_entidad import ConfiguracionEntidad
from app.dominio.entidades.usuario_entidad import UsuarioEntidad
from app.dominio.excepciones.aplicacion_exception import AplicacionException
from app.dominio.repositorios.configuracion_repositorio import IConfiguracionRepositorio
from app.dominio.repositorios.usuario_repositorio import IUsuarioRepositorio
from app.infraestructura.mongo_db.repositorios.configuracion_repositorio import ConfiguracionRepositorio
from app.infraestructura.mongo_db.repositorios.usuario_repositorio import UsuarioRepositorio
from app.settings import settings

encriptador = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UsuarioServicio:
    """
    Clase que contiene la logica de negocio para la administracion de usuarios.
    """

    def __init__(self,
                 usuario_repositorio: IUsuarioRepositorio = Depends(UsuarioRepositorio),
                 configuracion_repositorio: IConfiguracionRepositorio = Depends(ConfiguracionRepositorio)
                 ):
        self._usuario_repositorio = usuario_repositorio
        self._configuracion_repositorio = configuracion_repositorio

    async def obtener_todos(self) -> list[ObtenerTodosUsuarioResponse]:
        """
        Obtiene todos los usuarios activos.
        Returns:
            list[ObtenerTodosUsuarioResponse]: Lista de usuarios activos.
        """
        usuarios: list[UsuarioEntidad] = await self._usuario_repositorio.obtener_todos({
            "estado": base_entidad.ESTADO_ACTIVO
        })
        return [ObtenerTodosUsuarioResponse(**usuario.dict()) for usuario in usuarios]

    async def obtener_por_id(self, usuario_id: str) -> ObtenerPorIdUsuarioResponse:
        """
        Obtiene un usuario por su identificador.
        Args:
            usuario_id (str): Identificador del usuario.
        Returns:
            ObtenerPorIdUsuarioResponse: Usuario.
        """
        usuario: UsuarioEntidad = await self._usuario_repositorio.obtener_por_id(usuario_id)
        if not usuario.estado:
            raise AplicacionException("El usuario no existe", status.HTTP_404_NOT_FOUND)
        return ObtenerPorIdUsuarioResponse(**usuario.dict())

    async def __validar_email(self, email: str) -> None:
        """
        Valida que no exista un usuario con el correo electrónico ingresado.
        Args:
            email (str): Correo electrónico.
        Raises:
            AplicacionException: Si ya existe un usuario con el correo electrónico ingresado.
        """
        existe: bool = await self._usuario_repositorio.verificar_existencia_por_filtros({
            "estado": base_entidad.ESTADO_ACTIVO,
            "email": email
        })
        if existe:
            raise AplicacionException("Ya existe un usuario con el correo electrónico ingresado",
                                      status.HTTP_400_BAD_REQUEST)

    async def crear(self, request: CrearUsuarioRequest, usuario_auditoria_id: str,
                    es_superusuario: bool = False) -> str:
        """
        Crea un nuevo usuario.
        Args:
            request (CrearUsuarioRequest): Información del usuario a crear.
            usuario_auditoria_id (str): Identificador del usuario que crea el usuario.
            es_superusuario (bool): Indica si el usuario a crear es superusuario.
        Returns:
            str: Identificador del usuario creado.
        """
        username = request.username.strip()
        # Se valida que no se repita el nombre de usuario.
        existe = await self._usuario_repositorio.verificar_existencia_por_filtros({
            "estado": base_entidad.ESTADO_ACTIVO,
            "username": username
        })
        if existe:
            raise AplicacionException(
                "Ya existe un usuario con el nombre de usuario ingresado",
                status.HTTP_400_BAD_REQUEST
            )

        await self.__validar_email(request.email)
        password_encriptado: str = encriptador.hash(str(request.password))
        # Se establecen los reles predeterminados.
        roles: list[str] = [constantes.ROL_USUARIO] if not es_superusuario else [
            constantes.ROL_USUARIO,
            constantes.ROL_ADMINISTRADOR, constantes.ROL_SUPER_USUARIO
        ]
        usuario: UsuarioEntidad = UsuarioEntidad(
            email=request.email,
            username=username,
            password=password_encriptado,
            nombres=request.nombres,
            apellidos=request.apellidos,
            roles=roles,
            esta_habilitado=request.esta_habilitado
        )
        usuario.registrar_creacion(usuario_auditoria_id)
        return await self._usuario_repositorio.crear(usuario)

    async def crear_superusuario(self, request: CrearSuperusuarioRequest) -> str:
        """
        Crea un nuevo superusuario.
        Args:
            request (CrearSuperusuarioRequest): Información del superusuario a crear.
        Returns:
            str: Identificador del superusuario creado.
        """
        # Validacion de la llave secreta, solo se puede crear un superusuario si se envia la llave.
        if not request.llave_secreta == settings.SECRET_KEY:
            raise AplicacionException("La llave secreta no es valida", status.HTTP_403_FORBIDDEN)
        # Se valida que no haya más de un superusuario registrado.
        existe = await self._usuario_repositorio.verificar_existencia_por_filtros({
            "roles": {
                "$in": [constantes.ROL_SUPER_USUARIO]
            }
        })
        if existe:
            raise AplicacionException("Ya existe un superusuario", status.HTTP_400_BAD_REQUEST)
        superusuario_id = await self.crear(request, request.username, es_superusuario=True)
        # Se registran las configuraciones iniciales.
        configuraciones: list[ConfiguracionEntidad] = [
            ConfiguracionEntidad(nombre="nombre_empresa", valor=None),
            ConfiguracionEntidad(nombre="latitud_inicial", valor="0"),
            ConfiguracionEntidad(nombre="longitud_inicial", valor="0"),
            ConfiguracionEntidad(nombre="zoom_inicial", valor="0"),
            ConfiguracionEntidad(nombre="capa_base_incial_id", valor=None),
            ConfiguracionEntidad(nombre="servicios_externos_activos", valor=None),
        ]
        for configuracion in configuraciones:
            configuracion.registrar_creacion(request.username)
        configuraciones_id: list[str] = await self._configuracion_repositorio.crear_multiple(configuraciones)
        # Se valida que se hayan creado todas las configuraciones.
        if len(configuraciones_id) != len(configuraciones):
            raise AplicacionException(
                "No se pudieron crear las configuraciones iniciales",
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return superusuario_id

    async def actualizar(self, usuario_id: str, request: ActualizarUsuarioRequest, usuario_auditoria_id: str) -> str:
        """
        Actualiza un usuario existente.
        Args:
            usuario_id (str): Identificador del usuario.
            request (ActualizarUsuarioRequest): Información del usuario a actualizar.
            usuario_auditoria_id (str): Identificador del usuario que actualiza el usuario.
        Returns:
            str: Identificador del usuario actualizado.
        """
        usuario = await self._usuario_repositorio.obtener_por_id(usuario_id)
        usuario.nombres = request.nombres
        usuario.apellidos = request.apellidos
        usuario.esta_habilitado = request.esta_habilitado
        usuario.registrar_actualizacion(usuario_auditoria_id)
        return await self._usuario_repositorio.actualizar(usuario_id, usuario)

    async def eliminar(self, usuario_id: str, usuario_auditoria_id: str) -> str:
        """
        Elimina un usuario existente.
        Args:
            usuario_id (str): Identificador del usuario.
            usuario_auditoria_id (str): Identificador del usuario que elimina el usuario.
        Returns:
            str: Identificador del usuario eliminado.
        """
        existe_usuario: bool = await self._usuario_repositorio.verificar_existencia(usuario_id)
        if not existe_usuario:
            raise AplicacionException("El usuario no existe", status.HTTP_404_NOT_FOUND)
        return await self._usuario_repositorio.eliminar(usuario_id, usuario_auditoria_id)

    async def actualizar_rol(self, usuario_id: str, request: ActualizarRolUsuarioRequest,
                             usuario_auditoria_id: str) -> str:
        """
        Actualiza los roles de un usuario existente.
        Args:
            usuario_id (str): Identificador del usuario.
            request (ActualizarRolUsuarioRequest): Información de los roles del usuario a actualizar.
            usuario_auditoria_id (str): Identificador del usuario que actualiza los roles del usuario.
        Returns:
            str: Identificador del usuario actualizado.
        """
        # Se valida que el usuario no intente dejar de tener el rol de usuario.
        if not request.esUsuario:
            raise AplicacionException(
                "El usuario no puede dejar de tener el rol de usuario", status.HTTP_400_BAD_REQUEST
            )
        # Se valida que el usuario tenga al menos un rol.
        if not request.esUsuario and not request.esAdministrador:
            raise AplicacionException("Debe seleccionar al menos un rol", status.HTTP_400_BAD_REQUEST)
        # Se establecen los roles.
        roles: list[str] = []
        if request.esUsuario:
            roles.append(constantes.ROL_USUARIO)
        if request.esAdministrador:
            roles.append(constantes.ROL_ADMINISTRADOR)
        usuario = await self._usuario_repositorio.obtener_por_id(usuario_id)
        usuario.roles = roles
        usuario.registrar_actualizacion(usuario_auditoria_id)
        return await self._usuario_repositorio.actualizar(usuario_id, usuario)
