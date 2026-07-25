#!/bin/bash

echo "🔍 Running health checks..."

# Check Django
echo -n "Django API: "
curl -s http://localhost:8000/api/ > /dev/null && echo "✅" || echo "❌"

# Check Frontend
echo -n "Frontend: "
curl -s http://localhost:9003 > /dev/null && echo "✅" || echo "❌"

# Check Database
echo -n "PostgreSQL: "
docker compose exec -T postgres pg_isready -U instapy > /dev/null && echo "✅" || echo "❌"

# Check Redis
echo -n "Redis: "
docker compose exec -T redis redis-cli ping > /dev/null && echo "✅" || echo "❌"

# Check Elasticsearch
echo -n "Elasticsearch: "
curl -s http://localhost:9200 > /dev/null && echo "✅" || echo "❌"

echo ""
echo "✅ Health check complete!"
