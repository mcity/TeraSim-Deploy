# TeraSim Deploy

<div align="center">
<p align="center">

<img src="docs/figure/terasim_deploy.svg" height="200px">

</p>
</div>

TeraSim Deploy provides containerized deployment solutions for the TeraSim autonomous driving simulation platform. This repository orchestrates the deployment of various TeraSim components using Docker and Kubernetes, enabling seamless integration and scalable deployment.

## Components

TeraSim Deploy integrates the following components:
- `terasim`: Core simulation engine
- `terasim_nde_nade`: Neural differential equations component
- `terasim_service`: HTTP service interface for I/O operations
- `terasim_macro`: Macro-level simulation capabilities
- `terasim_data_zoo`: Data management and dataset utilities
- `terasim_gpt`: GPT-based simulation enhancement

## Prerequisites

- Docker >= 20.10
- Docker Compose >= 2.0
- Kubernetes >= 1.20 (for K8s deployment)
- Helm >= 3.0 (for K8s deployment)
- 16GB+ RAM recommended
- 50GB+ free disk space

## Quick Start with Docker

1. Clone the repository:
```bash
git clone <repository-url>
cd terasim-deploy
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

3. Start the services:
```bash
# For development environment
docker compose -f docker/docker-compose.dev.yml up -d

# For production environment
docker compose -f docker/docker-compose.prod.yml up -d
```

4. Verify deployment:
```bash
curl http://localhost:8000/health
```

## Kubernetes Deployment

1. Add TeraSim Helm repository:
```bash
helm repo add terasim https://charts.terasim.com
helm repo update
```

2. Install using Helm:
```bash
# For development environment
helm install terasim-dev terasim/terasim-deploy -f values.dev.yaml

# For production environment
helm install terasim-prod terasim/terasim-deploy -f values.prod.yaml
```

## Directory Structure

```
terasim-deploy/
├── docker/                 # Docker configuration
│   ├── Dockerfile.*       # Component-specific Dockerfiles
│   └── docker-compose.*   # Environment-specific compose files
├── k8s/                   # Kubernetes configuration
│   ├── charts/           # Helm charts
│   └── manifests/        # K8s manifests
├── config/                # Configuration files
│   ├── dev/              # Development configs
│   └── prod/             # Production configs
├── scripts/               # Utility scripts
└── docs/                  # Documentation
```

## Configuration

### Docker Environment Variables

Key configuration options in `.env`:
- `TERASIM_VERSION`: Version of TeraSim components
- `SERVICE_PORT`: HTTP service port (default: 8000)
- `REDIS_URL`: Redis connection string
- `LOG_LEVEL`: Logging level

### Kubernetes Configuration

Key configuration options in `values.yaml`:
- `global.environment`: Deployment environment
- `components`: Component-specific settings
- `resources`: Resource allocation
- `persistence`: Storage configuration

## Health Monitoring

- Docker: `http://localhost:8000/health`
- Kubernetes: `http://terasim-service.namespace/health`

## Scaling

### Docker Compose

```bash
docker compose -f docker/docker-compose.prod.yml up -d --scale terasim_service=3
```

### Kubernetes

```bash
kubectl scale deployment terasim-service --replicas=3
```

## Troubleshooting

1. Component startup issues:
   ```bash
   # Check Docker logs
   docker compose logs [service-name]
   
   # Check K8s logs
   kubectl logs -l app=terasim-service
   ```

2. Resource constraints:
   - Verify resource allocation in Docker Compose or K8s manifests
   - Check node capacity in K8s cluster

3. Networking issues:
   - Verify service discovery configuration
   - Check network policies and security groups

## Support

For deployment-related issues:
- GitHub Issues: <repository-url>/issues
- Documentation: <docs-url>
- Email: support@terasim.com

## License

[License Type] - See LICENSE file for details 