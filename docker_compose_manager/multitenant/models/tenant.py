"""
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
