#!/bin/bash

echo "🧹 Cleaning up Instapy..."

# Stop and remove containers
echo "Removing containers..."
docker compose down -v --remove-orphans

# Remove volumes
echo "Removing volumes..."
docker volume rm instapy_postgres_data instapy_redis_data instapy_elasticsearch_data 2>/dev/null || true

# Remove images
echo "Removing images..."
docker rmi instapy_instapy instapy_frontend instapy_celery 2>/dev/null || true

echo "✅ Cleanup complete!"
