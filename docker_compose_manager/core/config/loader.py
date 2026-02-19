"""
Configuration loader with support for multiple formats and environments.
"""

import os
import yaml
import json
from pathlib import Path
from typing import Any, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class Config:
    """Application configuration."""
    
    # Application settings
    app_name: str = "docker_compose_manager"
    debug: bool = False
    environment: str = "production"
    
    # Django settings
    django_secret_key: str = ""
    django_allowed_hosts: list = field(default_factory=lambda: ["*"])
    
    # Database settings
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "dcm_db"
    database_user: str = "dcm_user"
    database_password: str = ""
    
    # Redis settings
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    
    # Docker settings
    docker_socket: str = "unix:///var/run/docker.sock"
    docker_api_version: str = "auto"
    
    # Logging settings
    log_level: str = "INFO"
    log_file: Optional[str] = None
    
    # Multitenant settings
    enable_multitenancy: bool = True
    default_tenant: str = "default"
    
    # Network automation settings
    netbox_url: Optional[str] = None
    netbox_token: Optional[str] = None
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> "Config":
        """Create Config from dictionary."""
        return cls(**{k: v for k, v in config_dict.items() if k in cls.__annotations__})
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        config_dict = {
            "app_name": os.getenv("APP_NAME", "docker_compose_manager"),
            "debug": os.getenv("DEBUG", "false").lower() == "true",
            "environment": os.getenv("ENVIRONMENT", "production"),
            "django_secret_key": os.getenv("DJANGO_SECRET_KEY", ""),
            "database_host": os.getenv("DB_HOST", "localhost"),
            "database_port": int(os.getenv("DB_PORT", "5432")),
            "database_name": os.getenv("DB_NAME", "dcm_db"),
            "database_user": os.getenv("DB_USER", "dcm_user"),
            "database_password": os.getenv("DB_PASSWORD", ""),
            "redis_host": os.getenv("REDIS_HOST", "localhost"),
            "redis_port": int(os.getenv("REDIS_PORT", "6379")),
            "redis_db": int(os.getenv("REDIS_DB", "0")),
            "log_level": os.getenv("LOG_LEVEL", "INFO"),
            "log_file": os.getenv("LOG_FILE"),
            "netbox_url": os.getenv("NETBOX_URL"),
            "netbox_token": os.getenv("NETBOX_TOKEN"),
        }
        return cls.from_dict(config_dict)


def load_config(config_file: Optional[str] = None) -> Config:
    """
    Load configuration from file or environment.
    
    Args:
        config_file: Path to configuration file (YAML or JSON)
        
    Returns:
        Config object
    """
    if config_file and Path(config_file).exists():
        with open(config_file, 'r') as f:
            if config_file.endswith('.yaml') or config_file.endswith('.yml'):
                config_dict = yaml.safe_load(f)
            elif config_file.endswith('.json'):
                config_dict = json.load(f)
            else:
                raise ValueError(f"Unsupported config format: {config_file}")
        
        return Config.from_dict(config_dict)
    
    # Load from environment variables
    return Config.from_env()
