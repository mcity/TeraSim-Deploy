# Build arguments
ARG BASE_IMAGE=terasim_base
ARG VERSION=latest
ARG VARIANT=cpu

# Use the specified base image
FROM ${BASE_IMAGE}:${VERSION}-${VARIANT}

USER root
# Copy TeraSim core package
COPY TeraSim /app/TeraSim

# Install poetry
RUN pip install --no-cache-dir poetry
ENV PATH=/root/.local/bin:${PATH}
RUN poetry config virtualenvs.create false

# Install TeraSim package
WORKDIR /app/TeraSim
RUN rm -rf poetry.lock
RUN poetry install

# Set environment variables
ENV PYTHONPATH=/app:${PYTHONPATH}

USER terasim

WORKDIR /app