#!/bin/bash

# Function to check if a command exists
check_command() {
    if ! command -v $1 &> /dev/null; then
        echo "Error: $1 is not installed. Please install it first."
        exit 1
    fi
}

# Check required commands
check_command docker
check_command docker-compose
check_command curl

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "Starting TeraSim service..."

# Start the services
docker-compose -f docker/docker-compose.yml up -d

# Wait for service to be ready
echo "Waiting for service to be ready..."
for i in {1..30}; do
    if curl -s http://localhost:8000/health &> /dev/null; then
        echo "Service is ready!"
        echo "API documentation available at: http://localhost:8000/docs"
        exit 0
    fi
    echo "Waiting... ($i/30)"
    sleep 1
done

echo "Error: Service failed to start. Please check logs with: docker-compose -f docker/docker-compose.yml logs"
exit 1 