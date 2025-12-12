"""Centralized configuration management using Pydantic Settings v2.

This module provides type-safe configuration with:
- Environment variable support (OFAC_ prefix)
- .env file loading
- Validation of all settings
- Sensible defaults for all values

Usage:
    from ofac.core.config import settings

    # Access configuration values
    threshold = settings.match_threshold_nok
    data_path = settings.ofac_data_path
"""

from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support.

    All settings can be overridden via environment variables
    with the OFAC_ prefix. For example:
    - OFAC_MATCH_THRESHOLD_NOK=90
    - OFAC_LOG_LEVEL=DEBUG
    - OFAC_DATA_PATH=./custom/path
    """

    # Matching thresholds
    match_threshold_nok: int = Field(
        default=95,
        ge=0,
        le=100,
        description="Score >= this value results in NOK (blocked)",
    )
    match_threshold_review: int = Field(
        default=80,
        ge=0,
        le=100,
        description="Score >= this value results in REVIEW (needs human review)",
    )

    # OFAC data settings
    ofac_data_path: Path = Field(
        default=Path("./data/ofac"),
        description="Path to OFAC data cache directory",
    )
    auto_update: bool = Field(
        default=True,
        description="Enable automatic OFAC data update checks",
    )
    update_check_hours: int = Field(
        default=24,
        ge=1,
        description="Hours between automatic update checks",
    )

    # Performance settings
    batch_size: int = Field(
        default=100,
        ge=1,
        le=10000,
        description="Maximum entities to process in a single batch",
    )
    max_file_rows: int = Field(
        default=10000,
        ge=1,
        le=100000,
        description="Maximum rows allowed in uploaded file",
    )

    # Logging settings
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO",
        description="Application log level",
    )
    log_path: Path = Field(
        default=Path("./data/logs"),
        description="Path to log directory",
    )

    # API settings
    api_host: str = Field(
        default="127.0.0.1",
        description="API server host",
    )
    api_port: int = Field(
        default=8000,
        ge=1,
        le=65535,
        description="API server port",
    )
    cors_origins: list[str] = Field(
        default_factory=lambda: ["http://localhost:8501", "http://127.0.0.1:8501"],
        description="Allowed CORS origins for API",
    )

    # Streamlit settings
    streamlit_port: int = Field(
        default=8501,
        ge=1,
        le=65535,
        description="Streamlit server port",
    )

    model_config = SettingsConfigDict(
        env_prefix="OFAC_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("ofac_data_path", "log_path", mode="before")
    @classmethod
    def convert_to_path(cls, v: str | Path) -> Path:
        """Convert string paths to Path objects."""
        if isinstance(v, str):
            return Path(v)
        return v

    @model_validator(mode="after")
    def validate_thresholds(self) -> "Settings":
        """Ensure review threshold is less than NOK threshold."""
        if self.match_threshold_review >= self.match_threshold_nok:
            msg = (
                f"match_threshold_review ({self.match_threshold_review}) must be "
                f"less than match_threshold_nok ({self.match_threshold_nok})"
            )
            raise ValueError(msg)
        return self


# Singleton instance - import this in other modules
settings = Settings()


__all__ = ["Settings", "settings"]
