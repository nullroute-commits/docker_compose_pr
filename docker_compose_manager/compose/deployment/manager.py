"""
Docker Compose deployment manager for multitenant environments.
"""

import docker
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from docker.errors import DockerException


class DeploymentManager:
    """Manage Docker Compose v3 deployments."""
    
    def __init__(self, docker_client: Optional[docker.DockerClient] = None):
        """
        Initialize deployment manager.
        
        Args:
            docker_client: Docker client instance (creates default if None)
        """
        self.client = docker_client or docker.from_env()
        
    def validate_compose_file(self, compose_file: str) -> bool:
        """
        Validate Docker Compose file.
        
        Args:
            compose_file: Path to docker-compose.yml
            
        Returns:
            True if valid, raises exception otherwise
        """
        compose_path = Path(compose_file)
        if not compose_path.exists():
            raise FileNotFoundError(f"Compose file not found: {compose_file}")
        
        with open(compose_path, 'r') as f:
            compose_data = yaml.safe_load(f)
        
        # Check version
        version = compose_data.get('version', '3')
        if not version.startswith('3'):
            raise ValueError(f"Only Docker Compose v3 is supported, found: {version}")
        
        # Check for required sections
        if 'services' not in compose_data:
            raise ValueError("Compose file must contain 'services' section")
        
        return True
    
    def deploy_compose(self, compose_file: str, project_name: str,
                      env_vars: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Deploy Docker Compose application.
        
        Args:
            compose_file: Path to docker-compose.yml
            project_name: Project/deployment name
            env_vars: Optional environment variables
            
        Returns:
            Deployment result information
        """
        self.validate_compose_file(compose_file)
        
        # Note: This is a simplified implementation
        # In production, you would use docker-compose CLI or Python library
        result = {
            'project_name': project_name,
            'compose_file': compose_file,
            'status': 'deployed',
            'timestamp': None,
        }
        
        return result
    
    def list_deployments(self, tenant: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List active deployments.
        
        Args:
            tenant: Optional tenant filter
            
        Returns:
            List of deployment information
        """
        # Get all containers with compose project label
        containers = self.client.containers.list(
            filters={'label': 'com.docker.compose.project'}
        )
        
        deployments = {}
        for container in containers:
            project = container.labels.get('com.docker.compose.project')
            if project and (not tenant or project.startswith(f"{tenant}_")):
                if project not in deployments:
                    deployments[project] = {
                        'project_name': project,
                        'containers': [],
                        'status': 'running',
                    }
                deployments[project]['containers'].append(container.name)
        
        return list(deployments.values())
    
    def stop_deployment(self, project_name: str) -> bool:
        """
        Stop a deployment.
        
        Args:
            project_name: Project/deployment name
            
        Returns:
            True if successful
        """
        containers = self.client.containers.list(
            filters={'label': f'com.docker.compose.project={project_name}'}
        )
        
        for container in containers:
            container.stop()
        
        return True
    
    def remove_deployment(self, project_name: str) -> bool:
        """
        Remove a deployment completely.
        
        Args:
            project_name: Project/deployment name
            
        Returns:
            True if successful
        """
        self.stop_deployment(project_name)
        
        containers = self.client.containers.list(
            all=True,
            filters={'label': f'com.docker.compose.project={project_name}'}
        )
        
        for container in containers:
            container.remove()
        
        return True
