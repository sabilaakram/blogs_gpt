# Use the official Python image from the Docker Hub
FROM python:3.12

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    telnet \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["poetry", "run", "uvicorn", "blogs_gpt.main:app", "--host", "0.0.0.0", "--port", "8000"]
