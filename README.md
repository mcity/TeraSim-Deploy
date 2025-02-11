# TeraSim Simulation Platform

TeraSim is a powerful simulation platform for autonomous driving scenarios, providing a comprehensive environment for testing and validation.

## System Requirements

- Docker >= 20.10
- Docker Compose >= 2.0
- 8GB+ RAM
- 20GB+ free disk space
- Linux/macOS/Windows with WSL2

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd terasim-package
```

2. Make scripts executable:
```bash
chmod +x scripts/*.sh
```

3. Start the service:
```bash
./scripts/start.sh
```

4. Stop the service:
```bash
./scripts/stop.sh
```

## Directory Structure

```
terasim-package/
├── docker/             # Docker configuration files
├── config/             # Configuration files
├── maps/               # Simulation maps
├── scripts/            # Utility scripts
├── src/               # Source code
├── output/            # Simulation output
└── logs/              # Log files
```

## API Usage

### Python Example
```python
import requests

# Start a simulation
response = requests.post('http://localhost:8000/start_simulation', 
    json={
        "config_file": "/app/config/simulation_config.yaml",
        "auto_run": True
    })

simulation_id = response.json()['simulation_id']

# Get simulation status
status = requests.get(f'http://localhost:8000/simulation_status/{simulation_id}')

# Control vehicles
requests.post(f'http://localhost:8000/simulation/{simulation_id}/vehicle_command',
    json={
        "vehicle_id": "ego",
        "type": "set_state",
        "speed": 30.0
    })
```

## Configuration

The main configuration file is located at `config/simulation_config.yaml`. Key configuration options:

- `output`: Output directory settings
- `environment`: Simulation environment configuration
- `simulator`: Simulator parameters
- `file_paths`: Map and configuration file paths
- `logging`: Logging settings

## Troubleshooting

1. Service fails to start:
   - Check Docker logs: `docker-compose -f docker/docker-compose.yml logs`
   - Verify port 8000 is not in use
   - Ensure Redis is running: `docker ps | grep redis`

2. Cannot connect to API:
   - Verify service is running: `curl http://localhost:8000/health`
   - Check firewall settings

## Support

For technical support or bug reports, please contact:
- Email: support@terasim.com
- Issue Tracker: <repository-url>/issues 