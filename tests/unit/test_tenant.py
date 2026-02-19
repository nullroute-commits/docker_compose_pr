"""Test tenant management."""

import pytest
from docker_compose_manager.multitenant.models.tenant import Tenant
from docker_compose_manager.multitenant.managers.tenant_manager import TenantManager


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
