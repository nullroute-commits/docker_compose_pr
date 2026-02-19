# Quick Start Guide

Get started with Docker Compose Manager in 5 minutes.

## Installation

### Step 1: Create Your Project

```bash
# Use the init script to create your project
python3 init.py --name my_orchestrator

# Navigate to project directory
cd my_orchestrator
```

### Step 2: Set Up Environment

#### Option A: Using Poetry (Recommended)

```bash
# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

#### Option B: Using Docker (Fastest)

```bash
# Copy environment template
cp .env.template .env

# Build and start services
docker compose up -d

# Initialize database
docker compose exec web python manage.py migrate
```

#### Option C: Using pip (Legacy)

```bash
# Create virtual environment
python3.13 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure

```bash
# Copy environment template
cp .env.template .env

# Edit configuration (optional for quick start)
# nano .env
```

## Basic Usage

### Create a Tenant

```python
from my_orchestrator.multitenant import TenantManager

# Initialize tenant manager
manager = TenantManager()

# Create a new tenant
tenant = manager.create_tenant(
    name="Demo Company",
    slug="demo_company",
    description="Demo tenant for testing",
    max_deployments=5
)

print(f"Created tenant: {tenant.name}")
```

### Deploy Docker Compose Application

```python
from my_orchestrator.compose.deployment.manager import DeploymentManager

# Initialize deployment manager
deployer = DeploymentManager()

# Validate compose file
deployer.validate_compose_file("config/templates/docker-compose.yml.template")

# List active deployments
deployments = deployer.list_deployments()
print(f"Active deployments: {len(deployments)}")
```

### Use Advanced Logging

```python
from my_orchestrator.core.logging import get_logger

# Get logger instance
logger = get_logger(__name__)

# Log with structured data
logger.info(
    "Deployment started",
    extra={
        'context': {
            'tenant': 'demo_company',
            'deployment': 'webapp',
            'version': '1.0.0'
        }
    }
)
```

## Example: Complete Workflow

Here's a complete example deploying an application for a tenant:

```python
#!/usr/bin/env python3
"""Example: Deploy application for a tenant."""

import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from my_orchestrator.multitenant import TenantManager
from my_orchestrator.compose.deployment.manager import DeploymentManager
from my_orchestrator.core.logging import get_logger

# Initialize
logger = get_logger(__name__)
tenant_manager = TenantManager()
deployer = DeploymentManager()

def main():
    """Main workflow."""
    
    # 1. Create tenant if not exists
    tenant = tenant_manager.get_tenant("customer_a")
    if not tenant:
        logger.info("Creating new tenant")
        tenant = tenant_manager.create_tenant(
            name="Customer A",
            slug="customer_a",
            description="First customer",
            max_deployments=10
        )
    
    # 2. List existing deployments
    deployments = deployer.list_deployments(tenant="customer_a")
    logger.info(f"Found {len(deployments)} existing deployments")
    
    # 3. Validate compose file
    compose_file = "config/templates/docker-compose.yml.template"
    try:
        deployer.validate_compose_file(compose_file)
        logger.info("Compose file is valid")
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return 1
    
    # 4. Deploy application
    logger.info("Deploying application")
    result = deployer.deploy_compose(
        compose_file=compose_file,
        project_name=f"{tenant.slug}_webapp",
        env_vars={
            'TENANT_ID': tenant.slug,
            'WEBAPP_PORT': '8080'
        }
    )
    
    logger.info(f"Deployment complete: {result['status']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

Save this as `example_deployment.py` and run:

```bash
python example_deployment.py
```

## Configuration Examples

### Environment Variables (.env)

```bash
# Application
APP_NAME=my_orchestrator
ENVIRONMENT=development
DEBUG=true

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=orchestrator_db
DB_USER=orchestrator_user
DB_PASSWORD=your_secure_password

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# Docker
DOCKER_SOCKET=unix:///var/run/docker.sock

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/application.log
```

### YAML Configuration (config/config.yaml)

```yaml
app_name: my_orchestrator
environment: production
debug: false

database:
  host: localhost
  port: 5432
  name: orchestrator_db
  user: orchestrator_user
  password: secure_password

redis:
  host: localhost
  port: 6379
  db: 0

docker:
  socket: unix:///var/run/docker.sock
  api_version: auto

logging:
  level: INFO
  file: logs/application.log

multitenant:
  enabled: true
  default_tenant: default
```

## Docker Compose Template Example

Create a template in `config/templates/nginx.yml.template`:

```yaml
version: '3.8'

services:
  nginx:
    image: nginx:1.24-alpine
    container_name: ${TENANT_ID}_nginx
    restart: unless-stopped
    ports:
      - "${NGINX_PORT:-80}:80"
      - "${NGINX_SSL_PORT:-443}:443"
    volumes:
      - ${TENANT_ID}_nginx_conf:/etc/nginx/conf.d
      - ${TENANT_ID}_nginx_html:/usr/share/nginx/html
      - ${TENANT_ID}_nginx_logs:/var/log/nginx
    networks:
      - ${TENANT_ID}_network
    labels:
      - "com.docker.compose.project=${TENANT_ID}"
      - "tenant=${TENANT_ID}"
      - "service=nginx"

networks:
  ${TENANT_ID}_network:
    driver: bridge
    name: ${TENANT_ID}_network

volumes:
  ${TENANT_ID}_nginx_conf:
    name: ${TENANT_ID}_nginx_conf
  ${TENANT_ID}_nginx_html:
    name: ${TENANT_ID}_nginx_html
  ${TENANT_ID}_nginx_logs:
    name: ${TENANT_ID}_nginx_logs
```

## Testing Your Setup

### Run Unit Tests

#### Using Poetry
```bash
# Run all tests
poetry run pytest tests/

# Run specific test file
poetry run pytest tests/unit/test_tenant.py

# Run with verbose output
poetry run pytest -v tests/

# Run with coverage report
poetry run pytest --cov=my_orchestrator tests/
```

#### Using Docker
```bash
# Run all tests
docker compose exec web pytest tests/

# Run with coverage
docker compose exec web pytest --cov=my_orchestrator tests/
```

#### Using pip
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/unit/test_tenant.py

# Run with verbose output
pytest -v tests/

# Run with coverage report
pytest --cov=my_orchestrator tests/
```

### Test Imports

```python
# Test that all modules can be imported
python3 -c "
from my_orchestrator.multitenant import TenantManager
from my_orchestrator.compose.deployment.manager import DeploymentManager
from my_orchestrator.core.logging import get_logger
from my_orchestrator.core.config import load_config
print('✓ All imports successful')
"
```

## Common Operations

### List All Tenants

```python
from my_orchestrator.multitenant import TenantManager

manager = TenantManager()
tenants = manager.list_tenants(active_only=True)

for tenant in tenants:
    print(f"- {tenant.name} ({tenant.slug})")
```

### Update Tenant

```python
from my_orchestrator.multitenant import TenantManager

manager = TenantManager()
tenant = manager.update_tenant(
    slug="customer_a",
    max_deployments=20,
    max_containers=100
)
```

### Stop Deployment

```python
from my_orchestrator.compose.deployment.manager import DeploymentManager

deployer = DeploymentManager()
success = deployer.stop_deployment("customer_a_webapp")
print(f"Deployment stopped: {success}")
```

### Remove Deployment

```python
from my_orchestrator.compose.deployment.manager import DeploymentManager

deployer = DeploymentManager()
success = deployer.remove_deployment("customer_a_webapp")
print(f"Deployment removed: {success}")
```

## Next Steps

1. **Read the Full Documentation**: Check `README.md` for detailed information
2. **Explore Examples**: Look at example scripts in `scripts/` directory
3. **Customize Configuration**: Modify templates in `config/templates/`
4. **Add Custom Logic**: Extend modules with your business logic
5. **Set Up Django**: Configure Django admin interface
6. **Enable Network Automation**: Configure Netmiko/NAPALM for network devices
7. **Set Up Monitoring**: Configure logging and monitoring

## Troubleshooting

### Can't import modules

Ensure you're in the virtual environment and dependencies are installed:

#### Using Poetry
```bash
poetry install
poetry shell
```

#### Using Docker
```bash
docker compose up -d
docker compose exec web python -c "import my_orchestrator; print('OK')"
```

#### Using pip
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Docker connection errors

Check Docker is running:
```bash
docker ps
```

Check Docker Compose services:
```bash
docker compose ps
docker compose logs web
```

### Permission errors

Ensure your user has Docker permissions:
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

## Resources

- Full documentation: `docs/`
- API documentation: `docs/api/README.md`
- Initialization guide: `docs/guides/INITIALIZATION.md`
- Example configurations: `config/`
- Tests: `tests/`

## Getting Help

- Check the README.md file
- Review example code in tests/
- Examine template configurations in config/
- Open an issue on the repository

Happy orchestrating! 🚀
