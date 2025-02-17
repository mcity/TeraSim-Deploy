# Build arguments
ARG BASE_IMAGE=terasim_base
ARG VERSION=latest
ARG VARIANT=cpu

# Use the specified base image
FROM ${BASE_IMAGE}:${VERSION}-${VARIANT}

# Copy TeraSim-Service package
COPY TeraSim-Service/terasim_service /app/terasim_service
COPY TeraSim-Service/pyproject.toml TeraSim-Service/poetry.lock /app/

# Install poetry if not already installed
RUN pip install --no-cache-dir poetry

# Install package
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Expose service port
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app:${PYTHONPATH}

# Set the default command
CMD ["python", "-m", "terasim_service.main"] 