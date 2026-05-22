import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import os
# List of class labels
CLASS_LABELS = ['bacterial_blight', 'curl_virus', 'fussarium_wilt', 'healthy']

# Load the trained model
MODEL_PATH = 'model_vgg16.h5'

try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except OSError:
    print(f"Error: Model file '{MODEL_PATH}' not found. Please ensure the file is in the correct location.")
    exit()

def preprocess_image(image_path):
    """
    Preprocess the input image to make it compatible with the model.
    """
    try:
        # Load the image
        img = load_img(image_path, target_size=(224, 224))  # Resize to model input size
        img_array = img_to_array(img)  # Convert to array
        img_array = img_array / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions for batch size
        return img_array
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def predict_disease(image_path):
    """
    Predict the disease class of the input image.
    """
    img_array = preprocess_image(image_path)
    if img_array is None:
        return None, None

    # Make prediction
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)  # Get the index of the highest confidence score
    confidence = np.max(predictions) * 100  # Get the confidence percentage
    return CLASS_LABELS[class_index], confidence

if __name__ == "__main__":
    # Input image path
    image_path = input("Enter the path to the leaf image: ")

    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
    else:
        # Predict the disease
        disease, confidence = predict_disease(image_path)
        if disease:
            print(f"Predicted Disease: {disease}")
            print(f"Confidence: {confidence:.2f}%")
        else:
            print("Prediction failed. Please check the input image.")