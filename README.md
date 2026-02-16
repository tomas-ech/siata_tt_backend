# Sistema de gestión de entregas

Una API REST construida con FastAPI para la gestión integral de entregas y logística, incluyendo autenticación de usuarios, gestión de productos, planes de entrega y detalles de transporte (terrestre y marítimo).

# Características

- ✅ Autenticación y autorización con JWT
- ✅ Gestión de usuarios con validación de datos
- ✅ Catálogo de productos
- ✅ Planes de entrega con cálculo automático de descuentos
- ✅ Soporte para logística terrestre y marítima
- ✅ Generación automática de códigos de seguimiento
- ✅ CORS habilitado para múltiples orígenes
- ✅ Documentación interactiva con Swagger/OpenAPI

# Acceder a la documentación
The backend is deployed on Render. It automatically shuts down after 10–15 minutes of inactivity and may take 1–2 minutes to restart. Please be patient while it wakes up

Swagger UI: https://siata-tt-backend.onrender.com/docs
ReDoc: https://siata-tt-backend.onrender.com/redoc

# Rutas de la API
Versión: v1
Base URL: /api/v1

# Estructura del Proyecto

```
siata_tt_backend/
├── app/
│   ├── main.py                 # Entrada principal de la aplicación
│   ├── api/
│   │   ├── router.py           # Enrutador principal
│   │   └── endpoints/
│   │       ├── auth.py         # Rutas de autenticación
│   │       ├── users.py        # Rutas de usuarios
│   │       ├── products.py     # Rutas de productos
│   │       └── delivery.py     # Rutas de entregas
│   ├── models/
│   │   ├── base.py             # Modelo base SQLAlchemy
│   │   ├── user.py             # Modelo de usuario
│   │   ├── product.py          # Modelo de producto
│   │   ├── location.py         # Modelos de almacén y puerto
│   │   ├── logistic.py         # Modelos de logística
│   │   ├── delivery.py         # Modelo de entrega
│   │   └── __init__.py
│   ├── dto/
│   │   ├── user.py             # DTOs de usuario
│   │   ├── product.py          # DTOs de producto
│   │   ├── location.py         # DTOs de ubicación
│   │   ├── logistic.py         # DTOs de logística
│   │   └── delivery.py         # DTOs de entrega
│   ├── services/
│   │   └── delivery_service.py # Lógica de negocios para entregas
│   ├── utils/
│   │   └── auth/
│   │       └── get_user.py     # Utilidad para extraer usuario del token
│   ├── config/
│   │   ├── settings.py         # Configuración de la aplicación
│   │   └── security.py         # Utilidades de seguridad
│   └── db/
│       └── session.py          # Sesión de base de datos
├── tests/
│   └── reset_db.py             # Script para resetear la base de datos
├── requirements.txt            # Dependencias del proyecto
├── .env.example                # Ejemplo de variables de entorno
├── .gitignore                  # Archivos ignorados por git
└── README.md                   # Este archivo
```

# Dependencias Principales
FastAPI (0.109.0+): Framework web moderno

Uvicorn (0.27.0+): Servidor ASGI

SQLAlchemy (2.0.0+): ORM para base de datos

Pydantic (2.0.0+): Validación de datos

python-jose (3.3.0+): Manejo de JWT

passlib (1.7.4+): Hashing de contraseñas

pydantic-settings (2.1.0+): Gestión de configuración

Ver requirements.txt para la lista completa.

# Variables de Entorno
Copia .env.example a .env y configura:

Variable	Descripción	Ejemplo

* DATABASE_URL:	postgresql://user:pass@localhost/siata_db

* SECRET_KEY:	tu_clave_super_secreta_123

* ALGORITHM:	HS256

* ACCESS_TOKEN_EXPIRE_MINUTES:	30
