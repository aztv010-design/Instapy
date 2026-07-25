# Development Guide

## Environment Setup

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend
npm install
```

## Running Tests

### Backend Tests

```bash
cd backend
pytest
pytest --cov=apps  # With coverage
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Code Style

### Python

```bash
# Format code
black backend/

# Lint
flake8 backend/

# Type check
mypy backend/
```

### JavaScript

```bash
# Format
cd frontend
npm run format

# Lint
npm run lint
```

## Creating Models

### Django Model Example

```python
# apps/profile/models.py
from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    followers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.username
```

## Creating APIs

### DRF Serializer

```python
# apps/profile/serializers.py
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'full_name', 'followers']
```

### ViewSet

```python
# apps/profile/views.py
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
```

## Database Migrations

```bash
# Create migration
python manage.py makemigrations

# Apply migration
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

## Celery Tasks

```python
# apps/analysis/tasks.py
from celery import shared_task

@shared_task
def analyze_profile(profile_id):
    profile = Profile.objects.get(id=profile_id)
    # Analysis logic here
    return f"Analyzed {profile.username}"
```

## Git Workflow

```bash
# Create branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/new-feature
```

## Debugging

### Django Debug Toolbar

Set `ENABLE_DEBUG_TOOLBAR=True` in `.env`

### VS Code Debugger

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/backend/manage.py",
      "args": ["runserver"],
      "django": true
    }
  ]
}
```
