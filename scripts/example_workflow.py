#!/usr/bin/env python3
"""
Example: Multitenant Deployment Workflow

This example demonstrates a complete workflow for managing multitenant
Docker Compose deployments using the Docker Compose Manager.

Features demonstrated:
- Creating and managing tenants
- Deploying Docker Compose applications
- Listing and monitoring deployments
- Using structured JSON logging
- Configuration management
"""

import sys
import os
from pathlib import Path

# Add project to path (adjust based on your setup)
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from docker_compose_manager.multitenant.managers.tenant_manager import TenantManager
from docker_compose_manager.multitenant.models.tenant import Tenant
from docker_compose_manager.compose.deployment.manager import DeploymentManager
from docker_compose_manager.core.config.loader import Config, load_config
from docker_compose_manager.core.logging.json_logger import get_logger


def setup_logging():
    """Set up structured logging."""
    return get_logger(__name__, log_file="logs/example.log")


def create_sample_tenants(logger):
    """Create sample tenants for demonstration."""
    logger.info("Creating sample tenants")
    
    manager = TenantManager()
    
    # Create tenants if they don't exist
    tenants_to_create = [
        {
            "name": "Acme Corporation",
            "slug": "acme_corp",
            "description": "Enterprise customer with high resource limits",
            "max_deployments": 20,
            "max_containers": 100,
            "max_cpu": 8.0,
            "max_memory": 16384,
        },
        {
            "name": "Beta Inc",
            "slug": "beta_inc",
            "description": "Medium-sized customer",
            "max_deployments": 10,
            "max_containers": 50,
            "max_cpu": 4.0,
            "max_memory": 8192,
        },
        {
            "name": "Gamma LLC",
            "slug": "gamma_llc",
            "description": "Small customer with basic needs",
            "max_deployments": 5,
            "max_containers": 20,
            "max_cpu": 2.0,
            "max_memory": 4096,
        },
    ]
    
    created = []
    for tenant_data in tenants_to_create:
        slug = tenant_data["slug"]
        existing = manager.get_tenant(slug)
        
        if existing:
            logger.info(f"Tenant already exists: {slug}")
            created.append(existing)
        else:
            tenant = manager.create_tenant(**tenant_data)
            logger.info(
                f"Created tenant: {tenant.name}",
                extra={'context': {'tenant_id': tenant.id, 'slug': tenant.slug}}
            )
            created.append(tenant)
    
    return created


def list_tenants(logger):
    """List all tenants."""
    logger.info("Listing all tenants")
    
    manager = TenantManager()
    tenants = manager.list_tenants(active_only=True)
    
    print("\n" + "="*70)
    print("ACTIVE TENANTS")
    print("="*70)
    
    for tenant in tenants:
        print(f"\n{tenant.name} ({tenant.slug})")
        print(f"  Description: {tenant.description}")
        print(f"  Max Deployments: {tenant.max_deployments}")
        print(f"  Max Containers: {tenant.max_containers}")
        if tenant.max_cpu:
            print(f"  Max CPU: {tenant.max_cpu} cores")
        if tenant.max_memory:
            print(f"  Max Memory: {tenant.max_memory} MB")
        print(f"  Created: {tenant.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n" + "="*70 + "\n")
    
    return tenants


def demonstrate_deployment_validation(logger):
    """Demonstrate Docker Compose file validation."""
    logger.info("Demonstrating deployment validation")
    
    deployer = DeploymentManager()
    
    # Check if template exists
    template_file = "config/templates/docker-compose.yml.template"
    if not Path(template_file).exists():
        logger.warning(f"Template file not found: {template_file}")
        print(f"\n⚠ Template file not found: {template_file}")
        return False
    
    try:
        # Validate the compose file
        is_valid = deployer.validate_compose_file(template_file)
        logger.info(f"Compose file validation result: {is_valid}")
        print(f"\n✓ Compose file is valid: {template_file}")
        return True
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        print(f"\n✗ Validation failed: {e}")
        return False


def demonstrate_deployment_listing(logger):
    """Demonstrate listing active deployments."""
    logger.info("Listing active deployments")
    
    deployer = DeploymentManager()
    
    try:
        all_deployments = deployer.list_deployments()
        
        print("\n" + "="*70)
        print("ACTIVE DEPLOYMENTS")
        print("="*70)
        
        if not all_deployments:
            print("\nNo active deployments found.")
        else:
            for deployment in all_deployments:
                print(f"\nProject: {deployment['project_name']}")
                print(f"  Status: {deployment['status']}")
                print(f"  Containers: {', '.join(deployment['containers'])}")
        
        print("\n" + "="*70 + "\n")
        
        logger.info(f"Found {len(all_deployments)} active deployments")
        
    except Exception as e:
        logger.error(f"Failed to list deployments: {e}")
        print(f"\n✗ Error listing deployments: {e}")


def update_tenant_example(logger):
    """Demonstrate updating a tenant."""
    logger.info("Demonstrating tenant update")
    
    manager = TenantManager()
    
    # Update the first tenant
    tenant = manager.get_tenant("acme_corp")
    if tenant:
        updated = manager.update_tenant(
            slug="acme_corp",
            max_deployments=25,
            max_containers=150
        )
        
        logger.info(
            f"Updated tenant: {updated.name}",
            extra={'context': {'slug': updated.slug}}
        )
        print(f"\n✓ Updated tenant: {updated.name}")
        print(f"  New max deployments: {updated.max_deployments}")
        print(f"  New max containers: {updated.max_containers}")
    else:
        logger.warning("Tenant 'acme_corp' not found")
        print("\n⚠ Tenant 'acme_corp' not found")


def demonstrate_configuration(logger):
    """Demonstrate configuration loading."""
    logger.info("Demonstrating configuration management")
    
    # Load configuration from environment
    config = Config.from_env()
    
    print("\n" + "="*70)
    print("CONFIGURATION")
    print("="*70)
    print(f"\nApp Name: {config.app_name}")
    print(f"Environment: {config.environment}")
    print(f"Debug Mode: {config.debug}")
    print(f"Database Host: {config.database_host}")
    print(f"Database Port: {config.database_port}")
    print(f"Redis Host: {config.redis_host}")
    print(f"Log Level: {config.log_level}")
    print(f"Multitenancy Enabled: {config.enable_multitenancy}")
    print("\n" + "="*70 + "\n")


def main():
    """Main entry point."""
    print("\n" + "="*70)
    print("DOCKER COMPOSE MANAGER - EXAMPLE WORKFLOW")
    print("="*70 + "\n")
    
    # Set up logging
    logger = setup_logging()
    logger.info("Starting example workflow")
    
    try:
        # 1. Display configuration
        print("\n[1/6] Configuration Management")
        demonstrate_configuration(logger)
        
        # 2. Create sample tenants
        print("\n[2/6] Creating Sample Tenants")
        tenants = create_sample_tenants(logger)
        print(f"✓ Created/verified {len(tenants)} tenants")
        
        # 3. List all tenants
        print("\n[3/6] Listing Tenants")
        list_tenants(logger)
        
        # 4. Update a tenant
        print("\n[4/6] Updating Tenant")
        update_tenant_example(logger)
        
        # 5. Validate deployment configuration
        print("\n[5/6] Validating Deployment Configuration")
        demonstrate_deployment_validation(logger)
        
        # 6. List active deployments
        print("\n[6/6] Listing Active Deployments")
        demonstrate_deployment_listing(logger)
        
        logger.info("Example workflow completed successfully")
        print("\n" + "="*70)
        print("WORKFLOW COMPLETED SUCCESSFULLY")
        print("="*70 + "\n")
        
        print("Log file: logs/example.log")
        print("Tenant storage: deployments/tenants/")
        
        return 0
        
    except Exception as e:
        logger.error(f"Workflow failed: {e}", exc_info=True)
        print(f"\n✗ Error: {e}")
        return 1


if __name__ == "__main__":
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)
    
    # Run main workflow
    sys.exit(main())
