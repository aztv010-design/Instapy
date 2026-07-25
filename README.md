# 🔍 Instapy - Advanced Instagram OSINT Platform

**AI-Powered Instagram Intelligence & Analysis Platform**

![Status](https://img.shields.io/badge/Status-Development-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![React](https://img.shields.io/badge/React-18%2B-61DAFB)

---

## 🎯 ما هو Instapy؟

**Instapy** هي منصة متقدمة لجمع وتحليل بيانات Instagram بذكاء اصطناعي عالي، مصممة للتحقيقات الأمنية والبحث الأكاديمي.

### ✨ المميزات الرئيسية:

- 🔎 **جمع بيانات شاملة** - ملفات شخصية، صور، فيديوهات، stories
- 🤖 **تحليل ذكي بـ AI** - كشف الحسابات المزيفة والمريبة
- 🌍 **تتبع جغرافي** - تحديد المواقع والحركة
- 🔗 **كشف الروابط** - ربط البيانات والحسابات المرتبطة
- 📊 **رسوم بيانية متقدمة** - تصور العلاقات والشبكات
- 🎨 **تحليل الصور** - التعرف على الوجوه والنصوص (OCR)
- 📈 **تتبع النشاط** - مراقبة التغييرات والتطور
- 📄 **تقارير احترافية** - تصدير PDF/Excel
- 🔔 **نظام التنبيهات** - إخطارات ذكية وفورية
- 🔐 **أمان عسكري** - تشفير AES-256 وتسجيل شامل

---

## 🛠️ المتطلبات التقنية

### Frontend
- React 18+
- TypeScript
- Material-UI (MUI)
- D3.js / Recharts
- Redux Toolkit
- Leaflet (الخرائط)

### Backend
- Django 6.0+
- Django REST Framework
- Celery (المهام المتزامنة)
- Redis
- PostgreSQL

### AI/ML
- TensorFlow / PyTorch
- YOLO (كشف الوجوه)
- Tesseract (OCR)
- scikit-learn

### APIs الخارجية
- Instagram Graph API
- Google Vision API
- Reverse Image Search
- Geolocation Services

---

## 📋 التثبيت السريع

### المتطلبات الأساسية
```bash
- Docker & Docker Compose
- Git
- Python 3.10+
- Node.js 18+
```

### خطوات التثبيت

```bash
# 1. استنساخ المستودع
git clone https://github.com/aztv010-design/Instapy.git
cd Instapy

# 2. إنشاء البيئة
cp .env.example .env
cd deployment

# 3. التهيئة
make init

# 4. البدء
make up

# 5. إعداد قاعدة البيانات
make migrate
make superuser
make populate-db

# 6. الوصول
# http://localhost:9003
```

---

## 📁 هيكل المشروع

```
Instapy/
├── backend/                    # Django Backend
│   ├── instapy/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── profile/           # ملفات شخصية
│   │   ├── analysis/          # التحليل والذكاء الاصطناعي
│   │   ├── geolocation/       # البيانات الجغرافية
│   │   ├── relationship/      # العلاقات والشبكات
│   │   └── reports/           # التقارير
│   └── requirements.txt
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── store/
│   │   └── services/
│   └── package.json
├── deployment/                 # Docker & Deployment
│   ├── docker-compose.yml
│   ├── Makefile
│   └── .env.example
├── ml_models/                  # نماذج التعلم الآلي
│   ├── face_recognition/
│   ├── ocr/
│   └── fake_detection/
└── docs/                       # التوثيق
```

---

## 🚀 البدء السريع

### إنشاء ملف جديد

```bash
# في لوحة التحكم:
1. اذهب إلى Dashboard
2. انقر "New Scan"
3. أدخل username Instagram
4. اضغط "Analyze"
```

### استخدام الـ API

```bash
# جمع بيانات ملف شخصي
curl -X POST http://localhost:9003/api/profile/scan/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -d {"username": "target_user"}

# الحصول على التقارير
curl http://localhost:9003/api/reports/ \
  -H "Authorization: Token YOUR_TOKEN"
```

---

## ⚖️ إخلاء المسؤولية القانوني

```
⚠️ IMPORTANT LEGAL NOTICE ⚠️

هذه الأداة مخصصة حصراً للأغراض القانونية والأخلاقية:

✅ الاستخدامات المسموحة:
   • التحقيقات الأمنية الرسمية
   • البحث الأكاديمي
   • حماية البراءة الذمة
   • الحماية من الاحتيال والجرائم

❌ الاستخدامات الممنوعة:
   • الابتزاز والتحرش
   • انتهاك الخصوصية
   • سرقة البيانات
   • الجرائم الإلكترونية
   • التنصت غير المصرح به

المستخدم يتحمل المسؤولية الكاملة عن استخدام هذه الأداة.
يجب الامتثال لجميع القوانين المحلية والدولية.

تطوير هذا المشروع لا يعني قبول أي استخدام غير قانوني.
```

---

## 📖 التوثيق

- [دليل التثبيت](./docs/installation.md)
- [دليل المستخدم](./docs/user-guide.md)
- [مرجع الـ API](./docs/api-reference.md)
- [دليل التطوير](./docs/development.md)

---

## 👥 المساهمة

نرحب بالمساهمات! اقرأ [CONTRIBUTING.md](./CONTRIBUTING.md) أولاً.

---

## 📄 الترخيص

MIT License - اقرأ [LICENSE](./LICENSE)

---

## 📞 التواصل

- **Issues**: [GitHub Issues](https://github.com/aztv010-design/Instapy/issues)
- **Email**: support@instapy.local

---

**تم التطوير بواسطة:** Aztv010-Design  
**آخر تحديث:** 2025  
**الحالة:** 🔴 قيد التطوير النشط
