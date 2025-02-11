# Base image
FROM ubuntu:20.04

# Avoid timezone interactive prompt during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    wget \
    build-essential \
    python3-dev \
    python3-pip \
    python3-wheel \
    libgeos-dev \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y \
    python3.10 \
    python3.10-distutils \
    python3.10-dev \
    && wget https://bootstrap.pypa.io/get-pip.py \
    && python3.10 get-pip.py \
    && rm -rf /var/lib/apt/lists/* \
    && rm get-pip.py

# Install Redis
RUN apt-get update && \
    apt-get install -y redis-server && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code and requirements first
COPY requirements.txt /app/
COPY src/ /app/src/

# Install Python dependencies
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

# Copy other files
COPY config/ /app/config/
COPY maps/ /app/maps/

# Set environment variables
ENV PYTHONPATH=/app/src
ENV CONFIG_DIR=/app/config
ENV MAPS_DIR=/app/maps

# Create necessary directories
RUN mkdir -p /app/output /app/logs

# Expose service port
EXPOSE 8000

# Start command
CMD ["python3.10", "-m", "uvicorn", "src.TeraSim-Service.terasim_service:app", "--host", "0.0.0.0", "--port", "8000"] 