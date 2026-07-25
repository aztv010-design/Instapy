# Installation Guide

## Prerequisites

- Docker & Docker Compose
- Git
- 8GB RAM minimum
- 50GB disk space

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/aztv010-design/Instapy.git
cd Instapy
```

### 2. Configure Environment

```bash
cd deployment
cp .env.example .env
```

Edit `.env` with your settings:
- Database credentials
- API keys
- Security settings

### 3. Initialize and Start

```bash
make init
make up
make migrate
make populate-db
```

### 4. Access the Application

- **Frontend:** http://localhost:9003
- **API Docs:** http://localhost:8000/api/docs/
- **Admin Panel:** http://localhost:8000/admin/

## Docker Commands

```bash
# View logs
make logs

# Stop services
make down

# Backup database
make backup

# Database shell
make db-shell
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 9003
lsof -i :9003
# Kill the process
kill -9 <PID>
```

### Database Connection Error

```bash
# Check database logs
docker compose logs postgres

# Restart database
docker compose restart postgres
```

### Out of Memory

```bash
# Increase Docker memory in settings
# Recommended: 4GB minimum
```

## Production Deployment

```bash
make deploy
```

This uses `docker-compose.prod.yml` for production settings.

## Next Steps

1. Read the [User Guide](./user-guide.md)
2. Check the [API Reference](./api-reference.md)
3. Configure [Security Settings](./security.md)
