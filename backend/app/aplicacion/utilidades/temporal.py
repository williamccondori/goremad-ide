import tempfile


def obtener_carpeta_temporal() -> str:
    """
    Obtiene la carpeta temporal del sistema operativo.
    Returns:
        str: Carpeta temporal del sistema operativo.
    """
    carpeta_temporal: str = tempfile.gettempdir()
    if not carpeta_temporal:
        return "/tmp"
    return carpeta_temporal
