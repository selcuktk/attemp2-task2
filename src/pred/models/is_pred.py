from utils import load_image
import os
from tensorflow.keras.models import load_model
import numpy as np
from fastapi import HTTPException


def is_preprocess(img):
    try:
        # Resize to (30, 30)
        img = img.resize((30, 30))

        # Convert to NumPy array
        img_array = np.array(img)

        # Add batch dimension (1, 30, 30, 3)
        img_batch = np.expand_dims(img_array, axis=0)

        return img_batch
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Image preprocessing failed: {str(e)}")


model = load_model(os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "Trafic_signs_model.h5"))


def get_model():
    return model


def get_labels():
    # dictionary to label all traffic signs class.
    # it is added from https://towardsdatascience.com/traffic-sign-recognition-using-deep-neural-networks-6abdb51d8b70/
    labels = {1: 'Speed limit (20km/h)',
              2: 'Speed limit (30km/h)',
              3: 'Speed limit (50km/h)',
              4: 'Speed limit (60km/h)',
              5: 'Speed limit (70km/h)',
              6: 'Speed limit (80km/h)',
              7: 'End of speed limit (80km/h)',
              8: 'Speed limit (100km/h)',
              9: 'Speed limit (120km/h)',
              10: 'No passing',
              11: 'No passing veh over 3.5 tons',
              12: 'Right-of-way at intersection',
              13: 'Priority road',
              14: 'Yield',
              15: 'Stop',
              16: 'No vehicles',
              17: 'Veh > 3.5 tons prohibited',
              18: 'No entry',
              19: 'General caution',
              20: 'Dangerous curve left',
              21: 'Dangerous curve right',
              22: 'Double curve',
              23: 'Bumpy road',
              24: 'Slippery road',
              25: 'Road narrows on the right',
              26: 'Road work',
              27: 'Traffic signals',
              28: 'Pedestrians',
              29: 'Children crossing',
              30: 'Bicycles crossing',
              31: 'Beware of ice/snow',
              32: 'Wild animals crossing',
              33: 'End speed + passing limits',
              34: 'Turn right ahead',
              35: 'Turn left ahead',
              36: 'Ahead only',
              37: 'Go straight or right',
              38: 'Go straight or left',
              39: 'Keep right',
              40: 'Keep left',
              41: 'Roundabout mandatory',
              42: 'End of no passing',
              43: 'End no passing veh > 3.5 tons'}
    return labels


def is_predict(input_batch):
    labels = get_labels()
    # Make prediction
    predictions = model.predict(input_batch)
    # Get the class with highest probability
    predicted_class = np.argmax(predictions)
    predicted_class = labels[predicted_class+1]
    # Get the probability of the predicted class
    probability = np.max(predictions)

    # Side effect for the function: Print the predicted class and its probability
    # print(f"Predicted class: {predicted_class} with probability: {probability:.4f}")

    return predicted_class, probability
