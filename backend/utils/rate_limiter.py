# Configuración de Rate Limiting
from slowapi import Limiter
from slowapi.util import get_remote_address
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Cargar límites desde .env
RATE_LIMIT_LOGIN = os.getenv("RATE_LIMIT_LOGIN")
RATE_LIMIT_REGISTER = os.getenv("RATE_LIMIT_REGISTER")
RATE_LIMIT_REFRESH = os.getenv("RATE_LIMIT_REFRESH")

# Instancia global de limiter para usar en routers
limiter = Limiter(key_func=get_remote_address)
