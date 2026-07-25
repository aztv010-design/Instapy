# Security Guidelines

## Authentication

### Token Management

- Store tokens securely (never in localStorage)
- Use HTTP-only cookies when possible
- Rotate tokens regularly
- Revoke expired tokens

```python
# settings.py
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

## Encryption

### Data at Rest

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

encrypted_data = cipher.encrypt(b"sensitive data")
decrypted_data = cipher.decrypt(encrypted_data)
```

### Data in Transit

- Use HTTPS only
- Enable SSL/TLS
- Certificate pinning

## Input Validation

```python
from django.core.validators import URLValidator, EmailValidator

class Profile(models.Model):
    email = models.EmailField(validators=[EmailValidator()])
    website = models.URLField(validators=[URLValidator()])
```

## SQL Injection Prevention

```python
# ✅ Good - Using ORM
Profile.objects.filter(username=username)

# ❌ Bad - Raw SQL
Profile.objects.raw(f"SELECT * FROM profile WHERE username = '{username}'")
```

## CORS Configuration

```python
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
]

CORS_ALLOW_CREDENTIALS = True
```

## Rate Limiting

```python
from rest_framework.throttling import UserRateThrottle

class CustomRateThrottle(UserRateThrottle):
    scope = 'custom'
    THROTTLE_RATES = {'custom': '100/hour'}
```

## Audit Logging

```python
from django.contrib.admin.models import LogEntry

LogEntry.objects.create(
    user=user,
    content_type=ContentType.objects.get_for_model(Profile),
    object_id=profile.id,
    action_flag=CHANGE,
    change_message="Updated profile"
)
```

## OWASP Top 10 Compliance

1. ✅ Injection - Use ORM
2. ✅ Broken Auth - Use JWT/Token
3. ✅ Sensitive Data - Encrypt
4. ✅ XML External Entities - Parse safely
5. ✅ Broken Access Control - Use permissions
6. ✅ Security Misconfiguration - Follow guidelines
7. ✅ XSS - Sanitize inputs
8. ✅ Insecure Deserialization - Validate JSON
9. ✅ Using Components with Known Vulnerabilities - Update deps
10. ✅ Insufficient Logging - Enable audit logs
