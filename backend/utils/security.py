# Librerias
from datetime import datetime, timedelta, timezone
from typing import Any, cast
import jwt
from dotenv import load_dotenv
import os


# Cargar variables de entorno
load_dotenv()


# Configuracion de variables de entorno para JWT
def _require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"ERROR: {name} no está configurado en .env")
    return value


def _require_int_env(name: str) -> int:
    value = _require_env(name)
    return int(value)


_SECRET_KEY = _require_env("SECRET_KEY")
_ALGORITHM: str = _require_env("ALGORITHM")
_ACCESS_TOKEN_EXPIRE_MINUTES: int = _require_int_env("ACCESS_TOKEN_EXPIRE_MINUTES")
_REFRESH_TOKEN_EXPIRE_DAYS: int = _require_int_env("REFRESH_TOKEN_EXPIRE_DAYS")

SECRET_KEY: str = _SECRET_KEY
ALGORITHM: str = _ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES: int = _ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS: int = _REFRESH_TOKEN_EXPIRE_DAYS


# FUNCIONES DE JWT
def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=_ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire, "type": "access"})

    # jwt.encode() puede retornar str o bytes según la versión — cast garantiza str
    return cast(str, jwt.encode(to_encode, SECRET_KEY, algorithm=_ALGORITHM)) # type: ignore


def create_refresh_token(data: dict[str, Any]) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=_REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode.update({"exp": expire, "type": "refresh"})

    return cast(str, jwt.encode(to_encode, SECRET_KEY, algorithm=_ALGORITHM)) # type: ignore


def decode_token(token: str) -> dict[str, Any]:
    try:
        # jwt.decode() retorna dict[str, Any] pero los stubs lo marcan como Any
        payload = cast(dict[str, Any], jwt.decode(token, SECRET_KEY, algorithms=[_ALGORITHM])) # type: ignore
        return payload
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError("Token expirado")
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError("Token inválido")