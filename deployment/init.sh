#!/bin/bash

set -e

echo "🚀 Starting Instapy initialization..."

# Create necessary directories
mkdir -p logs data certificates
echo "✅ Created directories"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file"
else
    echo "⚠️  .env file already exists"
fi

# Create log directory
mkdir -p ../backend/logs
echo "✅ Created log directories"

echo ""
echo "🎉 Initialization complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit .env file with your configuration"
echo "2. Run: make up"
echo "3. Run: make migrate"
echo "4. Access: http://localhost:9003"
echo ""
