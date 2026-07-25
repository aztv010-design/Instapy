# Deployment Guide

## Prerequisites

- VPS or Cloud Server (AWS, DigitalOcean, etc.)
- Domain name
- SSL certificate
- 2GB RAM minimum
- 50GB storage

## Server Setup

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r backend/requirements.txt
        pip install pytest pytest-django


```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose git nginx certbot python3-certbot-nginx

# Add user to docker group
sudo usermod -aG docker $USER
```

### 2. Clone Repository

```bash
git clone https://github.com/aztv010-design/Instapy.git
cd Instapy
```

### 3. Configure Environment

```bash
cd deployment
cp .env.example .env
# Edit .env with production settings
nano .env
```

### 4. SSL Certificate

```bash
sudo certbot certonly --standalone -d yourdomain.com

# Copy certificates
sudo cp /etc/letsencrypt/live/yourdomain.com/fullchain.pem ./certificates/
sudo cp /etc/letsencrypt/live/yourdomain.com/privkey.pem ./certificates/
```

### 5. Deploy

```bash
make deploy
make migrate
```

## Nginx Configuration

Create `nginx.conf`:

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /etc/nginx/certs/fullchain.pem;
    ssl_certificate_key /etc/nginx/certs/privkey.pem;
    
    location /api {
        proxy_pass http://instapy:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location / {
        proxy_pass http://frontend:3000;
    }
}
```

## Monitoring

### Health Check

```bash
curl http://localhost:8000/api/health/
```

### View Logs

```bash
docker compose logs -f instapy
```

## Backup Strategy

```bash
# Daily backups
0 2 * * * cd /path/to/Instapy/deployment && make backup
```

## Updates

```bash
git pull origin main
make down
make build
make up
make migrate
```

## Scaling

### Increase Workers

```bash
# docker-compose.yml
command: gunicorn instapy.wsgi:application --bind 0.0.0.0:8000 --workers 8
```

### Load Balancing

Use Nginx as reverse proxy with multiple backend instances.
