# Contributing to Docker Compose Manager

Thank you for your interest in contributing to Docker Compose Manager! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Code Style](#code-style)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project adheres to professional standards of conduct. Please be respectful and constructive in all interactions.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/docker_compose_pr.git
   cd docker_compose_pr
   ```

3. Set up the upstream remote:
   ```bash
   git remote add upstream https://github.com/nullroute-commits/docker_compose_pr.git
   ```

## Development Setup

### Prerequisites

- Python 3.9-3.13
- Poetry (for dependency management)
- Docker Engine
- Git

### Environment Setup

#### Option 1: Using Poetry (Recommended)

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

4. Set up environment:
   ```bash
   cp .env.template .env
   # Edit .env as needed
   ```

#### Option 2: Using Docker

1. Build the Docker image:
   ```bash
   docker compose build
   ```

2. Set up environment:
   ```bash
   cp .env.template .env
   # Edit .env as needed
   ```

3. Run the services:
   ```bash
   docker compose up -d
   ```

#### Option 3: Using pip (Legacy)

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install development dependencies:
   ```bash
   pip install pytest pytest-cov black flake8 mypy pylint
   ```

4. Set up environment:
   ```bash
   cp .env.template .env
   # Edit .env as needed
   ```

## Making Changes

### Branch Naming

Use descriptive branch names:

- `feature/description` - For new features
- `fix/description` - For bug fixes
- `docs/description` - For documentation updates
- `refactor/description` - For code refactoring

Example:
```bash
git checkout -b feature/add-kubernetes-support
```

### Commit Messages

Write clear, concise commit messages:

```
Add support for Kubernetes deployments

- Implement K8s deployment manager
- Add K8s configuration validators
- Update documentation
```

## Testing

### Running Tests

#### Using Poetry

```bash
# Run all tests
poetry run pytest tests/

# Run specific test file
poetry run pytest tests/unit/test_tenant.py

# Run with coverage
poetry run pytest --cov=docker_compose_manager tests/

# Run with verbose output
poetry run pytest -v tests/
```

#### Using Docker

```bash
# Run tests in container
docker compose exec web pytest tests/

# Run with coverage
docker compose exec web pytest --cov=docker_compose_manager tests/
```

#### Using pip

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/unit/test_tenant.py

# Run with coverage
pytest --cov=docker_compose_manager tests/

# Run with verbose output
pytest -v tests/
```

### Writing Tests

- Place unit tests in `tests/unit/`
- Place integration tests in `tests/integration/`
- Name test files with `test_` prefix
- Name test functions with `test_` prefix

Example:
```python
def test_tenant_creation():
    """Test creating a tenant."""
    tenant = Tenant(name="Test", slug="test")
    assert tenant.name == "Test"
```

## Code Style

### Python Style Guide

Follow PEP 8 with these specifics:

- Line length: 100 characters
- Use 4 spaces for indentation
- Use double quotes for strings
- Add docstrings to all public functions/classes

### Formatting

Format your code with Black:

#### Using Poetry
```bash
poetry run black docker_compose_manager/
```

#### Using Docker
```bash
docker compose exec web black docker_compose_manager/
```

#### Using pip
```bash
black docker_compose_manager/
```

### Linting

Check code quality:

#### Using Poetry
```bash
# Flake8
poetry run flake8 docker_compose_manager/

# Pylint
poetry run pylint docker_compose_manager/

# MyPy
poetry run mypy docker_compose_manager/
```

#### Using Docker
```bash
# Flake8
docker compose exec web flake8 docker_compose_manager/

# Pylint
docker compose exec web pylint docker_compose_manager/

# MyPy
docker compose exec web mypy docker_compose_manager/
```

#### Using pip
```bash
# Flake8
flake8 docker_compose_manager/

# Pylint
pylint docker_compose_manager/

# MyPy
mypy docker_compose_manager/
```

### Type Hints

Use type hints for all function signatures:
```python
def create_tenant(name: str, slug: str) -> Tenant:
    """Create a new tenant."""
    ...
```

## Submitting Changes

### Pre-submission Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] Code formatted with Black
- [ ] No linting errors

### Pull Request Process

1. Update your branch with latest upstream:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Push your changes:
   ```bash
   git push origin feature/your-feature
   ```

3. Create a pull request on GitHub

4. Address review comments

5. Wait for approval and merge

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Testing
Describe tests performed

## Checklist
- [ ] Tests pass
- [ ] Code formatted
- [ ] Documentation updated
```

## Development Guidelines

### Adding New Modules

1. Create module directory structure:
   ```bash
   mkdir -p docker_compose_manager/new_module
   touch docker_compose_manager/new_module/__init__.py
   ```

2. Add module exports to `__init__.py`

3. Write tests in `tests/unit/test_new_module.py`

4. Update documentation

### Updating Dependencies

#### Using Poetry (Recommended)

1. Add a new dependency:
   ```bash
   poetry add package-name
   ```

2. Add a development dependency:
   ```bash
   poetry add --group dev package-name
   ```

3. Update a dependency:
   ```bash
   poetry update package-name
   ```

4. Update all dependencies:
   ```bash
   poetry update
   ```

5. Export to requirements.txt for backwards compatibility:
   ```bash
   poetry export -f requirements.txt --output requirements.txt --without-hashes
   ```

6. Rebuild Docker image with new dependencies:
   ```bash
   docker compose build
   ```

#### Using pip (Legacy)

1. Check compatibility with Python 3.9-3.13
2. Pin exact versions in `requirements.txt`
3. Update `pyproject.toml` dependencies manually
4. Test all modules after update
5. Document any breaking changes

### Documentation

- Update README.md for user-facing changes
- Add docstrings to all public APIs
- Update relevant guides in `docs/guides/`
- Include code examples where appropriate

## Architectural Guidelines

### Module Organization

Follow the existing modular structure:

```
docker_compose_manager/
├── core/          # Core functionality
├── compose/       # Docker Compose management
├── multitenant/   # Multitenant features
├── network/       # Network automation
├── data/          # Data processing
├── async_tasks/   # Async operations
└── django_app/    # Django application
```

### Design Principles

1. **Separation of Concerns**: Keep modules focused and independent
2. **DRY**: Don't repeat yourself
3. **SOLID**: Follow SOLID principles
4. **Testability**: Write testable code
5. **Documentation**: Document public APIs

### Error Handling

Use appropriate exception types:
```python
from typing import Optional

def get_tenant(slug: str) -> Optional[Tenant]:
    """Get tenant by slug."""
    if slug not in self._tenants:
        return None
    return self._tenants[slug]
```

### Logging

Use structured logging:
```python
from docker_compose_manager.core.logging import get_logger

logger = get_logger(__name__)
logger.info(
    "Tenant created",
    extra={'context': {'tenant_id': tenant.id}}
)
```

## Release Process

### Version Numbering

Follow Semantic Versioning (SemVer):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Creating a Release

1. Update version in `__init__.py`
2. Update CHANGELOG.md
3. Create git tag:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

## Getting Help

- Check documentation in `docs/`
- Review existing code and tests
- Ask questions in pull request comments
- Open an issue for discussion

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be recognized in the project README and release notes.

Thank you for contributing! 🎉
