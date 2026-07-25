# Main Makefile for Instapy
include .env

.PHONY: help init up down logs build pull deploy migrate backup clean status restart db-shell

help:
	@echo "================================"
	@echo "  INSTAPY - Available Commands"
	@echo "================================"
	@echo "  init             - Initialize the project"
	@echo "  up               - Start all services"
	@echo "  down             - Stop all services"
	@echo "  build            - Build Docker images"
	@echo "  pull             - Pull Docker images"
	@echo "  logs             - Show live logs"
	@echo "  migrate          - Run database migrations"
	@echo "  superuser        - Create admin user"
	@echo "  populate-db      - Load sample data"
	@echo "  backup           - Backup database"
	@echo "  db-shell         - Open database shell"
	@echo "  health-check     - Check services health"
	@echo "  deploy           - Deploy to production"
	@echo "  clean            - Clean all containers and volumes"
	@echo "  status           - Show service status"
	@echo "  restart          - Restart services"
	@echo "================================"

init:
	@bash init.sh

up:
	@echo "🚀 Starting Instapy services..."
	@docker compose --env-file .env up -d
	@echo "⏳ Waiting for services to be healthy..."
	@sleep 5
	@docker compose ps
	@echo "✅ Services started successfully!"
	@echo "🌐 Access at http://localhost:9003"

down:
	@echo "⛔ Stopping Instapy services..."
	@docker compose --env-file .env down --remove-orphans
	@echo "✅ Services stopped"

build:
	@echo "🔨 Building Docker images..."
	@docker compose --env-file .env build --no-cache
	@echo "✅ Build complete"

pull:
	@echo "⬇️  Pulling Docker images..."
	@docker compose --env-file .env pull
	@echo "✅ Images pulled"

logs:
	@echo "📋 Showing live logs..."
	@docker compose --env-file .env logs -f instapy

migrate:
	@echo "📊 Running database migrations..."
	@docker compose --env-file .env exec -T instapy python manage.py migrate
	@echo "✅ Migrations complete"

superuser:
	@echo "👤 Creating superuser account..."
	@docker compose --env-file .env exec instapy python manage.py createsuperuser

populate-db:
	@echo "🌱 Populating database with sample data..."
	@docker compose --env-file .env exec -T instapy python manage.py shell < ../backend/apps/profile/management/commands/populate_db.py
	@echo "✅ Database populated"

backup:
	@echo "💾 Backing up database..."
	@mkdir -p backups
	@docker compose --env-file .env exec -T postgres pg_dump -U $(DB_USER) $(DB_NAME) > backups/instapy_backup_$$(date +%Y%m%d_%H%M%S).sql
	@echo "✅ Backup created"

db-shell:
	@echo "🐘 Opening PostgreSQL shell..."
	@docker compose --env-file .env exec postgres psql -U $(DB_USER) -d $(DB_NAME)

health-check:
	@bash health-check.sh

deploy:
	@echo "🚀 Deploying to production..."
	@docker compose --env-file .env -f docker-compose.yml -f docker-compose.prod.yml up -d
	@echo "✅ Deployment complete"

clean:
	@bash cleanup.sh

status:
	@echo "📊 Service Status:"
	@docker compose --env-file .env ps

restart:
	@echo "🔄 Restarting services..."
	@docker compose --env-file .env restart
	@echo "✅ Services restarted"
