# Instapy Project Setup Instructions

## Quick Setup

```bash
# 1. Clone
git clone https://github.com/aztv010-design/Instapy.git
cd Instapy/deployment

# 2. Configure
cp .env.example .env
# Edit .env

# 3. Start
make init
make up
make migrate

# 4. Access
# Frontend: http://localhost:9003
# API: http://localhost:8000/api/docs/
# Admin: http://localhost:8000/admin/
```

## Project Structure

```
Instapy/
├── backend/              # Django Backend
├── frontend/             # React Frontend
├── deployment/           # Docker & Deployment
├── docs/                 # Documentation
├── ml_models/            # ML Models
└── README.md
```

## Key Features ✨

✅ Instagram Profile Analysis
✅ Fake Account Detection (AI)
✅ Network Analysis
✅ Geolocation Tracking
✅ Report Generation
✅ Machine Learning Models
✅ REST API
✅ Real-time Monitoring
✅ Data Export
✅ Advanced Analytics

## Support

- 📖 [Installation Guide](./docs/installation.md)
- 📚 [API Reference](./docs/api-reference.md)
- 🔧 [Development Guide](./docs/development.md)
- 🚀 [Deployment Guide](./docs/deployment.md)
- 🔐 [Security Guidelines](./docs/security.md)

## Legal Notice ⚖️

This tool is for lawful purposes only. Users are responsible for complying with all applicable laws and Instagram's Terms of Service.
