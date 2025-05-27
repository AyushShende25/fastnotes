FROM python:3.13.3-slim@sha256:56a11364ffe0fee3bd60af6d6d5209eba8a99c2c16dc4c7c5861dc06261503cc

ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    gcc \
    libpq-dev \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create a non-root user
RUN useradd -m appuser

# Set work directory
WORKDIR /usr/src/app

# Install Dependencies
COPY --chown=appuser:appuser pyproject.toml uv.lock ./
RUN uv venv && \
    uv sync --frozen --no-cache

# Copy project files
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

# Expose the app port
EXPOSE 8000

# Run migrations and start app
ENTRYPOINT ["uv", "run", "fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
