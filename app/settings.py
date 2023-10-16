from pathlib import Path
from typing import Any, Dict, Optional

from pydantic_settings import BaseSettings
from pydantic import Field, validator

APP_ROOT = Path(__file__).parent.parent

class Settings(BaseSettings):

    APP_DIR: Path = APP_ROOT

    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: str = Field(..., env="DB_PORT")
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, val: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(val, str):
            return val
        return (
            f"postgresql://{values.get('DB_USER')}:"
            f"{values.get('DB_PASSWORD')}@"
            f"{values.get('DB_HOST')}:{values.get('DB_PORT')}"
            f"/{values.get('DB_NAME')}"
        )
    
settings = Settings(_env_file=Path(APP_ROOT, ".env"), _env_file_encoding="utf-8")