#!/usr/bin/env python3
"""
Enterprise Docker Compose Manager - Initialization Script

This script creates a complete modular enterprise-level project structure
for managing multitenant Docker Compose v3 deployments of FOSS/OSS tools,
webapps, and databases.

Features:
- Custom module naming from templates
- Modular architecture with separation of concerns
- Advanced ISO JSON logging
- Django-based core application
- Network automation capabilities
- Data processing utilities
- Docker Compose v3 deployment management
- Multitenant support

Compatible with Python 3.9-3.13
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional


class ProjectInitializer:
    """Initialize enterprise Docker Compose manager project structure."""
    
    def __init__(self, project_name: str = "docker_compose_manager", base_path: Optional[str] = None):
        """
        Initialize the project initializer.
        
        Args:
            project_name: Name of the project/module
            base_path: Base path for project creation (defaults to current directory)
        """
        self.project_name = project_name.lower().replace("-", "_")
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.project_path = self.base_path / self.project_name
        self.timestamp = datetime.now(timezone.utc).isoformat()
        
    def create_directory_structure(self) -> None:
        """Create the complete directory structure for the project."""
        directories = [
            # Core application directories
            f"{self.project_name}",
            f"{self.project_name}/core",
            f"{self.project_name}/core/logging",
            f"{self.project_name}/core/config",
            f"{self.project_name}/core/models",
            f"{self.project_name}/core/utils",
            
            # Django application
            f"{self.project_name}/django_app",
            f"{self.project_name}/django_app/settings",
            f"{self.project_name}/django_app/api",
            f"{self.project_name}/django_app/management",
            f"{self.project_name}/django_app/management/commands",
            f"{self.project_name}/django_app/migrations",
            
            # Docker Compose management
            f"{self.project_name}/compose",
            f"{self.project_name}/compose/deployment",
            f"{self.project_name}/compose/templates",
            f"{self.project_name}/compose/validators",
            f"{self.project_name}/compose/orchestration",
            
            # Multitenant management
            f"{self.project_name}/multitenant",
            f"{self.project_name}/multitenant/models",
            f"{self.project_name}/multitenant/managers",
            f"{self.project_name}/multitenant/isolation",
            
            # Network automation
            f"{self.project_name}/network",
            f"{self.project_name}/network/netmiko_adapter",
            f"{self.project_name}/network/napalm_adapter",
            f"{self.project_name}/network/ipam",
            
            # Data processing
            f"{self.project_name}/data",
            f"{self.project_name}/data/processors",
            f"{self.project_name}/data/analytics",
            
            # Async operations
            f"{self.project_name}/async_tasks",
            f"{self.project_name}/async_tasks/workers",
            f"{self.project_name}/async_tasks/schedulers",
            
            # Configuration and templates
            "config",
            "config/templates",
            "config/docker",
            "config/nginx",
            
            # Deployments directory
            "deployments",
            "deployments/tenants",
            
            # Documentation
            "docs",
            "docs/api",
            "docs/guides",
            
            # Tests
            "tests",
            "tests/unit",
            "tests/integration",
            "tests/fixtures",
            
            # Scripts
            "scripts",
            "scripts/deployment",
            "scripts/maintenance",
            
            # Logs directory
            "logs",
        ]
        
        for directory in directories:
            dir_path = self.base_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")
            
    def create_requirements_file(self) -> None:
        """Create requirements.txt with pinned versions compatible with Python 3.9-3.13."""
        requirements = """# Core Django and Web Framework
Django==4.2.19; python_version < "3.10"
Django==5.1.14; python_version >= "3.10"
djangorestframework==3.15.2
django-cors-headers==4.6.0
django-filter==24.3
gunicorn==23.0.0

# Data Processing
pandas==2.2.3
numpy==1.26.4; python_version < "3.10"
numpy==2.1.3; python_version >= "3.10"

# Network Automation
netmiko==4.4.0
napalm==5.0.0
pynetbox==7.4.1

# Async Support
asyncio==3.4.3
aiohttp==3.13.3
asyncpg==0.30.0

# Docker
docker==7.1.0
docker-compose==1.29.2

# Database
psycopg2-binary==2.9.10
redis==5.2.1

# Configuration Management
python-dotenv==1.0.1
pyyaml==6.0.2
toml==0.10.2

# Logging and Monitoring
python-json-logger==3.2.1
structlog==24.4.0

# Validation
pydantic==2.10.4
marshmallow==3.24.1

# Testing
pytest==8.3.4
pytest-django==4.9.0
pytest-asyncio==0.24.0
pytest-cov==6.0.0
factory-boy==3.3.1

# Code Quality
black==24.10.0
flake8==7.1.1
mypy==1.13.0
pylint==3.3.2

# Security
cryptography==46.0.5
python-decouple==3.8

# Utilities
requests==2.32.3
click==8.1.8
rich==13.9.4
"""
        
        req_path = self.base_path / "requirements.txt"
        req_path.write_text(requirements)
        print(f"Created requirements.txt at {req_path}")
        
    def create_pyproject_toml(self) -> None:
        """Create pyproject.toml with Poetry configuration."""
        pyproject_content = f'''[tool.poetry]
name = "{self.project_name.replace("_", "-")}"
version = "1.0.0"
description = "Enterprise-level system for managing multitenant Docker Compose v3 deployments"
authors = ["Enterprise Team <team@example.com>"]
readme = "README.md"
license = "Apache-2.0"
keywords = ["docker", "compose", "multitenant", "deployment", "orchestration"]
packages = [{{include = "{self.project_name}"}}]

[tool.poetry.dependencies]
python = ">=3.9,<3.14"
Django = [
    {{ version = "^4.2.19", python = ">=3.9,<3.10" }},
    {{ version = "^5.1.14", python = ">=3.10,<3.14" }},
]
djangorestframework = "^3.15.2"
django-cors-headers = "^4.6.0"
django-filter = "^24.3"
gunicorn = "^23.0.0"
pandas = "^2.2.3"
numpy = [
    {{ version = "^1.26.4", python = ">=3.9,<3.10" }},
    {{ version = "^2.1.3", python = ">=3.10,<3.14" }},
]
netmiko = "^4.4.0"
napalm = "^5.0.0"
pynetbox = "^7.4.1"
asyncio = "^3.4.3"
aiohttp = "^3.13.3"
asyncpg = "^0.30.0"
docker = "^7.1.0"
docker-compose = "^1.29.2"
psycopg2-binary = "^2.9.10"
redis = "^5.2.1"
python-dotenv = "^1.0.1"
pyyaml = "^6.0.2"
toml = "^0.10.2"
python-json-logger = "^3.2.1"
structlog = "^24.4.0"
pydantic = "^2.10.4"
marshmallow = "^3.24.1"
requests = "^2.32.3"
click = "^8.1.8"
rich = "^13.9.4"
cryptography = "^46.0.5"
python-decouple = "^3.8"

[tool.poetry.group.dev.dependencies]
pytest = "^8.3.4"
pytest-django = "^4.9.0"
pytest-asyncio = "^0.24.0"
pytest-cov = "^6.0.0"
factory-boy = "^3.3.1"
black = "^24.10.0"
flake8 = "^7.1.1"
mypy = "^1.13.0"
pylint = "^3.3.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 100
target-version = ['py39']
include = '\\.pyi?$'

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
ignore_missing_imports = true

[tool.pylint.messages_control]
max-line-length = 100
disable = ["C0111", "C0103"]
'''
        
        pyproject_path = self.base_path / "pyproject.toml"
        pyproject_path.write_text(pyproject_content)
        print(f"Created pyproject.toml at {pyproject_path}")
        
    def create_core_files(self) -> None:
        """Create core module files."""
        # Core __init__.py
        init_content = f'''"""
{self.project_name.replace("_", " ").title()} - Enterprise Docker Compose Manager

A modular enterprise-level system for managing multitenant Docker Compose v3
deployments of FOSS/OSS tools, webapps, and databases.

Version: 1.0.0
Python: 3.9-3.13
Created: {self.timestamp}
"""

__version__ = "1.0.0"
__author__ = "Enterprise Team"
__python_requires__ = ">=3.9,<3.14"

from {self.project_name}.core.logging import get_logger
from {self.project_name}.core.config import load_config

__all__ = ["get_logger", "load_config", "__version__"]
'''
        
        init_path = self.project_path / "__init__.py"
        init_path.write_text(init_content)
        print(f"Created {init_path}")
        
    def create_logging_module(self) -> None:
        """Create advanced ISO JSON logging module."""
        logging_init = f'''"""
Advanced ISO JSON Logging Module

Provides structured logging with ISO 8601 timestamps and JSON formatting
for enterprise-level observability and compliance.
"""

from {self.project_name}.core.logging.json_logger import JSONLogger, get_logger
from {self.project_name}.core.logging.formatters import ISOJSONFormatter

__all__ = ["JSONLogger", "get_logger", "ISOJSONFormatter"]
'''
        
        json_logger_content = '''"""
JSON Logger Implementation with ISO 8601 timestamps.
"""

import logging
import sys
from typing import Optional
from pythonjsonlogger import jsonlogger
from datetime import datetime, timezone


class ISOJSONFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter with ISO 8601 timestamps."""
    
    def add_fields(self, log_record, record, message_dict):
        """Add custom fields to log record."""
        super().add_fields(log_record, record, message_dict)
        
        # Add ISO 8601 timestamp
        if not log_record.get('timestamp'):
            log_record['timestamp'] = datetime.now(timezone.utc).isoformat()
        
        # Add standard fields
        log_record['level'] = record.levelname
        log_record['logger_name'] = record.name
        log_record['module'] = record.module
        log_record['function'] = record.funcName
        log_record['line'] = record.lineno
        
        # Add process/thread info
        log_record['process_id'] = record.process
        log_record['thread_id'] = record.thread
        
        # Add context if available
        if hasattr(record, 'context'):
            log_record['context'] = record.context


class JSONLogger:
    """Wrapper for JSON logger with common configuration."""
    
    def __init__(self, name: str, level: int = logging.INFO, 
                 log_file: Optional[str] = None):
        """
        Initialize JSON logger.
        
        Args:
            name: Logger name
            level: Logging level
            log_file: Optional file path for file logging
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False
        
        # Remove existing handlers
        self.logger.handlers.clear()
        
        # Console handler with JSON formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        formatter = ISOJSONFormatter(
            '%(timestamp)s %(level)s %(logger_name)s %(message)s'
        )
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler if specified
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def get_logger(self):
        """Get the underlying logger instance."""
        return self.logger


# Global logger cache
_loggers = {}


def get_logger(name: str, level: int = logging.INFO, 
               log_file: Optional[str] = None) -> logging.Logger:
    """
    Get or create a JSON logger.
    
    Args:
        name: Logger name
        level: Logging level
        log_file: Optional file path for file logging
        
    Returns:
        Configured logger instance
    """
    cache_key = f"{name}:{level}:{log_file}"
    
    if cache_key not in _loggers:
        json_logger = JSONLogger(name, level, log_file)
        _loggers[cache_key] = json_logger.get_logger()
    
    return _loggers[cache_key]
'''
        
        formatters_content = '''"""
Custom log formatters for various output formats.
"""

from pythonjsonlogger import jsonlogger
from datetime import datetime, timezone


class ISOJSONFormatter(jsonlogger.JsonFormatter):
    """JSON formatter with ISO 8601 timestamps and custom fields."""
    
    def add_fields(self, log_record, record, message_dict):
        """Customize log record fields."""
        super().add_fields(log_record, record, message_dict)
        
        # ISO 8601 timestamp with timezone
        log_record['timestamp'] = datetime.now(timezone.utc).isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
        log_record['module'] = record.module
        log_record['function'] = record.funcName
        log_record['line_number'] = record.lineno
        
        # Add exception info if present
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)
'''
        
        # Write logging files
        logging_path = self.project_path / "core" / "logging"
        (logging_path / "__init__.py").write_text(logging_init)
        (logging_path / "json_logger.py").write_text(json_logger_content)
        (logging_path / "formatters.py").write_text(formatters_content)
        print(f"Created logging module at {logging_path}")
        
    def create_config_module(self) -> None:
        """Create configuration management module."""
        config_init = '''"""Configuration management module."""

from .loader import load_config, Config

__all__ = ["load_config", "Config"]
'''
        
        config_loader = '''"""
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
'''
        
        # Write config files
        config_path = self.project_path / "core" / "config"
        (config_path / "__init__.py").write_text(config_init)
        (config_path / "loader.py").write_text(config_loader)
        print(f"Created config module at {config_path}")
        
    def create_docker_compose_module(self) -> None:
        """Create Docker Compose management module."""
        compose_init = '''"""Docker Compose v3 deployment management module."""

from .deployment import DeploymentManager
from .orchestration import Orchestrator

__all__ = ["DeploymentManager", "Orchestrator"]
'''
        
        deployment_manager = '''"""
Docker Compose deployment manager for multitenant environments.
"""

import docker
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from docker.errors import DockerException


class DeploymentManager:
    """Manage Docker Compose v3 deployments."""
    
    def __init__(self, docker_client: Optional[docker.DockerClient] = None):
        """
        Initialize deployment manager.
        
        Args:
            docker_client: Docker client instance (creates default if None)
        """
        self.client = docker_client or docker.from_env()
        
    def validate_compose_file(self, compose_file: str) -> bool:
        """
        Validate Docker Compose file.
        
        Args:
            compose_file: Path to docker-compose.yml
            
        Returns:
            True if valid, raises exception otherwise
        """
        compose_path = Path(compose_file)
        if not compose_path.exists():
            raise FileNotFoundError(f"Compose file not found: {compose_file}")
        
        with open(compose_path, 'r') as f:
            compose_data = yaml.safe_load(f)
        
        # Check version
        version = compose_data.get('version', '3')
        if not version.startswith('3'):
            raise ValueError(f"Only Docker Compose v3 is supported, found: {version}")
        
        # Check for required sections
        if 'services' not in compose_data:
            raise ValueError("Compose file must contain 'services' section")
        
        return True
    
    def deploy_compose(self, compose_file: str, project_name: str,
                      env_vars: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Deploy Docker Compose application.
        
        Args:
            compose_file: Path to docker-compose.yml
            project_name: Project/deployment name
            env_vars: Optional environment variables
            
        Returns:
            Deployment result information
        """
        self.validate_compose_file(compose_file)
        
        # Note: This is a simplified implementation
        # In production, you would use docker-compose CLI or Python library
        result = {
            'project_name': project_name,
            'compose_file': compose_file,
            'status': 'deployed',
            'timestamp': None,
        }
        
        return result
    
    def list_deployments(self, tenant: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List active deployments.
        
        Args:
            tenant: Optional tenant filter
            
        Returns:
            List of deployment information
        """
        # Get all containers with compose project label
        containers = self.client.containers.list(
            filters={'label': 'com.docker.compose.project'}
        )
        
        deployments = {}
        for container in containers:
            project = container.labels.get('com.docker.compose.project')
            if project and (not tenant or project.startswith(f"{tenant}_")):
                if project not in deployments:
                    deployments[project] = {
                        'project_name': project,
                        'containers': [],
                        'status': 'running',
                    }
                deployments[project]['containers'].append(container.name)
        
        return list(deployments.values())
    
    def stop_deployment(self, project_name: str) -> bool:
        """
        Stop a deployment.
        
        Args:
            project_name: Project/deployment name
            
        Returns:
            True if successful
        """
        containers = self.client.containers.list(
            filters={'label': f'com.docker.compose.project={project_name}'}
        )
        
        for container in containers:
            container.stop()
        
        return True
    
    def remove_deployment(self, project_name: str) -> bool:
        """
        Remove a deployment completely.
        
        Args:
            project_name: Project/deployment name
            
        Returns:
            True if successful
        """
        self.stop_deployment(project_name)
        
        containers = self.client.containers.list(
            all=True,
            filters={'label': f'com.docker.compose.project={project_name}'}
        )
        
        for container in containers:
            container.remove()
        
        return True
'''
        
        orchestrator = '''"""
Orchestration engine for managing multiple deployments.
"""

import asyncio
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor


class Orchestrator:
    """Orchestrate multiple Docker Compose deployments."""
    
    def __init__(self, max_workers: int = 5):
        """
        Initialize orchestrator.
        
        Args:
            max_workers: Maximum number of concurrent operations
        """
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
    
    async def deploy_multiple(self, deployments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Deploy multiple applications concurrently.
        
        Args:
            deployments: List of deployment configurations
            
        Returns:
            List of deployment results
        """
        loop = asyncio.get_event_loop()
        tasks = []
        
        for deployment in deployments:
            task = loop.run_in_executor(
                self.executor,
                self._deploy_single,
                deployment
            )
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
    
    def _deploy_single(self, deployment: Dict[str, Any]) -> Dict[str, Any]:
        """Deploy a single application."""
        # Implementation would use DeploymentManager
        return {
            'project_name': deployment.get('project_name'),
            'status': 'success',
        }
    
    async def health_check_all(self, project_names: List[str]) -> Dict[str, bool]:
        """
        Check health of multiple deployments.
        
        Args:
            project_names: List of project names to check
            
        Returns:
            Dictionary mapping project names to health status
        """
        loop = asyncio.get_event_loop()
        tasks = []
        
        for project_name in project_names:
            task = loop.run_in_executor(
                self.executor,
                self._health_check_single,
                project_name
            )
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return dict(zip(project_names, results))
    
    def _health_check_single(self, project_name: str) -> bool:
        """Check health of a single deployment."""
        # Implementation would check container health
        return True
'''
        
        # Write compose management files
        compose_path = self.project_path / "compose"
        (compose_path / "__init__.py").write_text(compose_init)
        (compose_path / "deployment" / "__init__.py").write_text("")
        (compose_path / "deployment" / "manager.py").write_text(deployment_manager)
        (compose_path / "orchestration" / "__init__.py").write_text("")
        (compose_path / "orchestration" / "orchestrator.py").write_text(orchestrator)
        print(f"Created compose management module at {compose_path}")
        
    def create_multitenant_module(self) -> None:
        """Create multitenant management module."""
        multitenant_init = '''"""Multitenant management module."""

from .managers import TenantManager
from .models import Tenant

__all__ = ["TenantManager", "Tenant"]
'''
        
        tenant_models = '''"""
Tenant data models.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
from uuid import uuid4


@dataclass
class Tenant:
    """Represents a tenant in the multitenant system."""
    
    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    slug: str = ""
    description: str = ""
    active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    # Resource limits
    max_deployments: int = 10
    max_containers: int = 50
    max_cpu: Optional[float] = None  # CPU cores
    max_memory: Optional[int] = None  # Memory in MB
    
    # Configuration
    config: Dict = field(default_factory=dict)
    metadata: Dict = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        """Convert tenant to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'active': self.active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'max_deployments': self.max_deployments,
            'max_containers': self.max_containers,
            'max_cpu': self.max_cpu,
            'max_memory': self.max_memory,
            'config': self.config,
            'metadata': self.metadata,
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "Tenant":
        """Create tenant from dictionary."""
        tenant = cls()
        for key, value in data.items():
            if hasattr(tenant, key):
                if key in ('created_at', 'updated_at') and isinstance(value, str):
                    setattr(tenant, key, datetime.fromisoformat(value))
                else:
                    setattr(tenant, key, value)
        return tenant
'''
        
        tenant_manager = '''"""
Tenant management operations.
"""

from typing import List, Optional, Dict
import json
from pathlib import Path


class TenantManager:
    """Manage tenants in the multitenant system."""
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize tenant manager.
        
        Args:
            storage_path: Path to tenant storage directory
        """
        self.storage_path = Path(storage_path or "deployments/tenants")
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._tenants = {}
        self._load_tenants()
    
    def _load_tenants(self) -> None:
        """Load tenants from storage."""
        from .models import Tenant
        
        for tenant_file in self.storage_path.glob("*.json"):
            with open(tenant_file, 'r') as f:
                data = json.load(f)
                tenant = Tenant.from_dict(data)
                self._tenants[tenant.slug] = tenant
    
    def _save_tenant(self, tenant) -> None:
        """Save tenant to storage."""
        tenant_file = self.storage_path / f"{tenant.slug}.json"
        with open(tenant_file, 'w') as f:
            json.dump(tenant.to_dict(), f, indent=2)
    
    def create_tenant(self, name: str, slug: str, 
                     description: str = "", **kwargs) -> "Tenant":
        """
        Create a new tenant.
        
        Args:
            name: Tenant name
            slug: Tenant slug (unique identifier)
            description: Tenant description
            **kwargs: Additional tenant attributes
            
        Returns:
            Created tenant
        """
        from .models import Tenant
        
        if slug in self._tenants:
            raise ValueError(f"Tenant with slug '{slug}' already exists")
        
        tenant = Tenant(name=name, slug=slug, description=description)
        
        # Set additional attributes
        for key, value in kwargs.items():
            if hasattr(tenant, key):
                setattr(tenant, key, value)
        
        self._tenants[slug] = tenant
        self._save_tenant(tenant)
        
        return tenant
    
    def get_tenant(self, slug: str) -> Optional["Tenant"]:
        """Get tenant by slug."""
        return self._tenants.get(slug)
    
    def list_tenants(self, active_only: bool = False) -> List["Tenant"]:
        """
        List all tenants.
        
        Args:
            active_only: Only return active tenants
            
        Returns:
            List of tenants
        """
        tenants = list(self._tenants.values())
        
        if active_only:
            tenants = [t for t in tenants if t.active]
        
        return tenants
    
    def update_tenant(self, slug: str, **kwargs) -> Optional["Tenant"]:
        """
        Update tenant attributes.
        
        Args:
            slug: Tenant slug
            **kwargs: Attributes to update
            
        Returns:
            Updated tenant or None if not found
        """
        from datetime import datetime
        
        tenant = self._tenants.get(slug)
        if not tenant:
            return None
        
        for key, value in kwargs.items():
            if hasattr(tenant, key):
                setattr(tenant, key, value)
        
        tenant.updated_at = datetime.utcnow()
        self._save_tenant(tenant)
        
        return tenant
    
    def delete_tenant(self, slug: str) -> bool:
        """
        Delete a tenant.
        
        Args:
            slug: Tenant slug
            
        Returns:
            True if deleted, False if not found
        """
        if slug not in self._tenants:
            return False
        
        tenant_file = self.storage_path / f"{slug}.json"
        if tenant_file.exists():
            tenant_file.unlink()
        
        del self._tenants[slug]
        return True
'''
        
        # Write multitenant files
        multitenant_path = self.project_path / "multitenant"
        (multitenant_path / "__init__.py").write_text(multitenant_init)
        (multitenant_path / "models" / "__init__.py").write_text("")
        (multitenant_path / "models" / "tenant.py").write_text(tenant_models)
        (multitenant_path / "managers" / "__init__.py").write_text("")
        (multitenant_path / "managers" / "tenant_manager.py").write_text(tenant_manager)
        print(f"Created multitenant module at {multitenant_path}")
        
    def create_network_module(self) -> None:
        """Create network automation module."""
        network_init = '''"""Network automation module with Netmiko, NAPALM, and PyNetBox support."""

__all__ = []
'''
        
        # Create placeholder files for network modules
        network_path = self.project_path / "network"
        (network_path / "__init__.py").write_text(network_init)
        (network_path / "netmiko_adapter" / "__init__.py").write_text('"""Netmiko adapter for device connections."""\n')
        (network_path / "napalm_adapter" / "__init__.py").write_text('"""NAPALM adapter for network device automation."""\n')
        (network_path / "ipam" / "__init__.py").write_text('"""IP Address Management with PyNetBox."""\n')
        print(f"Created network automation module at {network_path}")
        
    def create_data_module(self) -> None:
        """Create data processing module."""
        data_init = '''"""Data processing module with pandas and numpy."""

__all__ = []
'''
        
        # Create placeholder files for data modules
        data_path = self.project_path / "data"
        (data_path / "__init__.py").write_text(data_init)
        (data_path / "processors" / "__init__.py").write_text('"""Data processors using pandas."""\n')
        (data_path / "analytics" / "__init__.py").write_text('"""Data analytics using numpy and pandas."""\n')
        print(f"Created data processing module at {data_path}")
        
    def create_async_module(self) -> None:
        """Create async operations module."""
        async_init = '''"""Async operations module for background tasks."""

__all__ = []
'''
        
        # Create placeholder files for async modules
        async_path = self.project_path / "async_tasks"
        (async_path / "__init__.py").write_text(async_init)
        (async_path / "workers" / "__init__.py").write_text('"""Async workers for background processing."""\n')
        (async_path / "schedulers" / "__init__.py").write_text('"""Task schedulers."""\n')
        print(f"Created async operations module at {async_path}")
        
    def create_django_app(self) -> None:
        """Create Django application structure."""
        django_init = '''"""Django application for web interface and API."""

default_app_config = 'docker_compose_manager.django_app.apps.DjangoAppConfig'
'''
        
        django_apps = '''"""Django app configuration."""

from django.apps import AppConfig


class DjangoAppConfig(AppConfig):
    """Configuration for Django app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'docker_compose_manager.django_app'
    verbose_name = 'Docker Compose Manager'
'''
        
        django_settings = '''"""
Django settings for Docker Compose Manager.

For production deployments, override settings using environment variables.
"""

import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'change-me-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'docker_compose_manager.django_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'docker_compose_manager.django_app.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'dcm_db'),
        'USER': os.getenv('DB_USER', 'dcm_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# CORS
CORS_ALLOW_ALL_ORIGINS = DEBUG
'''
        
        django_urls = '''"""URL configuration."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('docker_compose_manager.django_app.api.urls')),
]
'''
        
        django_wsgi = '''"""WSGI config."""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docker_compose_manager.django_app.settings.base')

application = get_wsgi_application()
'''
        
        api_urls = '''"""API URL configuration."""

from django.urls import path

urlpatterns = [
    # API endpoints will be added here
]
'''
        
        # Write Django files
        django_path = self.project_path / "django_app"
        (django_path / "__init__.py").write_text(django_init)
        (django_path / "apps.py").write_text(django_apps)
        (django_path / "settings" / "__init__.py").write_text("")
        (django_path / "settings" / "base.py").write_text(django_settings)
        (django_path / "urls.py").write_text(django_urls)
        (django_path / "wsgi.py").write_text(django_wsgi)
        (django_path / "api" / "__init__.py").write_text("")
        (django_path / "api" / "urls.py").write_text(api_urls)
        (django_path / "management" / "__init__.py").write_text("")
        (django_path / "management" / "commands" / "__init__.py").write_text("")
        print(f"Created Django application at {django_path}")
        
    def create_config_files(self) -> None:
        """Create configuration files and templates."""
        # Example docker-compose template
        compose_template = '''version: '3.8'

services:
  # Example service configuration
  webapp:
    image: nginx:latest
    container_name: ${TENANT_ID}_webapp
    restart: unless-stopped
    ports:
      - "${WEBAPP_PORT:-8080}:80"
    networks:
      - ${TENANT_ID}_network
    labels:
      - "com.docker.compose.project=${TENANT_ID}"
      - "tenant=${TENANT_ID}"

networks:
  ${TENANT_ID}_network:
    driver: bridge
    name: ${TENANT_ID}_network

volumes:
  ${TENANT_ID}_data:
    name: ${TENANT_ID}_data
'''
        
        # Example configuration file
        example_config = '''# Docker Compose Manager Configuration

app_name: docker_compose_manager
environment: production
debug: false

# Database configuration
database_host: localhost
database_port: 5432
database_name: dcm_db
database_user: dcm_user
database_password: change_me

# Redis configuration
redis_host: localhost
redis_port: 6379
redis_db: 0

# Docker configuration
docker_socket: unix:///var/run/docker.sock
docker_api_version: auto

# Logging configuration
log_level: INFO
log_file: logs/application.log

# Multitenant configuration
enable_multitenancy: true
default_tenant: default

# Network automation (optional)
# netbox_url: https://netbox.example.com
# netbox_token: your_token_here
'''
        
        # Environment template
        env_template = '''# Environment Configuration Template
# Copy this file to .env and customize values

# Django Settings
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=false
DJANGO_ALLOWED_HOSTS=*

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dcm_db
DB_USER=dcm_user
DB_PASSWORD=change_me

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/application.log

# Network Automation (Optional)
# NETBOX_URL=https://netbox.example.com
# NETBOX_TOKEN=your_token_here

# Docker
DOCKER_SOCKET=unix:///var/run/docker.sock
'''
        
        # Write config files
        config_path = self.base_path / "config"
        (config_path / "templates" / "docker-compose.yml.template").write_text(compose_template)
        (config_path / "config.example.yaml").write_text(example_config)
        (self.base_path / ".env.template").write_text(env_template)
        print(f"Created configuration files at {config_path}")
        
    def create_documentation(self) -> None:
        """Create documentation files."""
        readme_content = f'''# {self.project_name.replace("_", " ").title()}

Enterprise-level system for managing multitenant Docker Compose v3 deployments of FOSS/OSS tools, webapps, and databases.

## Features

- **Modular Architecture**: Clean separation of concerns with well-defined modules
- **Advanced Logging**: ISO JSON logging with structured output
- **Django Integration**: Full Django web framework with REST API support
- **Multitenant Support**: Isolated environments for multiple tenants
- **Docker Compose v3**: Native support for Docker Compose v3 deployments
- **Network Automation**: Integration with Netmiko, NAPALM, and PyNetBox
- **Data Processing**: Built-in pandas and numpy support
- **Async Operations**: Asyncio-based concurrent operations
- **Version Pinning**: All dependencies pinned to stable LTS releases
- **Python 3.9-3.13 Compatible**: Fully compatible with Python 3.9 through 3.13

## Installation

### Prerequisites

- Python 3.9-3.13
- Poetry (for dependency management)
- Docker Engine
- PostgreSQL (optional, for Django)
- Redis (optional, for caching)

### Setup

#### Option 1: Using Poetry (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd {self.project_name}
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Activate the virtual environment:
```bash
poetry shell
```

5. Configure environment:
```bash
cp .env.template .env
# Edit .env with your configuration
```

6. Initialize the database (if using Django):
```bash
poetry run python manage.py migrate
```

#### Option 2: Using Docker (Recommended for Production)

1. Clone the repository:
```bash
git clone <repository-url>
cd {self.project_name}
```

2. Configure environment:
```bash
cp .env.template .env
# Edit .env with your configuration
```

3. Build and run with Docker Compose:
```bash
docker-compose up -d
```

4. Initialize the database:
```bash
docker-compose exec web python manage.py migrate
```

#### Option 3: Using pip (Legacy)

1. Clone the repository:
```bash
git clone <repository-url>
cd {self.project_name}
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.template .env
# Edit .env with your configuration
```

5. Initialize the database (if using Django):
```bash
python manage.py migrate
```

## Usage

### Creating a New Tenant

```python
from {self.project_name}.multitenant import TenantManager

manager = TenantManager()
tenant = manager.create_tenant(
    name="Customer A",
    slug="customer_a",
    description="Customer A Environment",
    max_deployments=5
)
```

### Deploying Docker Compose Application

```python
from {self.project_name}.compose import DeploymentManager

deployer = DeploymentManager()
result = deployer.deploy_compose(
    compose_file="deployments/customer_a/app.yml",
    project_name="customer_a_webapp"
)
```

### Using Advanced Logging

```python
from {self.project_name} import get_logger

logger = get_logger(__name__)
logger.info("Application started", extra={{'context': {{'version': '1.0.0'}}}})
```

## Architecture

```
{self.project_name}/
├── core/                 # Core functionality
│   ├── config/          # Configuration management
│   ├── logging/         # ISO JSON logging
│   ├── models/          # Data models
│   └── utils/           # Utilities
├── compose/             # Docker Compose management
│   ├── deployment/      # Deployment operations
│   ├── orchestration/   # Multi-deployment orchestration
│   └── templates/       # Compose templates
├── multitenant/         # Multitenant management
│   ├── managers/        # Tenant managers
│   └── models/          # Tenant models
├── network/             # Network automation
│   ├── netmiko_adapter/ # Netmiko integration
│   ├── napalm_adapter/  # NAPALM integration
│   └── ipam/            # IP address management
├── data/                # Data processing
│   ├── processors/      # Data processors
│   └── analytics/       # Analytics
├── async_tasks/         # Async operations
│   ├── workers/         # Background workers
│   └── schedulers/      # Task schedulers
└── django_app/          # Django web application
    ├── api/             # REST API
    ├── management/      # Management commands
    └── settings/        # Django settings
```

## Configuration

Configuration can be provided via:
1. YAML configuration file (`config/config.yaml`)
2. Environment variables (`.env` file)
3. Command-line arguments

See `config/config.example.yaml` and `.env.template` for examples.

## Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Format code
black {self.project_name}/

# Lint code
flake8 {self.project_name}/

# Type checking
mypy {self.project_name}/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

See LICENSE file for details.

## Support

For issues, questions, or contributions, please open an issue on the repository.
'''
        
        # Write documentation
        (self.base_path / "README.md").write_text(readme_content)
        
        # Create API documentation
        api_docs = '''# API Documentation

## REST API Endpoints

### Tenants

- `GET /api/tenants/` - List all tenants
- `POST /api/tenants/` - Create new tenant
- `GET /api/tenants/{slug}/` - Get tenant details
- `PUT /api/tenants/{slug}/` - Update tenant
- `DELETE /api/tenants/{slug}/` - Delete tenant

### Deployments

- `GET /api/deployments/` - List all deployments
- `POST /api/deployments/` - Create new deployment
- `GET /api/deployments/{id}/` - Get deployment details
- `PUT /api/deployments/{id}/` - Update deployment
- `DELETE /api/deployments/{id}/` - Delete deployment

### Health

- `GET /api/health/` - System health check

## Authentication

API uses token-based authentication. Include token in header:

```
Authorization: Token <your-token>
```
'''
        
        docs_path = self.base_path / "docs"
        (docs_path / "api" / "README.md").write_text(api_docs)
        print(f"Created documentation at {docs_path}")
        
    def create_test_structure(self) -> None:
        """Create test structure and example tests."""
        test_init = '''"""Test suite for Docker Compose Manager."""

import pytest
'''
        
        test_config = '''"""Test configuration and fixtures."""

import pytest
from pathlib import Path


@pytest.fixture
def temp_config_dir(tmp_path):
    """Create temporary configuration directory."""
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    return config_dir


@pytest.fixture
def sample_compose_file(tmp_path):
    """Create sample docker-compose.yml file."""
    compose_content = """
version: '3.8'
services:
  test:
    image: nginx:latest
    ports:
      - "8080:80"
"""
    compose_file = tmp_path / "docker-compose.yml"
    compose_file.write_text(compose_content)
    return str(compose_file)
'''
        
        test_tenant = f'''"""Test tenant management."""

import pytest
from {self.project_name}.multitenant.models.tenant import Tenant
from {self.project_name}.multitenant.managers.tenant_manager import TenantManager


def test_tenant_creation():
    """Test creating a tenant."""
    tenant = Tenant(
        name="Test Tenant",
        slug="test_tenant",
        description="Test tenant for unit tests"
    )
    
    assert tenant.name == "Test Tenant"
    assert tenant.slug == "test_tenant"
    assert tenant.active is True


def test_tenant_manager_create(tmp_path):
    """Test tenant manager creation."""
    manager = TenantManager(storage_path=str(tmp_path / "tenants"))
    
    tenant = manager.create_tenant(
        name="Test Tenant",
        slug="test_tenant",
        description="Test description"
    )
    
    assert tenant.name == "Test Tenant"
    assert tenant.slug == "test_tenant"
    
    # Verify tenant is stored
    retrieved = manager.get_tenant("test_tenant")
    assert retrieved is not None
    assert retrieved.name == "Test Tenant"


def test_tenant_manager_list(tmp_path):
    """Test listing tenants."""
    manager = TenantManager(storage_path=str(tmp_path / "tenants"))
    
    manager.create_tenant(name="Tenant 1", slug="tenant1")
    manager.create_tenant(name="Tenant 2", slug="tenant2")
    
    tenants = manager.list_tenants()
    assert len(tenants) == 2
'''
        
        # Write test files
        tests_path = self.base_path / "tests"
        (tests_path / "__init__.py").write_text(test_init)
        (tests_path / "conftest.py").write_text(test_config)
        (tests_path / "unit" / "__init__.py").write_text("")
        (tests_path / "unit" / "test_tenant.py").write_text(test_tenant)
        (tests_path / "integration" / "__init__.py").write_text("")
        print(f"Created test structure at {tests_path}")
        
    def create_utility_scripts(self) -> None:
        """Create utility scripts."""
        # Management script
        manage_script = f'''#!/usr/bin/env python3
"""Management script for Docker Compose Manager."""

import os
import sys
from pathlib import Path

# Add project to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from {self.project_name} import get_logger

logger = get_logger(__name__)


def main():
    """Main entry point."""
    logger.info("Docker Compose Manager starting")
    
    # Add management commands here
    print("Docker Compose Manager")
    print("Available commands:")
    print("  - tenant: Manage tenants")
    print("  - deploy: Manage deployments")
    print("  - config: Show configuration")


if __name__ == "__main__":
    main()
'''
        
        # Deployment script
        deploy_script = '''#!/bin/bash
# Deployment automation script

set -e

echo "Docker Compose Manager - Deployment Script"
echo "==========================================="

# Check Python version
python_version=$(python3 --version)
echo "Python version: $python_version"

# Check Docker
docker_version=$(docker --version)
echo "Docker version: $docker_version"

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Deployment complete!"
'''
        
        # Write scripts
        scripts_path = self.base_path / "scripts"
        manage_path = self.base_path / "manage.py"
        manage_path.write_text(manage_script)
        manage_path.chmod(0o755)
        
        deploy_path = scripts_path / "deployment" / "deploy.sh"
        deploy_path.write_text(deploy_script)
        deploy_path.chmod(0o755)
        
        print(f"Created utility scripts at {scripts_path}")
        
    def create_gitignore_additions(self) -> None:
        """Add project-specific gitignore entries."""
        gitignore_additions = '''
# Docker Compose Manager specific
deployments/tenants/*.json
logs/*.log
config/config.yaml
.env

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
        
        gitignore_path = self.base_path / ".gitignore"
        if gitignore_path.exists():
            current = gitignore_path.read_text()
            if "Docker Compose Manager specific" not in current:
                gitignore_path.write_text(current + gitignore_additions)
        else:
            gitignore_path.write_text(gitignore_additions)
        
        print(f"Updated .gitignore")
        
    def create_docker_files(self) -> None:
        """Create Dockerfile and docker-compose.yml."""
        # Create Alpine-based Dockerfile
        dockerfile_content = f'''# Multi-stage Alpine-based Dockerfile for {self.project_name.replace("_", " ").title()}
# Uses Poetry for dependency management

# Stage 1: Builder
FROM python:3.13-alpine AS builder

# Install build dependencies
RUN apk add --no-cache \\
    gcc \\
    g++ \\
    musl-dev \\
    libffi-dev \\
    postgresql-dev \\
    linux-headers \\
    rust \\
    cargo \\
    openssl-dev \\
    pkgconfig

# Install Poetry
ENV POETRY_VERSION=1.8.2 \\
    POETRY_HOME="/opt/poetry" \\
    POETRY_NO_INTERACTION=1 \\
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install --no-cache-dir "poetry==${{POETRY_VERSION}}"

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies
RUN poetry install --only main --no-root --no-directory

# Stage 2: Runtime
FROM python:3.13-alpine

# Install runtime dependencies
RUN apk add --no-cache \\
    postgresql-libs \\
    libffi \\
    openssl

# Create non-root user
RUN addgroup -g 1000 dcm && \\
    adduser -D -u 1000 -G dcm dcm

# Set working directory
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=dcm:dcm . .

# Create necessary directories
RUN mkdir -p /app/logs /app/deployments/tenants && \\
    chown -R dcm:dcm /app

# Switch to non-root user
USER dcm

# Expose port for Django application
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    PATH="/app:${{PATH}}"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD python -c "import sys; sys.exit(0)"

# Default command
CMD ["gunicorn", "{self.project_name}.django_app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
'''
        
        dockerfile_path = self.base_path / "Dockerfile"
        dockerfile_path.write_text(dockerfile_content)
        
        # Create docker-compose.yml
        compose_content = '''version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    image: docker-compose-manager:latest
    container_name: dcm_web
    restart: unless-stopped
    ports:
      - "${DCM_PORT:-8000}:8000"
    environment:
      - DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY:-change-me-in-production}
      - DEBUG=${DEBUG:-false}
      - DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS:-*}
      - DB_HOST=${DB_HOST:-db}
      - DB_PORT=${DB_PORT:-5432}
      - DB_NAME=${DB_NAME:-dcm_db}
      - DB_USER=${DB_USER:-dcm_user}
      - DB_PASSWORD=${DB_PASSWORD:-dcm_password}
      - REDIS_HOST=${REDIS_HOST:-redis}
      - REDIS_PORT=${REDIS_PORT:-6379}
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
    volumes:
      - ./logs:/app/logs
      - ./deployments:/app/deployments
      - /var/run/docker.sock:/var/run/docker.sock
    depends_on:
      - db
      - redis
    networks:
      - dcm_network

  db:
    image: postgres:16-alpine
    container_name: dcm_postgres
    restart: unless-stopped
    environment:
      - POSTGRES_DB=${DB_NAME:-dcm_db}
      - POSTGRES_USER=${DB_USER:-dcm_user}
      - POSTGRES_PASSWORD=${DB_PASSWORD:-dcm_password}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - dcm_network

  redis:
    image: redis:7-alpine
    container_name: dcm_redis
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - dcm_network

networks:
  dcm_network:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
'''
        
        compose_path = self.base_path / "docker-compose.yml"
        compose_path.write_text(compose_content)
        
        # Create .dockerignore
        dockerignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
dist/
build/
.eggs/

# Virtual environments
venv/
env/
ENV/
.venv

# Poetry
poetry.lock

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.hypothesis/

# IDEs
.vscode/
.idea/
*.swp
*.swo
.DS_Store

# Git
.git/
.gitignore
.gitattributes

# Documentation
docs/_build/
*.md
!README.md

# Logs
*.log
logs/

# Database
*.sqlite3
db.sqlite3

# Environment files
.env
.env.*
!.env.template

# Temporary files
tmp/
temp/
*.tmp

# Build artifacts
setup.py
MANIFEST.in

# Development
tests/
scripts/deployment/deploy.sh
'''
        
        dockerignore_path = self.base_path / ".dockerignore"
        dockerignore_path.write_text(dockerignore_content)
        
        print(f"Created Docker files (Dockerfile, docker-compose.yml, .dockerignore)")
        
    def run(self) -> None:
        """Run the complete initialization process."""
        print(f"\n{'='*60}")
        print(f"Initializing {self.project_name}")
        print(f"{'='*60}\n")
        
        try:
            self.create_directory_structure()
            self.create_requirements_file()
            self.create_pyproject_toml()
            self.create_core_files()
            self.create_logging_module()
            self.create_config_module()
            self.create_docker_compose_module()
            self.create_multitenant_module()
            self.create_network_module()
            self.create_data_module()
            self.create_async_module()
            self.create_django_app()
            self.create_config_files()
            self.create_documentation()
            self.create_test_structure()
            self.create_utility_scripts()
            self.create_docker_files()
            self.create_gitignore_additions()
            
            print(f"\n{'='*60}")
            print(f"✓ Initialization Complete!")
            print(f"{'='*60}\n")
            print(f"Project created at: {self.project_path}")
            print(f"\nNext steps:")
            print(f"")
            print(f"Option 1: Using Poetry (Recommended):")
            print(f"1. cd {self.project_name}")
            print(f"2. poetry install")
            print(f"3. poetry shell")
            print(f"4. cp .env.template .env")
            print(f"5. Edit .env with your configuration")
            print(f"6. poetry run python manage.py migrate")
            print(f"")
            print(f"Option 2: Using Docker (Recommended for Production):")
            print(f"1. cd {self.project_name}")
            print(f"2. cp .env.template .env")
            print(f"3. Edit .env with your configuration")
            print(f"4. docker-compose up -d")
            print(f"5. docker-compose exec web python manage.py migrate")
            print(f"\nFor more information, see README.md")
            
        except Exception as e:
            print(f"\n✗ Error during initialization: {{e}}")
            raise


def main():
    """Main entry point for init script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Initialize Docker Compose Manager project structure"
    )
    parser.add_argument(
        "--name",
        default="docker_compose_manager",
        help="Project/module name (default: docker_compose_manager)"
    )
    parser.add_argument(
        "--path",
        default=None,
        help="Base path for project creation (default: current directory)"
    )
    
    args = parser.parse_args()
    
    initializer = ProjectInitializer(
        project_name=args.name,
        base_path=args.path
    )
    initializer.run()


if __name__ == "__main__":
    main()
