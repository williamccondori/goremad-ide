from fastapi import Depends
from pymongo import MongoClient
from typing import Type
from app.dominio.entidades.capa_base_entidad import CapaBaseEntidad
from app.dominio.entidades.catalogo_entidad import CatalogoEntidad
from app.dominio.entidades.grupo_entidad import GrupoEntidad
from app.dominio.entidades.tema_entidad import TemaEntidad
from app.settings import settings
from app.dominio.repositorios.base_repositorio import IBaseRepositorio
from app.infraestructura.mongo_db.repositorios.base_repositorio import BaseRepositorio


def get_mongo_client() -> MongoClient:
    return MongoClient(settings.MONGODB_URL_BASE_DATOS)


def registrar_repo_capa_base(
    client: MongoClient = Depends(get_mongo_client),
) -> IBaseRepositorio:
    return BaseRepositorio(
        client[settings.MONGODB_NOMBRE_BASE_DATOS]["capas_base"], CapaBaseEntidad
    )


def registrar_repo_catalogo(
    client: MongoClient = Depends(get_mongo_client),
) -> IBaseRepositorio:
    return BaseRepositorio(
        client[settings.MONGODB_NOMBRE_BASE_DATOS]["catalogos"], CatalogoEntidad
    )


def registrar_repo_tema(
    client: MongoClient = Depends(get_mongo_client),
) -> IBaseRepositorio:
    return BaseRepositorio(
        client[settings.MONGODB_NOMBRE_BASE_DATOS]["temas"], TemaEntidad
    )


def registrar_repo_grupo(
    client: MongoClient = Depends(get_mongo_client),
) -> IBaseRepositorio:
    return BaseRepositorio(
        client[settings.MONGODB_NOMBRE_BASE_DATOS]["grupos"], GrupoEntidad
    )
