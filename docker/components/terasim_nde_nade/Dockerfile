# Build arguments
ARG BASE_IMAGE=terasim_base
ARG VERSION=latest
ARG VARIANT=cpu

# Use the specified base image
FROM ${BASE_IMAGE}:${VERSION}-${VARIANT}

# Copy TeraSim-NDE-NADE package
COPY TeraSim-NDE-NADE/terasim_nde_nade /app/terasim_nde_nade
COPY TeraSim-NDE-NADE/pyproject.toml TeraSim-NDE-NADE/poetry.lock /app/

# Install poetry if not already installed
RUN pip install --no-cache-dir poetry

# Install package
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Set environment variables
ENV PYTHONPATH=/app:${PYTHONPATH} 