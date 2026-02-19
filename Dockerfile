# Multi-stage Alpine-based Dockerfile for Docker Compose Manager
# Uses Poetry for dependency management

# Stage 1: Builder
FROM python:3.13-alpine AS builder

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    postgresql-dev \
    linux-headers \
    rust \
    cargo \
    openssl-dev \
    pkgconfig

# Install Poetry
ENV POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies
RUN poetry install --only main --no-root --no-directory

# Stage 2: Runtime
FROM python:3.13-alpine

# Install runtime dependencies
RUN apk add --no-cache \
    postgresql-libs \
    libffi \
    openssl

# Create non-root user
RUN addgroup -g 1000 dcm && \
    adduser -D -u 1000 -G dcm dcm

# Set working directory
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=dcm:dcm . .

# Create necessary directories
RUN mkdir -p /app/logs /app/deployments/tenants && \
    chown -R dcm:dcm /app

# Switch to non-root user
USER dcm

# Expose port for Django application
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app:${PATH}"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

# Default command
CMD ["gunicorn", "docker_compose_manager.django_app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
