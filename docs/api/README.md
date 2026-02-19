# API Documentation

## REST API Endpoints

### Tenants

- `GET /api/tenants/` - List all tenants
- `POST /api/tenants/` - Create new tenant
- `GET /api/tenants/{slug}/` - Get tenant details
- `PUT /api/tenants/{slug}/` - Update tenant
- `DELETE /api/tenants/{slug}/` - Delete tenant

### Deployments

- `GET /api/deployments/` - List all deployments
- `POST /api/deployments/` - Create new deployment
- `GET /api/deployments/{id}/` - Get deployment details
- `PUT /api/deployments/{id}/` - Update deployment
- `DELETE /api/deployments/{id}/` - Delete deployment

### Health

- `GET /api/health/` - System health check

## Authentication

API uses token-based authentication. Include token in header:

```
Authorization: Token <your-token>
```
