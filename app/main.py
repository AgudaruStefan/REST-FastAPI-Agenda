from fastapi import FastAPI

import alembic.config

from app.agenda import agenda_api


def _register_api_handlers(app: FastAPI) -> FastAPI:
    app.include_router(agenda_api.router, tags=["Agenda-CRUD"])

    return app


def create_app() -> FastAPI:
    """Create and return FastAPI application."""
    app = FastAPI()
    app = _register_api_handlers(app)
    
    return app


app = create_app()

def add_migrations():
    alembicArgs = [
        "revision",
        "--autogenerate",
    ]
    alembic.config.main(argv=alembicArgs)

def apply_migrations():
    alembicArgs = [
        "--raiseerr",
        "upgrade",
        "head",
    ]
    alembic.config.main(argv=alembicArgs)


@app.on_event("startup")
async def apply_migrations_on_startup():
    add_migrations()
    apply_migrations()
