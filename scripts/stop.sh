#!/bin/bash

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "Stopping TeraSim service..."

# Stop the services
docker-compose -f docker/docker-compose.yml down

echo "Service stopped successfully" 