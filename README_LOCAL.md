# Local Development Setup Guide

## Prerequisites

- Ubuntu 22.04 (x86)
- Python 3.10 
- Poetry (Python package manager)
- Conda (for virtual environment management)
- Redis (running on port 6379)

## Environment Setup

1. Install and start Redis:
```bash
sudo apt-get update
sudo apt-get install redis-server
sudo systemctl start redis-server
sudo systemctl enable redis-server
```

2. Create and activate a Conda virtual environment:
```bash
conda create -n terasim python=3.10
conda activate terasim
```

3. Install Poetry if not already installed:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

4. Navigate to the project directory and install dependencies:
```bash
bash download_repo.sh
cd TeraSim
poetry install
cd ..
cd TeraSim-NDE-NADE
poetry install
cd ..
cd TeraSim-Service
poetry install
```

## Running the Service

1. Start the HTTP co-simulation service:
```bash
python safetest_http_cosim_main.py
```

## Testing the Service

You can use the provided REST file to test the HTTP endpoints:

1. Open `examples/terasim_request.rest` in your preferred REST client (e.g., VS Code REST Client extension)
2. Send HTTP requests to test the service functionality

## Notes

- Make sure all dependencies are properly installed before running the service
- The service must be running before sending test requests
- Check the logs for any potential errors during execution
