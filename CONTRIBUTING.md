# مساهمة في Instapy

شكراً لاهتمامك بالمساهمة في Instapy! 🎉

## القواعد الأساسية

### 1. الاحترام والأخلاقيات
- احترم خصوصية الآخرين
- استخدم الأداة بشكل قانوني وأخلاقي فقط
- لا تساهم بأي كود لأغراض غير قانونية

### 2. قبل البدء
- اقرأ [ملف إخلاء المسؤولية](./README.md#إخلاء-المسؤولية-القانوني)
- تأكد من توافق مساهمتك مع القوانين المحلية

### 3. خطوات المساهمة

```bash
# 1. Fork المشروع
git clone https://github.com/YOUR_USERNAME/Instapy.git

# 2. أنشئ فرع جديد
git checkout -b feature/your-feature-name

# 3. اكتب الكود
# - اتبع معايير PEP 8 (Python)
# - اتبع Airbnb Style Guide (JavaScript/React)

# 4. اختبر كودك
pytest

# 5. commit مع رسالة واضحة
git commit -m "feat: إضافة ميزة X"

# 6. Push للفرع الخاص بك
git push origin feature/your-feature-name

# 7. أنشئ Pull Request
```

## معايير الكود

### Python
```python
# ✅ Good
def analyze_profile(username: str) -> dict:
    """تحليل ملف شخصي على Instagram."""
    try:
        profile = fetch_profile(username)
        return process_data(profile)
    except Exception as e:
        logger.error(f"Error: {e}")
        return {}

# ❌ Bad
def analyze(u):
    x = fetch(u)
    return x
```

### JavaScript/React
```javascript
// ✅ Good
const ProfileAnalyzer = ({ username }) => {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    analyzeProfile(username).then(setData);
  }, [username]);
  
  return <ProfileCard data={data} />;
};

// ❌ Bad
const a = ({ u }) => {
  const [d, sd] = useState(null);
  fetch(u).then(sd);
  return <div>{d}</div>;
};
```

## أنواع المساهمات المقبولة

✅ **Features**
- إضافة ميزات جديدة
- تحسينات الأداء
- إصلاح الأخطاء

❌ **غير مقبول**
- الكود الذي ينتهك القوانين
- أدوات للتنصت غير المصرح به
- كود بدون توثيق

## عملية المراجعة

1. سيتم مراجعة PR الخاص بك
2. قد نطلب تعديلات
3. بعد الموافقة، سيتم دمجه في `main`

## أسئلة متكررة

**س: هل يمكن إضافة ميزة X؟**
- تأكد أنها قانونية وأخلاقية أولاً

**س: كم وقت تستغرق مراجعة PR؟**
- عادة 3-7 أيام

**س: هل هناك معايير محددة للاختبار؟**
- نعم، اكتب اختبارات لكل ميزة جديدة

---

شكراً لمساهمتك! 🙏
