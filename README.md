# TeraSim Deploy

TeraSim Deploy provides containerized deployment solutions for the TeraSim autonomous driving simulation platform. This repository orchestrates the deployment of various TeraSim components using Docker.

## Components

TeraSim Deploy integrates the following components:
- `terasim`: Core simulation engine
- `terasim_service`: HTTP service interface
- `terasim_nde_nade`: Neural differential equations component
<!-- - `terasim_data_zoo`: Data management utilities
- `terasim_gpt`: GPT-based simulation enhancement -->

## Prerequisites

- Docker >= 20.10
- Docker Compose >= 2.0
- NVIDIA Container Toolkit (for GPU support)
- 16GB+ RAM recommended
- 50GB+ free disk space

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/mcity/TeraSim-Deploy.git
cd Terasim-Deploy
bash download_repo.sh # download TeraSim, TeraSim-NDE-NADE, TeraSim-Service
```

2. Build images:
```bash
# For CPU version
./scripts/build.sh --version=1.0.0

# # For GPU version
# ./scripts/build.sh --version=1.0.0 --gpu

# # Build specific components
# ./scripts/build.sh --version=1.0.0 --gpu --components=terasim_service,terasim_nde_nade
```

3. Start services:
```bash
# Start all services
cd docker
docker-compose up -d

# # Start specific services
# docker-compose up -d terasim_service redis
```

4. Verify deployment:
```bash
curl http://localhost:8000/health
```

## Directory Structure

```
terasim-deploy/
├── docker/                 # Docker configuration
│   ├── base/              # Base image configuration
│   │   ├── Dockerfile.base.cpu
│   │   ├── Dockerfile.base.gpu
│   │   └── requirements.*.txt
│   ├── components/        # Component-specific Dockerfiles
│   │   ├── terasim/
│   │   ├── terasim_service/
│   │   └── ...
│   └── docker-compose.yml
├── config/                # Configuration files
│   ├── dev/              # Development configs
│   └── prod/             # Production configs
└── scripts/              # Utility scripts
    └── build.sh          # Build script
```

## Configuration

### Environment Variables

Key configuration options:
- `VERSION`: Version of TeraSim components
- `ENVIRONMENT`: Deployment environment (development/production)
- `CUDA_VISIBLE_DEVICES`: GPU device selection

### Component Configuration

Each component can be configured through:
- Environment variables
- Configuration files in `config/` directory
- Docker Compose overrides

## Health Monitoring

- Service health endpoint: `http://localhost:8000/health`
- Container health checks are configured in docker-compose.yml

## Scaling

```bash
# Scale specific services
docker compose up -d --scale terasim_service=3
```

## Troubleshooting

1. Image building issues:
```bash
# Check build logs
./scripts/build.sh --version=1.0.0 --gpu 2>&1 | tee build.log
```

2. Container issues:
```bash
# Check container logs
docker compose logs -f [service-name]
```

3. GPU support:
```bash
# Verify GPU access
docker run --rm --gpus all nvidia/cuda:12.1.1-base nvidia-smi
```

## Support

For deployment-related issues:
- GitHub Issues: <repository-url>/issues
- Documentation: <docs-url>

## License

[License Type] - See LICENSE file for details 