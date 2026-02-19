"""
Docker Compose Manager - Enterprise Docker Compose Manager

A modular enterprise-level system for managing multitenant Docker Compose v3
deployments of FOSS/OSS tools, webapps, and databases.

Version: 1.0.0
Python: 3.13+
Created: 2026-02-19T05:08:54.542461
"""

__version__ = "1.0.0"
__author__ = "Enterprise Team"
__python_requires__ = ">=3.13"

from docker_compose_manager.core.logging import get_logger
from docker_compose_manager.core.config import load_config

__all__ = ["get_logger", "load_config", "__version__"]
