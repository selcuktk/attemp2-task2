from pred.models.is_pred import *
from typing import Any

# is: internship
def internship_run_classifier(image: str) -> Any:
    img = load_image(image)  # loading image
    if img is None:
        return None
    input_batch = is_preprocess(img)  # preprocessing image
    predicted_class, probability = is_predict(input_batch)  # prediction
    return {
        "class": predicted_class,
        "confidence": round(float(probability), 4)
    }