```python
import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import preprocess_input

def preprocess_image(image_path):
    """
    Preprocess an image for image classification.
    """
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def decode_predictions(preds, top=5):
    """
    Decode predictions to class labels.
    """
    from tensorflow.keras.applications.resnet50 import decode_predictions as dp
    return dp(preds, top=top)
```