#!/bin/bash

# Check if Docker is installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'Error: Docker is not installed.' >&2
  echo 'Please install Docker before running this script.' >&2
  echo 'You can download it from: https://www.docker.com/products/docker-desktop' >&2
  exit 1
fi

# Check if docker-compose is installed
if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  echo 'Please install Docker Desktop, which includes docker-compose.' >&2
  echo 'You can download it from: https://www.docker.com/products/docker-desktop' >&2
  exit 1
fi

# Build and run the application
echo "Starting Project Thunderbird..."
docker-compose build
docker-compose up -d

echo "Project Thunderbird is running!"
echo "You can access it at: http://localhost:5001"
