# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables for Python buffering and UTF-8 encoding
ENV PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH="$PATH:/root/.poetry/bin"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        libssl-dev \
        libffi-dev \
        postgresql \
        postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the working directory
COPY pyproject.toml poetry.lock ./


# Copy the project files to the working directory
COPY . .

# Install project dependencies
RUN poetry install

# PostgreSQL configuration
ENV POSTGRES_DB=hackathon
ENV POSTGRES_USER=ozimiz
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

# Expose the port that the Django app will run on
EXPOSE 8000

# Run the Django development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
