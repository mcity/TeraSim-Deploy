# Build arguments
ARG BASE_IMAGE=terasim_base
ARG VERSION=latest
ARG VARIANT=cpu

# Use the specified base image
FROM ${BASE_IMAGE}:${VERSION}-${VARIANT}

# Copy TeraSim core package
COPY TeraSim/terasim /app/terasim
COPY TeraSim/pyproject.toml TeraSim/poetry.lock /app/

# Install poetry
RUN pip install --no-cache-dir poetry

# Install TeraSim package
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Set environment variables
ENV PYTHONPATH=/app:${PYTHONPATH} 