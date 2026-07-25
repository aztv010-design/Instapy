# ML Models Guide

## Face Recognition

```python
import cv2
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1

class FaceRecognizer:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.mtcnn = MTCNN(device=self.device)
        self.model = InceptionResnetV1(pretrained='vggface2').eval().to(self.device)
    
    def recognize_faces(self, image_path):
        img = cv2.imread(image_path)
        faces = self.mtcnn(img)
        return faces
```

## Fake Account Detection

```python
from sklearn.ensemble import RandomForestClassifier

class FakeDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
    
    def predict(self, features):
        # features: [follower_ratio, activity_score, profile_completeness, ...]
        probability = self.model.predict_proba(features)
        return probability[0][1]  # Probability of being fake
```

## OCR Text Recognition

```python
import pytesseract
from PIL import Image

class TextRecognizer:
    @staticmethod
    def extract_text(image_path):
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='ara+eng')
        return text
```

## Model Training

```python
# training.py
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2
)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save model
model.save('models/fake_detector.h5')
```

## Using Trained Models

```python
import tensorflow as tf

# Load model
model = tf.keras.models.load_model('models/fake_detector.h5')

# Make predictions
predictions = model.predict(new_features)
```

## Performance Optimization

```python
# Use quantization for faster inference
converter = tf.lite.TFLiteConverter.from_saved_model('models/')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
```
