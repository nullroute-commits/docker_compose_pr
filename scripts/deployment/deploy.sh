#!/bin/bash
# Deployment automation script

set -e

echo "Docker Compose Manager - Deployment Script"
echo "==========================================="

# Check Python version
python_version=$(python3 --version)
echo "Python version: $python_version"

# Check Docker
docker_version=$(docker --version)
echo "Docker version: $docker_version"

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Deployment complete!"
