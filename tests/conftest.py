"""Test configuration and fixtures."""

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
