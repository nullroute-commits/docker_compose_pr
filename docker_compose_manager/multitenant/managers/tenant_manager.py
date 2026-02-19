"""
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
