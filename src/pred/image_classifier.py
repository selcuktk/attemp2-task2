from pred.models.torch_pred import *
from pred.models.tf_pred import *
from pred.models.is_pred import *
from typing import Any


def torch_run_classifier(image: str) -> Any:
    img = load_image(image)  # loading image
    if img is None:
        return None
    input_batch = torch_preprocess(img)  # preprocessing image
    top_labels = torch_predict(input_batch, model=None)  # prediction
    return top_labels[0]


def tf_run_classifier(image: str) -> Any:
    img = load_image(image)
    if img is None:
        return None
    pred_results = tf_predict(img)
    pred_results["status_code"] = 200
    return pred_results


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