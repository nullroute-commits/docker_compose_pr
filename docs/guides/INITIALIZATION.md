# Initialization Guide

This guide explains how to use the `init.py` script to create a custom Docker Compose Manager project.

## Overview

The `init.py` script is a powerful initialization tool that creates a complete enterprise-level project structure for managing multitenant Docker Compose v3 deployments. It supports custom module naming and generates all necessary files and directories.

## Usage

### Basic Usage (Default Name)

```bash
python3 init.py
```

This creates a project named `docker_compose_manager` in the current directory.

### Custom Module Name

```bash
python3 init.py --name my_company_orchestrator
```

This creates a project with a custom name `my_company_orchestrator`.

### Custom Base Path

```bash
python3 init.py --name my_project --path /path/to/projects
```

This creates the project in a specified directory.

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--name` | Project/module name | `docker_compose_manager` |
| `--path` | Base path for project creation | Current directory |

## Generated Structure

The init script creates the following structure:

```
<project_name>/
├── <module_name>/           # Main Python package
│   ├── core/                # Core functionality
│   │   ├── config/          # Configuration management
│   │   ├── logging/         # ISO JSON logging
│   │   ├── models/          # Data models
│   │   └── utils/           # Utilities
│   ├── compose/             # Docker Compose management
│   │   ├── deployment/      # Deployment operations
│   │   ├── orchestration/   # Multi-deployment orchestration
│   │   ├── templates/       # Compose templates
│   │   └── validators/      # Validation logic
│   ├── multitenant/         # Multitenant management
│   │   ├── managers/        # Tenant managers
│   │   ├── models/          # Tenant models
│   │   └── isolation/       # Isolation logic
│   ├── network/             # Network automation
│   │   ├── netmiko_adapter/ # Netmiko integration
│   │   ├── napalm_adapter/  # NAPALM integration
│   │   └── ipam/            # IP address management
│   ├── data/                # Data processing
│   │   ├── processors/      # Data processors
│   │   └── analytics/       # Analytics
│   ├── async_tasks/         # Async operations
│   │   ├── workers/         # Background workers
│   │   └── schedulers/      # Task schedulers
│   └── django_app/          # Django web application
│       ├── api/             # REST API
│       ├── management/      # Management commands
│       └── settings/        # Django settings
├── config/                  # Configuration files
│   ├── templates/           # Docker Compose templates
│   ├── docker/              # Docker configs
│   └── nginx/               # Nginx configs
├── deployments/             # Deployment storage
│   └── tenants/             # Tenant-specific deployments
├── docs/                    # Documentation
│   ├── api/                 # API documentation
│   └── guides/              # User guides
├── tests/                   # Test suite
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── fixtures/            # Test fixtures
├── scripts/                 # Utility scripts
│   ├── deployment/          # Deployment scripts
│   └── maintenance/         # Maintenance scripts
├── logs/                    # Log directory
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup
├── pyproject.toml          # Modern Python packaging
├── manage.py               # Management script
├── .env.template           # Environment template
└── README.md               # Project documentation
```

## Key Features

### 1. Modular Architecture

The generated project follows a modular architecture with clear separation of concerns:

- **Core**: Fundamental functionality (config, logging, models)
- **Compose**: Docker Compose management and orchestration
- **Multitenant**: Tenant isolation and management
- **Network**: Network automation capabilities
- **Data**: Data processing and analytics
- **Async**: Background task processing
- **Django**: Web interface and REST API

### 2. Advanced Logging

All modules include ISO 8601 compliant JSON logging:

```python
from <module_name> import get_logger

logger = get_logger(__name__)
logger.info("Operation completed", extra={'context': {'tenant': 'customer1'}})
```

Output:
```json
{
  "timestamp": "2026-02-19T05:10:30.123456+00:00",
  "level": "INFO",
  "logger_name": "my_module",
  "message": "Operation completed",
  "context": {"tenant": "customer1"}
}
```

### 3. Configuration Management

Supports multiple configuration sources:

- YAML configuration files
- Environment variables (.env file)
- Command-line arguments

### 4. Multitenant Support

Built-in multitenant management:

```python
from <module_name>.multitenant import TenantManager

manager = TenantManager()
tenant = manager.create_tenant(
    name="Customer A",
    slug="customer_a",
    max_deployments=10
)
```

### 5. Docker Compose v3 Management

Native Docker Compose v3 support:

```python
from <module_name>.compose import DeploymentManager

deployer = DeploymentManager()
result = deployer.deploy_compose(
    compose_file="deployments/customer_a/app.yml",
    project_name="customer_a_webapp"
)
```

### 6. Async Operations

Asyncio-based concurrent operations:

```python
from <module_name>.compose import Orchestrator

orchestrator = Orchestrator()
results = await orchestrator.deploy_multiple([
    {'project_name': 'app1', 'compose_file': 'app1.yml'},
    {'project_name': 'app2', 'compose_file': 'app2.yml'},
])
```

## Post-Initialization Steps

After running `init.py`, follow these steps:

### 1. Navigate to Project Directory

```bash
cd <project_name>
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.template .env
# Edit .env with your configuration
nano .env
```

### 5. Initialize Database (if using Django)

```bash
python manage.py migrate
```

### 6. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

## Examples

### Example 1: Cloud Provider Orchestrator

```bash
python3 init.py --name cloud_orchestrator
cd cloud_orchestrator
# Configure for cloud provider integration
```

### Example 2: Development Environment Manager

```bash
python3 init.py --name dev_env_manager
cd dev_env_manager
# Configure for development team environments
```

### Example 3: Customer Deployment Platform

```bash
python3 init.py --name customer_platform
cd customer_platform
# Configure for customer-facing deployments
```

## Customization

After initialization, you can customize the project:

### 1. Add Custom Modules

Create new modules in the main package:

```bash
mkdir <module_name>/custom_module
touch <module_name>/custom_module/__init__.py
```

### 2. Extend Django Application

Add new Django apps:

```bash
cd <module_name>/django_app
python ../../manage.py startapp new_app
```

### 3. Add Custom Templates

Create Docker Compose templates:

```bash
cp config/templates/docker-compose.yml.template \
   config/templates/my-custom-template.yml.template
```

### 4. Implement Custom Validators

Add validation logic:

```bash
touch <module_name>/compose/validators/custom_validator.py
```

## Version Pinning

All dependencies are pinned to specific versions compatible with Python 3.9-3.13:

- Django 5.0.13 (LTS)
- pandas 2.2.3
- numpy 2.1.3
- netmiko 4.4.0
- napalm 5.0.0
- docker 7.1.0

To update dependencies:

```bash
# Review available updates
pip list --outdated

# Update specific package
pip install --upgrade package_name==version

# Update requirements.txt
pip freeze > requirements.txt
```

## Testing

Run tests to verify the installation:

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/unit/

# Run with coverage
pytest --cov=<module_name> tests/
```

## Troubleshooting

### Issue: Import errors after initialization

**Solution**: Ensure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Docker connection errors

**Solution**: Verify Docker is running and accessible:
```bash
docker ps
```

### Issue: Database connection errors

**Solution**: Check database configuration in `.env`:
```bash
# Verify database settings
echo $DB_HOST
echo $DB_PORT
```

## Best Practices

1. **Use Virtual Environments**: Always create a virtual environment for isolation
2. **Version Control**: Initialize git repository after creation
3. **Environment Variables**: Never commit `.env` file with secrets
4. **Documentation**: Update README.md with project-specific information
5. **Testing**: Write tests for custom functionality
6. **Code Quality**: Use provided linting tools (black, flake8, mypy)

## Advanced Usage

### Multiple Environments

Create separate configurations for different environments:

```bash
# Production
python3 init.py --name prod_manager --path /opt/production

# Staging
python3 init.py --name staging_manager --path /opt/staging

# Development
python3 init.py --name dev_manager --path /home/user/development
```

### Template Customization

Modify the init.py script to include custom templates:

1. Edit `init.py`
2. Add custom template generation methods
3. Update the `run()` method to call your custom methods

### Integration with CI/CD

Use init.py in your CI/CD pipeline:

```yaml
# Example GitLab CI configuration
stages:
  - init
  - test
  - deploy

init_project:
  stage: init
  script:
    - python3 init.py --name $CI_PROJECT_NAME
    - cd $CI_PROJECT_NAME
    - pip install -r requirements.txt
```

## Support

For issues or questions:

1. Check the README.md in the generated project
2. Review the API documentation in `docs/api/`
3. Examine example configurations in `config/`
4. Open an issue on the repository

## License

See LICENSE file in the generated project for details.
