# Docker Compose Manager

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
- **Python 3.13 Compatible**: Fully compatible with Python 3.13+

## Installation

### Prerequisites

- Python 3.13+
- Docker Engine
- PostgreSQL (optional, for Django)
- Redis (optional, for caching)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd docker_compose_manager
```

2. Create and activate virtual environment:
```bash
python3.13 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
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
from docker_compose_manager.multitenant import TenantManager

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
from docker_compose_manager.compose import DeploymentManager

deployer = DeploymentManager()
result = deployer.deploy_compose(
    compose_file="deployments/customer_a/app.yml",
    project_name="customer_a_webapp"
)
```

### Using Advanced Logging

```python
from docker_compose_manager import get_logger

logger = get_logger(__name__)
logger.info("Application started", extra={'context': {'version': '1.0.0'}})
```

## Architecture

```
docker_compose_manager/
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
black docker_compose_manager/

# Lint code
flake8 docker_compose_manager/

# Type checking
mypy docker_compose_manager/
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
