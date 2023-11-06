```python
import cv2
import numpy as np
import tensorflow as tf
from utils import preprocess_image

def classify_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Load the trained model
    model = tf.keras.models.load_model('model.h5')

    # Predict the class of the image
    prediction = model.predict(np.array([preprocessed_image]))

    # Return the predicted class
    return np.argmax(prediction)

if __name__ == "__main__":
    image_path = 'test_image.jpg'
    predicted_class = classify_image(image_path)
    print(f'The predicted class of the image is: {predicted_class}')
```