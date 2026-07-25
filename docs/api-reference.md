# API Reference

## Authentication

All API endpoints require authentication using a token.

### Get Token

```bash
POST /api/auth/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:

```json
{
  "token": "abc123..."
}
```

### Using Token

```bash
Authorization: Token abc123...
```

## Profile Analysis

### Scan Profile

```bash
POST /api/profile/scan/
Authorization: Token <your_token>
Content-Type: application/json

{
  "username": "target_user"
}
```

Response:

```json
{
  "id": 1,
  "username": "target_user",
  "full_name": "User Name",
  "followers": 1000,
  "following": 500,
  "bio": "Bio text",
  "profile_pic": "https://...",
  "verified": false,
  "created_at": "2025-01-01T00:00:00Z"
}
```

### Get Profile

```bash
GET /api/profile/{username}/
Authorization: Token <your_token>
```

## Analysis

### Fake Account Detection

```bash
GET /api/analysis/fake-detection/{profile_id}/
Authorization: Token <your_token>
```

Response:

```json
{
  "is_fake": false,
  "confidence": 0.95,
  "factors": [
    {"name": "follower_ratio", "score": 0.9},
    {"name": "activity_pattern", "score": 0.95}
  ]
}
```

### Activity Analysis

```bash
GET /api/analysis/activity/{profile_id}/
Authorization: Token <your_token>
```

## Reports

### Generate Report

```bash
POST /api/reports/generate/
Authorization: Token <your_token>
Content-Type: application/json

{
  "profile_id": 1,
  "format": "pdf"
}
```

### Download Report

```bash
GET /api/reports/{report_id}/download/
Authorization: Token <your_token>
```

## Error Handling

### Status Codes

- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `404` - Not Found
- `500` - Server Error

### Error Response

```json
{
  "detail": "Error message",
  "code": "ERROR_CODE"
}
```

## Rate Limiting

- `60` requests per minute per user
- Header: `X-RateLimit-Remaining`

## Pagination

```bash
GET /api/profiles/?page=1&page_size=20
```

Response:

```json
{
  "count": 100,
  "next": "http://api.example.com/profiles/?page=2",
  "previous": null,
  "results": [...]
}
```
